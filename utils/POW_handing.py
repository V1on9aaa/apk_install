from typing import List, Dict, Any, Optional, Union
from abc import ABC, abstractmethod
import uiautomator2
from utils.utils import *
from setting import *
from utils.adb_utils import AdbCLI
from utils.ui2_utils import *
from utils.wx_ocr import *
from utils import *
from threading import Thread
# from utils.ocr_utils import *

class ClickStrategy(ABC):
    """点击策略抽象基类"""

    @abstractmethod
    def can_click(self, text: str, text_info: Dict[str, Any]) -> bool:
        """判断是否可以点击"""
        pass

    @abstractmethod
    def click(self, text: str, accurate_match: bool = True) -> bool:
        """执行点击操作"""
        pass


class UI2ClickStrategy(ClickStrategy):
    """UI2点击策略"""

    def __init__(self, ua2):
        self.ua2 = ua2

    def can_click(self, text: str, text_info: Dict[str, Any]) -> bool:
        """检查UI2文本是否可点击"""
        return text_info.get('clickable') == 'true'

    def click(self, text: str, accurate_match: bool = True) -> bool:
        """使用UI2点击"""
        return self.ua2.click_word(text, accurate_match)


class OCRClickStrategy(ClickStrategy):
    """OCR点击策略"""

    def __init__(self, adb_cli):
        self.adb_cli = adb_cli

    def can_click(self, text: str, text_info: Dict[str, Any]) -> bool:
        """OCR总是可以尝试点击"""
        return True

    def click(self, text: str, accurate_match: bool = True) -> bool:
        """使用OCR点击"""
        return self.adb_cli.click_word_ocr(text, accurate_match)


class AdbInputClickStrategy(ClickStrategy):
    """adb shell input点击策略"""

    def __init__(self, adb_cli):
        self.adb_cli = adb_cli

    def can_click(self, text: str, text_info: Dict[str, Any]) -> bool:
        """input总是可以尝试点击"""
        return True

    def click(self, text: str, accurate_match: bool = True) -> bool:
        """使用input点击"""
        btn = text.split('KEYCODE_')[-1]
        if len(btn) == 1:
            if str_word_is_int(btn):
                btn = int(btn)
        return self.adb_cli.KEYCODE_ALL(btn)

class TextFinder:
    """文本查找器，负责查找文本并返回查找结果"""

    def __init__(self, ua2, adb_cli):
        self.ua2 = ua2
        self.adb_cli = adb_cli

    def find_text(self, target_text: str, timeout: int = 30) -> Dict[str, Any]:
        """
        查找文本，返回查找结果
        返回格式: {'found': bool, 'text_info': Dict, 'source': str}
        """
        start_time = time.time()
        deadline = start_time + timeout

        while time.time() < deadline:
            # 判断是否是keycode
            if re.search('KEYCODE', target_text):
                return {
                    'found': True,
                    'text_info': {'text': target_text, 'clickable': True},
                    'source': 'AdbInput'
                }

            # 1. 首先尝试UI2查找
            ui2_texts = self.ua2.get_ui2_text()
            # print(ui2_texts)
            if target_text in ui2_texts:
                return {
                    'found': True,
                    'text_info': {'text': target_text, 'clickable': ui2_texts[target_text]},
                    'source': 'ui2'
                }

            # 2. 尝试OCR查找
            if self.adb_cli.search_word_by_ocr(target_text):
                return {
                    'found': True,
                    'text_info': {'text': target_text, 'clickable': True},
                    'source': 'ocr'
                }

            time.sleep(0.1)  # 避免CPU占用过高

        return {'found': False, 'text_info': {}, 'source': None}


class AndroidPopup:
    """Android弹窗处理类（优化版）"""

    def __init__(self, device, ocr_server):
        self.device = device
        self.ua2 = ui2(device)
        self.ocr_server = ocr_server
        self.uiauto2 = uiautomator2.connect(device)
        self.adb_cli = AdbCLI(device, self.ocr_server)

        # 初始化策略和查找器
        self.ui2_strategy = UI2ClickStrategy(self.ua2)
        self.ocr_strategy = OCRClickStrategy(self.adb_cli)
        self.AdbInput_strategy = AdbInputClickStrategy(self.adb_cli)
        self.text_finder = TextFinder(self.ua2, self.adb_cli)


        # 策略映射字典，替代if-else判断[1](@ref)[6](@ref)
        self.click_strategies = {
            'ui2': self.ui2_strategy,
            'ocr': self.ocr_strategy,
            'AdbInput': self.AdbInput_strategy
        }

    def _log_click(self, text: str, start_time: float, source: str, result=True):
        """统一的点击日志记录"""
        if result:
            pass
            # print(f'点击: {text}')
        else:
            pass
            # print(f'未点击: {text}')
        # print(f'{source}点击耗时: {round((time.time()-start_time), 2)}')

    def _execute_click(self, text: str, source: str, accurate_match: bool = True) -> bool:
        """
        执行点击操作
        使用策略模式替代if-else判断[8](@ref)
        """
        start_time = time.time()
        strategy = self.click_strategies.get(source)

        if not strategy:
            return False

        if strategy.click(text, accurate_match):
            self._log_click(text, start_time, source)
            return True
        else:
            self._log_click(text, start_time, source, False)
            return False


    def multiple_traversal_click(self, click_texts: List[str], clicks_num: int, timeout: int = 30):
        """多次遍历点击"""
        for _ in range(clicks_num):
            if not self.traversal_click(click_texts, timeout=timeout):
                break
            time.sleep(0.1)

    def multiple_precise_click(self, text_list: List[str], timeout: int = 30):
        """多次精确点击"""
        for text in text_list:
            if self.precise_click(text, timeout=timeout):
                continue
            else:
                self.precise_click(text, timeout=timeout)
            time.sleep(0.1)

    def traversal_click(self, text_list: List[str], timeout: int = 30) -> bool:
        """
        遍历点击（优化版）
        使用字典映射优化查找逻辑[1](@ref)[6](@ref)
        """
        # 使用集合提高查找效率[1](@ref)
        text_set = set(text_list)

        start_time = time.time()
        deadline = start_time + timeout

        while time.time() < deadline:
            # 1. 查找UI2文本
            ui2_texts = self.ua2.get_ui2_text()

            # 使用集合交集快速找到匹配的文本[5](@ref)
            matching_texts = text_set.intersection(set(ui2_texts.keys()))

            for text in matching_texts:
                if ui2_texts[text] == 'true':
                    if self._execute_click(text, 'ui2'):
                        return True
                else:
                    if self._execute_click(text, 'ocr'):
                        return True

            # 2. 查找OCR文本
            ocr_texts = self.adb_cli.screen_ocr_center_point()
            matching_ocr_texts = text_set.intersection(set(ocr_texts.keys()))

            for text in matching_ocr_texts:
                if self._execute_click(text, 'ocr'):
                    return True
            time.sleep(0.1)

        return False

    def precise_click(self, popup_text: str, timeout: int = 30, accurate_match: bool = True) -> bool:
        """
        精确点击（优化版）
        使用查找器统一查找逻辑，减少重复代码
        """
        # 使用查找器查找文本
        result = self.text_finder.find_text(popup_text, timeout)
        # print(result)

        if not result['found']:
            return False

        text_info = result['text_info']
        source = result['source']

        # 根据文本是否可点击选择策略
        if source == 'ui2' and text_info.get('clickable') == 'true':
            res = self._execute_click(popup_text, 'ui2', accurate_match)
        elif source == 'AdbInput':
            res = self._execute_click(popup_text, 'AdbInput', accurate_match)
        else:
            res = self._execute_click(popup_text, 'ocr', accurate_match)

        return res

    def password_click(self, timeout: int = 30):
        """
        1+7 : com.android.vending 弹窗
                BiometricPrompt 密码
        A11 : com.coloros.safecenter 密码

        """
        print('检测到需要输入密码，正在处理...\n输入: ')
        s_time = time.time()
        while time.time() > s_time + timeout:
            for p in pkg_password.keys():
                if self.adb_cli.search_force(p):
                    for i in text_split_2_ascii(pkg_password[p]):
                        self.adb_cli.KEYCODE_ALL(i)
                        print(i, end='')


    def popup_process(self, mode_set: Optional[str] = None, pop_mod='normal', timeout: int = 30):
        """
        弹窗处理（优化版）
        使用字典映射替代多个if判断[6](@ref)
        pop_mod=['normal', 'install', 'other']
        """
        popup_dict = {'install': 'install_pkgname', 'other': 'system_pkgname'}
        start_time = time.time()
        popup_data_ = popup_data()

        click_traversal_popup = popup_data_['click_traversal_popup']
        if pop_mod == 'normal':
            popup_pkgname_list = []
            for pkgname in popup_data_['popup_pkgname'].keys():
                for pkg in popup_data_['popup_pkgname'][pkgname]:
                    popup_pkgname_list.append(pkg)
        else:
            if pop_mod == 'install' or 'other':
                popup_pkgname_list = popup_data_['popup_pkgname'][popup_dict[pop_mod]]
            else:
                return False

        # 等待弹窗出现
        popup_check = 0
        while time.time() < start_time + timeout:
            android = AdbCLI(self.device, self.ocr_server)
            if android.popup_detection(popup_pkgname_list):
                print('当前界面存在弹窗，正在处理')
                popup_check = 1
                break
        if not popup_check:
            return

        # 使用字典映射处理模式选择[1](@ref)[6](@ref)
        popup_special = popup_data_['popup_special']

        # 模式选择逻辑
        if mode_set is not None:
            mode = mode_set
        elif self.device in popup_special:
            special_value = popup_special[self.device]
            if isinstance(special_value, list):
                if len(special_value) == 1 and type(special_value[0]) == int:
                    mode = 'plural_times'
                else:
                    mode = 'user-defined'
            else:
                raise 'popup_config.yaml: special_handling 配置错误'
        else:
            mode = 'normal'

        # 使用字典映射执行对应的方法[6](@ref)
        mode_handlers = {
            'normal': lambda: self.traversal_click(click_traversal_popup),
            'plural_times': lambda: self.multiple_traversal_click(
                click_traversal_popup, popup_special[self.device][0], timeout
            ),
            'user-defined': lambda: self.multiple_precise_click(
                popup_special[self.device], timeout
            )
        }
        handler = mode_handlers.get(mode)
        if handler:
            handler()
        else:
            print(f"未知模式: {mode}")








