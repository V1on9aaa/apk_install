import os
import re
import time
import subprocess
from typing import Dict, List, Optional, Tuple, Union
from pathlib import Path
from functools import lru_cache
from datetime import datetime
from setting import *
from utils.utils import *



class AdbCLI:
    """ADB命令行工具类（优化版）"""

    # 命令模板字典，减少字符串拼接
    COMMAND_TEMPLATES = {
        'install': '{adb_exe} -s {device} install {pkg_path}',
        'shell': '{adb_shell} {command}',
        'push': '{adb_exe} -s {device} push {src} {dst}',
        'pull': '{adb_exe} -s {device} pull {src} {dst}',
        'uninstall': '{adb_exe} -s {device} uninstall {pkg_name}',
        'screencap': '{adb_shell} "screencap -p {path}"',
        'am_start': '{adb_shell} "am start {activity}"',
        'am_stop': '{adb_shell} "am force-stop {pkg}"',
        'pm_list': '{adb_shell} "pm list package | grep {pkg_name}"',
        'ps_grep': '{adb_shell} "ps | grep {pkg_name}"',
        'getprop': '{adb_shell} "getprop {prop_name}"',
        'wm_size': '{adb_shell} "wm size"',
        'dumpsys_window': '{adb_shell} "dumpsys window | grep mCurrentFocus"',
        'dumpsys_input': '{adb_shell} "dumpsys input | grep SurfaceOrientation"',
        'dumpsys_package': '{adb_shell} "dumpsys package {pkg_name} | grep -A 1 android.intent.action.MAIN:"',
        'get_focus': '{adb_shell} "dumpsys window | grep mCurrentFocus"',
        'get_process': '{adb_shell} "ps | grep {pkg_name}"',
        'get_log_low': '{adb_shell} "cat /sdcard/sdk/log.log"',
        'get_log_high': '{adb_shell} "cat /sdcard/Android/data/{pkg_name}/files/log.log"',
        'get_shell_log_low': '{adb_shell} "cat /sdcard/sdk/shell.log | grep OpenID"',
        'get_shell_log_high': '{adb_shell} "cat /sdcard/Android/data/{pkg_name}/files/shell.log | grep OpenID"',
        'pull_log_low': '{adb_exe} -s {device} pull /sdcard/sdk/log.log {out_path}',
        'pull_log_high': '{adb_exe} -s {device} pull /sdcard/Android/data/{pkg_name}/files/log.log {out_path}',
        'input_tap': '{adb_shell} "input tap {x} {y}"',
        'input_swipe': '{adb_shell} "input swipe {x1} {y1} {x2} {y2} {duration}“',
        'keyevent': '{adb_shell} input keyevent {keycode}',
        'grant_permission': '{adb_shell} pm grant {pkg_name} {permission}',
        'screenshot': '{adb_shell} screencap -p {path}',
        'pull_screenshot': '{adb_exe} -s {device} pull "{remote_path}" "{local_path}"',
        'remove_file': '{adb_shell} rm -rf "{remote_path}"',
        'set_screen_off_time': '{adb_shell} "settings put system screen_off_timeout 1800000"'
    }

    # 权限列表常量
    PERMISSIONS = [
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.READ_EXTERNAL_STORAGE'
    ]

    # 键码映射字典，提高可读性和可维护性
    KEYCODE_MAP = {
        'POWER': 26,
        'HOME': 3,
        'BACK': 4,
        'MENU': 82,
        'ENTER': 66,
        'VOLUME_UP': 24,
        'VOLUME_Down': 25,
        'DEL': 67,
        'SPACE': 62
    }

    def __init__(self, device: str, ocr_server=None, tools_path: str = tools_path):
        """初始化ADB命令行工具

        Args:
            device: 设备序列号
            tools_path: ADB工具路径
        """
        self.device = device
        self.tools_path = Path(tools_path)
        self.adb_exe = str(self.tools_path / 'adb.exe')
        self.adb_shell = f'{self.adb_exe} -s {self.device} shell '
        self.ocr_server = ocr_server


        # 缓存常用属性
        self._version_cache = None
        self._resolution_cache = None
        self._screen_path = Path(screen_path) if 'screen_path' in globals() else Path('.temp/screenshots')
        self._screen_path.mkdir(parents=True, exist_ok=True)
        self._surface_cache = None
        self._api_version_cache = None
        self._abi_cache = None

    def _build_command(self, command_type: str, **kwargs) -> str:
        """构建ADB命令，使用模板减少字符串拼接[1](@ref)[2](@ref)"""
        if command_type not in self.COMMAND_TEMPLATES:
            raise ValueError(f"不支持的命令类型: {command_type}")

        # 使用字典解包填充模板
        params = {
            'adb_exe': self.adb_exe,
            'adb_shell': self.adb_shell,
            'device': self.device,
            **kwargs
        }
        return self.COMMAND_TEMPLATES[command_type].format(**params)

    def _run_command(self, command: str, decode_type: str = 'gbk') -> str:
        """执行命令的通用方法，减少重复代码"""
        try:
            return cmd_single_run(command, decode_type)
        except Exception as e:
            print(f"命令执行失败: {command}, 错误: {e}", flush=True)
            return ""

    def _get_current_time(self, format_str: str = '%H:%M:%S') -> str:
        """获取当前时间格式化字符串"""
        return datetime.now().strftime(format_str)

    @lru_cache(maxsize=32)
    def ver(self) -> int:
        """获取Android版本号（使用缓存）[1](@ref)"""
        if self._version_cache is not None:
            return self._version_cache

        result = self._run_command(f'{self.adb_shell} getprop ro.build.version.release')
        if not result:
            return 0

        # 使用正则表达式提取版本号
        match = re.search(r'(\d+)', result)
        self._version_cache = int(match.group(1)) if match else 0
        return self._version_cache

    @lru_cache(maxsize=10)
    def get_focus(self) -> str:
        """获取当前焦点窗口（使用缓存）[2](@ref)[6](@ref)"""
        return self._run_command(self._build_command('dumpsys_window'))

    def search_force(self, pkgname: str) -> Optional[re.Match]:
        """搜索指定包名的焦点窗口"""
        focus = self.get_focus()
        return re.search(pkgname, focus)

    @lru_cache(maxsize=1)
    def get_resolution_ratio(self) -> tuple:
        """获取设备分辨率（使用缓存）"""
        if self._resolution_cache is not None:
            return self._resolution_cache

        result = self._run_command(f'{self.adb_shell} wm size')
        if not result:
            self._resolution_cache = (0, 0)
            return self._resolution_cache

        # 使用列表推导式提取数字
        numbers = re.findall(r'\d+', result)
        self._resolution_cache = (int(numbers[0]), int(numbers[1]))
        return self._resolution_cache

    @lru_cache(maxsize=1)
    def get_surface(self) -> int:
        """获取屏幕方向（使用缓存）[2](@ref)[6](@ref)"""
        if self._surface_cache is not None:
            return self._surface_cache

        result = self._run_command(self._build_command('dumpsys_input'))
        if not result:
            self._surface_cache = 0
            return self._surface_cache

        numbers = re.findall(r'\d+', result)
        self._surface_cache = int(numbers if numbers else 0)
        return self._surface_cache

    @lru_cache(maxsize=1)
    def get_api_ver(self) -> int:
        """获取API版本（使用缓存）[2](@ref)[6](@ref)"""
        if self._api_version_cache is not None:
            return self._api_version_cache

        result = self._run_command(self._build_command('getprop', prop_name='ro.build.version.sdk'))
        self._api_version_cache = int(result.strip()) if result.strip().isdigit() else 0
        return self._api_version_cache

    @lru_cache(maxsize=1)
    def get_abi(self) -> str:
        """获取设备ABI（使用缓存）[2](@ref)[6](@ref)"""
        if self._abi_cache is not None:
            return self._abi_cache

        result = self._run_command(self._build_command('getprop', prop_name='ro.product.cpu.abi'))
        self._abi_cache = result.strip().split('\r\n')[0] if result else ""
        return self._abi_cache

    def get_permission(self, file: str) -> str:
        """修改文件权限"""
        return self._run_command(self._build_command('shell', command=f'chmod 777 "{file}"'))

    def adb_push(self, file: str, push_to: str) -> str:
        """推送文件到设备"""
        return self._run_command(self._build_command('push', src=file, dst=push_to))

    def adb_pull(self, file: str, pull_to: str) -> str:
        """从设备拉取文件"""
        return self._run_command(self._build_command('pull', src=file, dst=pull_to))

    def uninstall_pkg(self, pkg_name: str) -> str:
        """卸载应用"""
        return self._run_command(self._build_command('uninstall', pkg_name=pkg_name))

    def set_off_time(self, Time: int = 1800000):
        return self._run_command(self._build_command('set_screen_off_time', pkg_name=Time))

    def install_apk(self, pkg_path: str) -> str:
        """安装APK（优化版）[1](@ref)[3](@ref)

        Args:
            pkg_path: APK文件路径

        Returns:
            安装结果
        """
        android_version = self.ver()

        # 根据版本选择命令
        if android_version <= 6:
            command = self._build_command('install', pkg_path=pkg_path)
        else:
            command = f'{self.adb_exe} -s {self.device} install -g "{pkg_path}"'

        try:
            return self._run_command(command)
        except UnicodeDecodeError:
            return self._run_command(command, decode_type='utf-8')

    def install_apk_abi(self, pkg_path: str, abi: str) -> str:
        """安装指定ABI的APK（优化版）[1](@ref)[3](@ref)

        Args:
            pkg_path: APK文件路径
            abi: ABI类型

        Returns:
            安装结果
        """
        android_version = self.ver()

        if android_version <= 6:
            command = self._build_command('install', pkg_path=pkg_path)
        else:
            command = f'{self.adb_exe} -s {self.device} install --abi {abi} -g "{pkg_path}"'

        return self._run_command(command)

    def install_apks(self, apks: str) -> str:
        """安装APKS文件"""
        command = f'java -jar {self.tools_path}\\bundletool.jar install-apks --adb {self.adb_exe} --apks {apks} --device-id {self.device}'
        return self._run_command(command, 'gbk')

    def reinstall_pkg(self, pkg_path: str) -> None:
        """重新安装应用（优化版）[1](@ref)[3](@ref)

        Args:
            pkg_path: 应用文件路径
        """
        # 使用字典映射文件类型处理逻辑
        file_handlers = {
            '.apk': self._reinstall_apk,
            '.aab': self._reinstall_aab
        }

        # 获取文件扩展名
        file_ext = os.path.splitext(pkg_path)[1].lower()

        if file_ext in file_handlers:
            file_handlers[file_ext](pkg_path)
        else:
            print(f'不支持的文件类型: {file_ext}', flush=True)

    def _reinstall_apk(self, pkg_path: str) -> None:
        """重新安装APK"""
        pkg_name = get_pkg_name(pkg_path)

        if self.pkg_exists(pkg_name):
            self.uninstall_pkg(pkg_name)
            print('已卸载同包名app', flush=True)

        size_mb = round(get_size(pkg_path) / (1024 * 1024), 2)
        print(f"正在安装 {pkg_path}\n文件大小：{size_mb}MB", flush=True)

        self.install_apk(pkg_path)
        self.set_enable(pkg_name, 'shell')

    def _reinstall_aab(self, pkg_path: str) -> None:
        """重新安装AAB"""
        pkg_name = get_aab_name(pkg_path)

        if self.pkg_exists(pkg_name):
            self.uninstall_pkg(pkg_name)
            print('已卸载同包名app', flush=True)

        size_mb = round(get_size(pkg_path) / (1024 * 1024), 2)
        print(f"正在安装 {pkg_path}\n文件大小：{size_mb}MB", flush=True)

        apks = extract(pkg_path, None)
        self.install_apks(apks)
        self.set_enable(pkg_name, 'shell')

    def pkg_exists(self, pkg_name: str, timeout: int = 10) -> bool:
        """检查包是否存在（优化版）[1](@ref)[3](@ref)

        Args:
            pkg_name: 包名
            timeout: 超时时间（秒）

        Returns:
            包是否存在
        """
        deadline = time.time() + timeout
        command = self._build_command('pm_list', pkg_name=pkg_name)

        while time.time() < deadline:
            try:
                result = self._run_command(command)
                pkg_list = result.splitlines()
                set_pkgs = set(pkg_list)
                pkg = ['package:'+pkg_name]
                set_pkg = set(pkg)
                if len(set_pkg.intersection(set_pkgs)) != 0:
                    return True
            except Exception:
                return False
            time.sleep(0.1)  # 避免CPU占用过高[1](@ref)

        return False

    def popup_detection(self, popup_list: List[str], ) -> bool:
        """弹窗检测（优化版）[1](@ref)[4](@ref)

        Args:
            popup_list: 弹窗包名列表

        Returns:
            检测结果字典
        """
        # 使用集合提高查找效率[1](@ref)[2](@ref)
        focus = self.get_focus()

        # 检查弹窗
        for pkgname in popup_list:
            if pkgname in focus:
                return True

        # 检查OCR文本
        # if text_location is not None:
        #     result['text'] = 1 if self.search_word_by_ocr(text_location) else 0
        return False

    def pop_up_win_focus(self, popup_list: List[str]) -> bool:
        """检查弹窗窗口焦点（优化版）[1](@ref)[4](@ref)

        Args:
            popup_list: 弹窗包名列表

        Returns:
            是否存在弹窗焦点
        """
        focus = self.get_focus()
        # 使用any()提高效率[1](@ref)[5](@ref)
        return any(popup in focus for popup in popup_list)

    def start_app(self, pkg_name: str) -> bool:
        """启动应用（优化版）[1](@ref)[3](@ref)

        Args:
            pkg_name: 包名

        Returns:
            是否启动成功
        """
        try:
            # 使用字典存储版本对应的解析逻辑
            version_parsers = {
                '<=5': lambda res: res.split('\n')[1].split(' '),
                '>5': lambda res: res.split('\n')[1].split(' ')
            }
            # 获取活动信息
            command = self._build_command('dumpsys_package', pkg_name=pkg_name)
            result = self._run_command(command)

            if not result:
                print(f'未找到对应包名: {pkg_name}', flush=True)
                return False

            # 解析活动名称
            android_version = self.ver()
            parser = version_parsers['<=5'] if android_version <= 5 else version_parsers['>5']
            # print(parser)
            parts = parser(result)

            # 使用列表推导式过滤空字符串[1](@ref)[5](@ref)
            clean_parts = [part for part in parts if part]
            # print(clean_parts)

            if len(clean_parts) < 2:
                print(f'无法解析活动名称: {pkg_name}', flush=True)
                return False

            activity_name = clean_parts[1]
            # print(activity_name)

            # 启动应用
            self._run_command(self._build_command('am_start', activity=activity_name))
            return True

        except Exception as e:
            print(f'启动 {pkg_name} 失败: {e}', flush=True)
            return False

    def stop_app(self, pkg: str) -> None:
        """停止应用"""
        self._run_command(self._build_command('am_stop', pkg=pkg))

    def get_pid(self, pkg_name: str) -> Optional[str]:
        """获取进程ID（优化版）[1](@ref)[3](@ref)

        Args:
            pkg_name: 包名

        Returns:
            进程ID或None
        """
        result = self._run_command(self._build_command('ps_grep', pkg_name=pkg_name))
        if not result:
            return None

        # 使用split()和strip()简化处理
        lines = result.strip().split('\n')
        for line in lines:
            if line.strip():
                # 提取PID（第二列）
                parts = line.split()
                if len(parts) >= 2:
                    return parts[1]

        return None

    def kill_pid(self, pid: str) -> str:
        """杀死进程（优化版）[1](@ref)[3](@ref)

        Args:
            pid: 进程ID

        Returns:
            执行结果
        """
        try:
            # 使用subprocess.Popen的上下文管理器
            with subprocess.Popen(
                    self.adb_exe + ' -s ' + self.device + ' shell',
                    shell=True,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,  # 使用文本模式
                    encoding='utf-8'
            ) as proc:
                # 发送命令
                proc.stdin.write('su\n')
                proc.stdin.write(f'kill {pid}\n')
                proc.stdin.flush()

                # 获取输出
                output, error = proc.communicate(timeout=5)
                return output if output else error

        except subprocess.TimeoutExpired:
            return "命令执行超时"
        except Exception as e:
            return f"执行失败: {e}"

    def set_enable(self, pkg_name: str, enable_set: str, config_path: str = config_path) -> None:
        """设置应用启用状态（优化版）[1](@ref)[3](@ref)

        Args:
            pkg_name: 包名
            enable_set: 启用设置类型
            config_path: 配置文件路径
        """
        # 使用字典存储启用类型配置[1](@ref)[2](@ref)
        enable_types = {
            'shell': '0000000000000000090910009000000000000',
            'sdk': '0000000000000000090900009000000000000',
            'all_1': '1111111111111111111111111111111111111111111',
            'official': '0000000000000000090000009000000000000',
            'perf_68': '000000000000000009009000000000000000000000000000000000000000000000009'
        }

        if enable_set not in enable_types:
            print(f'未知的启用类型: {enable_set}', flush=True)
            return

        enable = enable_types[enable_set]
        config_dir = Path(config_path)

        # 使用上下文管理器自动关闭文件[6](@ref)
        try:
            # 读取模板文件
            adv_template_path = config_dir / 'adv_ver_template.txt'
            low_template_path = config_dir / 'low_ver_template.txt'

            with open(adv_template_path, 'r', encoding='utf-8') as f:
                adv_template = f.readlines()

            with open(low_template_path, 'r', encoding='utf-8') as f:
                low_template = f.readlines()

            # 生成配置文件
            adv_config_path = config_dir / 'adv_ver.txt'
            low_config_path = config_dir / 'low_ver.txt'

            with open(low_config_path, 'w', encoding='utf-8') as f:
                for line in low_template:
                    f.write(line.replace('pkg_name', pkg_name).replace('enable_set', enable))

            with open(adv_config_path, 'w', encoding='utf-8') as f:
                for line in adv_template:
                    f.write(line.replace('pkg_name', pkg_name).replace('enable_set', enable))

            # 根据Android版本执行不同命令
            android_version = self.ver()

            if android_version >= 9:
                # 高版本
                command = f'{self.adb_exe} -s {self.device} shell < {adv_config_path}'
                self._run_command(command)
            elif android_version <= 5:
                # 最低版本
                commands = [
                    f'{self.adb_exe} -s {self.device} shell mkdir /sdcard/sdk/',
                    f'{self.adb_exe} -s {self.device} shell "echo {enable} > /sdcard/sdk/enable.log"'
                ]
                for cmd in commands:
                    self._run_command(cmd)
            else:
                # 低版本6-8
                command = f'{self.adb_exe} -s {self.device} shell < {low_config_path}'
                self._run_command(command)

        except FileNotFoundError as e:
            print(f'配置文件不存在: {e}', flush=True)
        except Exception as e:
            print(f'设置启用状态失败: {e}', flush=True)



    def check_app(self, pkg_name: str) -> bool:
        """
        检测app是否闪退（包含检测前台应用、进程、截图）
        优化点：减少重复代码，提高可读性，使用集合操作提高效率[1](@ref)[2](@ref)
        """
        time_str = self._get_current_time()

        # 并行执行两个检查命令
        focus_result = self._run_command(self._build_command('get_focus'))
        process_result = self._run_command(self._build_command('get_process', pkg_name=pkg_name))

        # 使用集合操作检查包名是否存在
        is_in_focus = pkg_name in focus_result
        is_in_process = pkg_name in process_result

        # 使用字典映射状态消息，减少if-else嵌套
        status_messages = {
            (True, True): f'{self.device} {pkg_name}在前台 {time_str}\n{self.device} {pkg_name}进程存活 {time_str}\n',
            (True, False): f'{self.device} {pkg_name}在前台 {time_str}\n{self.device} {pkg_name}进程死亡 发生闪退 {time_str}\n',
            (False,
             True): f'{self.device} {pkg_name}不在前台 请检查是否有弹窗，或是已经闪退 {time_str}\n{self.device} {pkg_name}进程存活 {time_str}\n',
            (False,
             False): f'{self.device} {pkg_name}不在前台 请检查是否有弹窗，或是已经闪退 {time_str}\n{self.device} {pkg_name}进程死亡 发生闪退 {time_str}\n'
        }

        print(status_messages[(is_in_focus, is_in_process)], flush=True)

        # 返回检查结果
        return is_in_focus and is_in_process

    def click_point(self, point: Tuple[int, int]) -> bool:
        """点击指定坐标点"""
        try:
            x, y = point
            command = self._build_command('input_tap', x=x, y=y)
            self._run_command(command)
            return True
        except Exception:
            return False

    def click(self, x_y: Tuple[float, float]) -> bool:
        """点击相对坐标（基于屏幕分辨率）"""
        try:
            x, y = x_y
            width, height = self.get_resolution_ratio()

            if width == 0 or height == 0:
                return False
            # print(x_y)
            # 计算实际坐标
            actual_x = round(width * x, 1)
            actual_y = round(height * y, 1)
            # print(actual_x, actual_y)
            return self.click_point((actual_x, actual_y))
        except Exception:
            return False

    def swipe(self, start_point: Tuple[float, float], end_point: Tuple[float, float],
              duration: int = 300) -> bool:
        """滑动操作"""
        try:
            x1, y1 = start_point
            x2, y2 = end_point

            # 获取分辨率并计算实际坐标
            width, height = self.get_resolution_ratio()
            if width == 0 or height == 0:
                return False

            actual_x1 = round(width * x1, 1)
            actual_y1 = round(height * y1, 1)
            actual_x2 = round(width * x2, 1)
            actual_y2 = round(height * y2, 1)

            # 构建滑动命令
            command = self._build_command(
                'input_swipe',
                x1=actual_x1, y1=actual_y1,
                x2=actual_x2, y2=actual_y2,
                duration=duration
            )

            self._run_command(command)
            return True
        except Exception:
            return False

    def _get_log_command(self, pkg_name: str, log_type: str = 'log') -> str:
        """根据Android版本获取日志命令"""
        android_version = self.ver()

        command_map = {
            ('log', 'low'): self._build_command('get_log_low'),
            ('log', 'high'): self._build_command('get_log_high', pkg_name=pkg_name),
            ('shell_log', 'low'): self._build_command('get_shell_log_low'),
            ('shell_log', 'high'): self._build_command('get_shell_log_high', pkg_name=pkg_name)
        }

        version_key = 'low' if android_version <= 9 else 'high'
        return command_map.get((log_type, version_key), '')

    def get_log(self, pkg_name: str) -> Optional[str]:
        """获取应用日志"""
        try:
            command = self._get_log_command(pkg_name, 'log')
            if not command:
                return None

            result = self._run_command(command)

            # 检查文件是否存在
            if 'No such file or directory' in result:
                # 尝试备用路径
                backup_command = self._build_command('get_log_low')
                result = self._run_command(backup_command)

                if 'No such file or directory' in result:
                    print(f'{self.device} 未生成log.log', flush=True)
                    return None

            # 提取openid
            match = re.search(r'user_info->uin_.uin_str_:.*', result)
            if match:
                return match.group()

            return None
        except Exception:
            print('获取log.log失败，未生成log.log或未接入sdk\n', flush=True)
            return None

    def get_shell_log(self, pkg_name: str) -> Optional[str]:
        """获取shell日志"""
        try:
            command = self._get_log_command(pkg_name, 'shell_log')
            if not command:
                return None

            result = self._run_command(command)

            if 'No such file or directory' in result:
                return '未生成shell.log'

            # 使用列表推导式处理日志行
            lines = [line.strip() for line in result.split('\n') if line.strip()]
            if not lines:
                return None

            # 获取倒数第二行（假设最后一行可能是空行）
            last_line = lines[-2] if len(lines) >= 2 else lines[-1]

            # 提取OpenID
            match = re.search(r'OpenID:.*,', last_line)
            return match.group() if match else None

        except Exception:
            print('获取shell.log失败', flush=True)
            return None

    def pull_log(self, pkg_name: str, out_path: str) -> bool:
        """拉取日志文件到本地"""
        try:
            android_version = self.ver()

            # 使用字典映射命令选择
            command_map = {
                True: self._build_command('pull_log_low', out_path=out_path),
                False: self._build_command('pull_log_high', pkg_name=pkg_name, out_path=out_path)
            }

            command = command_map[android_version <= 9]
            result = self._run_command(command)

            if 'No such file or directory' in result:
                # 尝试备用路径
                backup_command = command_map[not (android_version <= 9)]
                result = self._run_command(backup_command)

                if 'No such file or directory' in result:
                    print(f'{self.device} 未生成log.log', flush=True)
                    return False

            return True
        except Exception:
            print('获取log.log失败，未生成log.log或未接入sdk\n', flush=True)
            return False

    def log_out(self, pkgname: str, pkgpath: str, alive_or_not: bool,
                crash_pkg: List[str], out_path: str) -> None:
        """记录日志输出"""
        # 并行获取两种日志
        openid = self.get_log(pkgname)
        shell_openid = self.get_shell_log(pkgname)

        # 使用三元表达式简化赋值
        openid = openid if openid else '无openid'
        shell_openid = shell_openid if shell_openid else '无shell_openid'

        # 拉取日志文件
        self.pull_log(pkgname, out_path)

        # 准备日志内容
        time_str = datetime.now().strftime('%Y-%m-%d')
        log_file_path = Path(log_path) / f'{time_str}.txt'

        # 构建日志消息
        if alive_or_not:
            log_message = f'>>>{pkgpath}\n{pkgname}未闪退，运行正常\n{openid}\n{shell_openid}\n\n'
        else:
            # 使用any()函数简化判断[1](@ref)
            if any(crash == pkgname for crash in crash_pkg):
                log_message = f'>>>{pkgpath}\n{pkgname}发生预期内闪退\n{openid}\n{shell_openid}\n\n'
            else:
                log_message = f'>>>{pkgpath}\n{pkgname}发生闪退\n{openid}\n{shell_openid}\n\n'

        # 写入日志文件
        with open(log_file_path, 'a', encoding='utf-8') as file:
            file.write(log_message)

    def permission(self, pkg_name: str) -> None:
        """给应用授予权限"""
        for permission in self.PERMISSIONS:
            command = self._build_command('grant_permission', pkg_name=pkg_name, permission=permission)
            self._run_command(command)

    def _send_keyevent(self, keycode: int) -> bool:
        """发送按键事件（内部方法）"""
        try:
            command = self._build_command('keyevent', keycode=keycode)
            self._run_command(command)
            return True
        except Exception:
            return False

    def KEYCODE_BUTTON(self, STR: str) -> bool:
        return self._send_keyevent(self.KEYCODE_MAP[STR])

    def KEYCODE_num(self, num: int) -> bool:
        """数字键（0-9）"""
        if 0 <= num <= 9:
            keycode = num + 7  # Android数字键码映射
            return self._send_keyevent(keycode)
        return False

    def KEYCODE_majuscule(self, majuscule: str) -> bool:
        """字母键（A-Z）"""
        text = majuscule.upper()
        if len(text) == 1 and 65 <= ord(text) <= 91:
            keycode = ord(text) - 36  # Android数字键码映射
            return self._send_keyevent(keycode)
        return False

    def KEYCODE_ALL(self, word: str or int) -> bool:
        """
        按键点击
        Args:
            word: 1-9 or A-Z or
            ['POWER', 'HOME', 'BACK', 'MENU', 'ENTER', 'VOLUME_UP', 'VOLUME_Down', 'DEL', 'SPACE']
        """
        try:
            if type(word) == int:
                self.KEYCODE_num(word)
            elif len(word) == 1 and type(word) == str:
                self.KEYCODE_majuscule(word)
            else:
                self.KEYCODE_BUTTON(word)
            return True
        except:
            return False

    def screen(self, out_path: str, name: str) -> bool:
        """截图并保存到本地"""
        try:
            # 生成唯一文件名
            remote_path = f'/sdcard/{name}.png'
            local_path = Path(out_path) / f'{name}.png'

            # 确保本地目录存在
            local_path.parent.mkdir(parents=True, exist_ok=True)

            # 执行截图命令
            screenshot_cmd = self._build_command('screenshot', path=remote_path)
            pull_cmd = self._build_command('pull_screenshot',
                                           remote_path=remote_path,
                                           local_path=str(local_path))
            remove_cmd = self._build_command('remove_file', remote_path=remote_path)

            # 执行命令序列
            self._run_command(screenshot_cmd)
            self._run_command(pull_cmd)
            self._run_command(remove_cmd)

            return True
        except Exception:
            return False


    def screen_ocr(self) -> Dict[str, any]:
        """屏幕OCR识别"""
        name = f'ocr_{int(time.time())}'
        screenshot_success = self.screen(str(self._screen_path), name)

        if not screenshot_success:
            return {}

        pic_path = self._screen_path / f'{name}.png'
        return self.ocr_server.ocr_single(str(pic_path))[0]

    def screen_ocr_center_point(self) -> Dict:
        ocr_results = self.screen_ocr()
        return self.ocr_server.box_center_point(ocr_results)

    def click_word_ocr(self, text: str, accurate_match: bool = True) -> bool:
        """通过OCR识别文本并点击"""
        name = f'click_{int(time.time())}'
        screenshot_success = self.screen(str(self._screen_path), name)

        if not screenshot_success:
            return False

        img_path = str(self._screen_path / f'{name}.png')

        # 获取点击坐标
        permit = self.ocr_server.match_text(img_path, text, accurate_match)['point']
        # print(permit)

        # 执行点击
        return self.click(permit)

    def search_word_by_ocr(self, text: str, accurate_match: bool = True) -> bool:
        """通过OCR搜索文本"""
        name = f'search_{int(time.time())}'
        screenshot_success = self.screen(str(self._screen_path), name)

        if not screenshot_success:
            return False

        img_data = self.screen_ocr()
        # print(img_data)

        # 使用字典推导式或生成器表达式提高效率[1](@ref)[2](@ref)
        if accurate_match:
            # 精确匹配
            return any(key['text'] == text for key in img_data)
        else:
            # 模糊匹配
            pattern = re.compile(text)
            return any(pattern.search(key['text']) for key in img_data)
