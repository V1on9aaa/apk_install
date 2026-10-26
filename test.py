# from public import phone_link
#
# link = phone_link('18fdf3fd')
#
# link.install_apk(r'D:\shell\need_shell\Tools.apk')

# import minidevice

# d = 'zpa66l5lyhf6lj5t'


# from pyplist import XMLParser as plt
#
#
#
# # 读取 XML 格式的 plist 文件
# f = open(r'D:\sdk\7.2.2.18249\demo\Info.plist', 'rb').read()
# a = plt.parseFile(r'D:\sdk\7.2.2.18249\demo\Info.plist')
#
# print(a)

# # 修改配置并写回文件
# config['key'] = 'value'
# with open('config.plist', 'wb') as f:
#     plist.dump(config, f)

# ===========================================================================
# import time
# import zipfile
# import shutil
#
# import pyautogui
# import pygetwindow as gw
# import autoit

# window = gw.getActiveWindow()
# windows = gw.getAllWindows()
# print(windows)
# print(window)
#
#
# autoit.run('E:\VOWSoft iPod Software\plist Editor Pro\plistEditor.exe')
# plist = gw.getWindowsWithTitle('D:\shell\IOS_Shell\ipa_sign\Info.plist')
# print(gw.getAllTitles())
# time.sleep(0.5)
# print(plist)
# p = plist[0]
# print(p)
# print(p.title)
# p.activate()
# time.sleep(0.5)
# print(p.isActive)


# ===============================================================================
# import time
# import zipfile
# import shutil
# import autoit
# from autoit import properties
# import pywinauto
# from pywinauto.application import Application

# print(autoit.win_get_text('D:\shell\IOS_Shell\ipa_sign\Info.plist', 'XML View'))
# a = pywinauto.Application('uia')
# plist = pywinauto.Application('uia').connect(title='D:\shell\IOS_Shell\ipa_sign\Info.plist')
# print(plist.window_text())
# print(pyautogui.Window(title='D:\shell\IOS_Shell\ipa_sign\Info.plist').isActive())


# autoit.run('E:\VOWSoft iPod Software\plist Editor Pro\plistEditor.exe')
# autoit.win_wait_active('plist Editor Pro for Windows', 3)
# print(autoit.win_get_handle('plist Editor Pro for Windows'))
# print(autoit.win_get_handle())
# autoit.win_menu_select_item('plist Editor Pro for Windows', '', 'File', 'Open')
# autoit.control_click('plist Editor Pro for Windows', '', 'File', 'Open')
# print(autoit.control_get_text)
# autoit.control_click('D:\shell\IOS_Shell\ipa_sign\Info.plist', '', 'File', 'Open')

# time.sleep(1)
# autoit.win_close('plist Editor Pro for Windows')

# =============================================================================
# import time
# import os
# import zipfile
# import shutil
# import autoit
# from autoit import properties
# import pywinauto
# from pywinauto import Application
#
# import win32gui

# hwnd_title = {}
#
#
# def get_all_hwnd(hwnd, mouse):
#     if (win32gui.IsWindow(hwnd)
#             and win32gui.IsWindowEnabled(hwnd)
#             and win32gui.IsWindowVisible(hwnd)):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#
#
# win32gui.EnumWindows(get_all_hwnd, 0)
# for h, t in hwnd_title.items():
#     if t:
#         print(h, t)
# if __name__ == '__main__':
#     pass

# print(win32gui.FindWindow('wxWindowNR', 'D:\shell\IOS_Shell\ipa_sign\Info.plist'))
# print(win32gui.GetMenu(1775702))
# print(win32gui.GetSubMenu(4294935298, 0))


# os.popen('D:\shell\IOS_Shell\ipa_sign\Info.plist')
# time.sleep(2)
# plist = gw.getWindowsWithTitle('D:\shell\IOS_Shell\ipa_sign\Info.plist')
# time.sleep(1)
# p = plist[0]
# p.activate()
# # print(autoit.win_get_text('D:\shell\IOS_Shell\ipa_sign\Info.plist'))
# autoit.control_send('D:\shell\IOS_Shell\ipa_sign\Info.plist', 'XML View', '^a')

# app = Application(backend='uia')
# app.connect(process=1324)
# d = app.window()
# d.print_control_identifiers()
# print(app.is64bit())

# ============================================================================
# a = 'asdfzcvdfaermfghdzcvdaadasdqeasd'
#
# b = a.replace('12', 'ab')
# print(a)
# print(b)

# from gooey import Gooey, GooeyParser
#
# @Gooey(program_name="自动安装运行脚本（apk、aab）", language="chinese", default_size=(1100, 600))
# def init():
#     parser = GooeyParser(description='请选择配置')
#     machine = parser.add_subparsers(dest='result')
#     android = machine.add_parser('android')
#     android.add_argument('devices', widget='Dropdown', metavar='设备', choices=['0', '1'], default='0')
#
#     args = parser.parse_args()
#     if args.result == 'android':
#         OS = 'android'
#         Devices = args.devices
#
# init()


# import os
# import time
#
# print(type(time.time()))

# print(os.popen('adb -s b7b2e062 shell am start com.tencent.sdk/com.tencent.foogame.MainActivity', 'r').read())

# def start_app(usb, pkg_name):
#     # 打开app
#     res = os.popen(f'adb -s {usb} shell "dumpsys package {pkg_name}|grep -A 1 android.intent.action.MAIN:"', 'r').read()
#     sstr = []
#     print(res)
#     for msg in res.split('\n')[2].split(' '):
#         if msg != '':
#             sstr.append(msg)
#     print(sstr)
#     name_act = sstr[1]
#     start = os.popen(f'adb -s {usb} shell am start {name_act}', 'r').read()
#     return start
#
# start_app('b7b2e062', 'com.tencent.sdk')

# from public import *
#
# usb = 'b7b2e062'
# android = Android_device(usb)
# res = android.start_app_test('com.tencent.sdk')
# print(res)
# import re
#
# res = 'package:com.wind.bird2'
# pkg = 'com.wind.bird2'
#
#
# print(res)
# print(pkg)
# print(re.search(pkg, res))

# ==================================================================================
# import os
# from device import Android_dev
# import time

# device = '18fdf3fd'
# android = Android_dev.Android_device(device)
# import socket
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# result = sock.connect_ex(('127.0.0.1', 5001))
#
# if result == 0:
#     print("Port is open")
# else:
#     print("Port is not open")

# dir = r'D:\code\python\All_project\adb_install\temp\screen\minicap\18fdf3fd'
# stmtime = []
# for file in os.listdir(dir):
#     stmtime.append(os.path.join(dir, file))
# while len(stmtime) >= 10:
#     os.remove(stmtime[0])
#     stmtime.remove(stmtime[0])

# ==========================================================================================
# import multiprocessing
# import time
# import os
#
#
# def worker_function(name):
#     """进程执行的函数"""
#     print(f"Worker {name} (PID: {os.getpid()}) 开始运行")
#     try:
#         while True:
#             print(f"Worker {name} 正在工作...")
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print(f"Worker {name} 收到中断信号")
#     finally:
#         print(f"Worker {name} 结束运行")
#
#
# class ProcessManager:
#     """进程管理器，负责创建、终止和重启进程"""
#
#     def __init__(self, target, args=()):
#         self.target = target
#         self.args = args
#         self.process = None
#
#     def start(self):
#         """启动新进程"""
#         if self.is_running():
#             print("进程已经在运行中")
#             return
#
#         # 创建新的进程对象
#         self.process = multiprocessing.Process(
#             target=self.target,
#             args=self.args
#         )
#         self.process.start()
#         print(f"已启动进程，PID: {self.process.pid}")
#
#     def stop(self):
#         """终止当前进程"""
#         if not self.is_running():
#             print("没有运行中的进程")
#             return
#
#         # 终止进程
#         self.process.terminate()
#         # 等待进程结束
#         self.process.join(timeout=5)
#
#         # 检查进程是否已经结束
#         if self.process.is_alive():
#             print("强制终止进程")
#             self.process.kill()
#
#         print(f"进程 (PID: {self.process.pid}) 已终止")
#         self.process = None
#
#     def restart(self):
#         """重启进程"""
#         print("重启进程...")
#         self.stop()
#         self.start()
#
#     def is_running(self):
#         """检查进程是否在运行"""
#         return self.process is not None and self.process.is_alive()
#
#
# if __name__ == "__main__":
#     # 创建进程管理器
#     manager = ProcessManager(worker_function, args=("测试进程",))
#
#     try:
#         # 第一次启动
#         manager.start()
#         time.sleep(3)
#
#         # 重启进程
#         manager.restart()
#         time.sleep(3)
#
#         # 再次重启
#         manager.restart()
#         time.sleep(3)
#
#         # 停止进程
#         manager.stop()
#
#     except KeyboardInterrupt:
#         print("主程序收到中断信号")
#         manager.stop()

# ========================================================================================
# import socket
#
# def check_port(port: int):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result = sock.connect_ex(('127.0.0.1', port))
#     print(result)
#
#     if result == 0:
#         return True
#     else:
#         return False
#
#
# print(check_port(5000))

#  =====================================================================================
# import socket
# import threading
# import time
# import os
# import struct
# import keyboard
# from PIL import Image
# import io
# import shutil
#
# # 配置参数
# DEVICE_ID = "9e2bd91c"
# PORT = 5000
# MAX_IMAGES = 50
# CAPTURE_INTERVAL = 0.5  # 秒
# INITIAL_RESOLUTION = (1440, 3120)
#
#
# class MinicapCapture:
#     def __init__(self):
#         self.running = False
#         self.paused = False
#         self.image_count = 0
#         self.image_list = []
#         self.current_resolution = INITIAL_RESOLUTION
#         self.socket = None
#         self.thread = None
#         self.buffer = b''
#
#         # 创建存储目录
#         if not os.path.exists(r'.\temp\screen\minicap'):
#             os.makedirs(r'.\temp\screen\minicap')
#
#     def connect(self):
#         """连接到minicap服务"""
#         try:
#             self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             self.socket.connect(('localhost', PORT))
#             print(f"已连接到minicap服务 (端口: {PORT})")
#             return True
#         except Exception as e:
#             print(f"连接失败: {e}")
#             return False
#
#     def parse_header(self, data):
#         """解析minicap头部信息"""
#         if len(data) < 24:
#             return None
#
#         header = struct.unpack('<BBBBHHIIII', data[:24])
#         version = header[0]
#         length = header[1]
#         pid = header[2]
#         real_width = header[4]
#         real_height = header[5]
#         virtual_width = header[6]
#         virtual_height = header[7]
#
#         # 检查分辨率是否有变化
#         new_resolution = (virtual_width, virtual_height)
#         if new_resolution != self.current_resolution:
#             self.current_resolution = new_resolution
#             print(f"分辨率已变更为: {self.current_resolution[0]}x{self.current_resolution[1]}")
#
#         return {
#             'version': version,
#             'length': length,
#             'pid': pid,
#             'real_size': (real_width, real_height),
#             'virtual_size': (virtual_width, virtual_height)
#         }
#
#     def capture_loop(self):
#         """截图主循环"""
#         while self.running:
#             if self.paused:
#                 time.sleep(0.1)
#                 continue
#
#             try:
#                 # 读取数据
#                 data = self.socket.recv(4096)
#                 if not data:
#                     break
#
#                 self.buffer += data
#
#                 # 检查是否有完整的帧
#                 while len(self.buffer) >= 4:
#                     # 解析帧长度
#                     frame_size = struct.unpack('<I', self.buffer[:4])[0]
#
#                     # 检查是否有完整的帧
#                     if len(self.buffer) < 4 + frame_size:
#                         break
#
#                     # 提取帧数据
#                     frame_data = self.buffer[4:4 + frame_size]
#                     self.buffer = self.buffer[4 + frame_size:]
#
#                     # 解析头部（第一帧包含头部信息）
#                     if self.image_count == 0:
#                         self.parse_header(frame_data)
#
#                     # 处理图像数据
#                     img = Image.open(io.BytesIO(frame_data))
#
#                     # 保存图像
#                     timestamp = int(time.time() * 1000)
#                     filename = rf".\temp\screen\minicap\{DEVICE_ID}_{timestamp}.png"
#                     img.save(filename)
#
#                     # 管理图像列表
#                     self.image_list.append(filename)
#                     self.image_count += 1
#
#                     # 超过上限则删除最早的
#                     if len(self.image_list) > MAX_IMAGES:
#                         oldest = self.image_list.pop(0)
#                         if os.path.exists(oldest):
#                             os.remove(oldest)
#                             print(f"已删除 oldest image: {oldest}")
#
#                     print(f"已保存截图 {self.image_count}, 分辨率: {self.current_resolution[0]}x{self.current_resolution[1]}")
#
#                     # 等待指定间隔
#                     time.sleep(CAPTURE_INTERVAL)
#
#             except Exception as e:
#                 print(f"捕获过程出错: {e}")
#                 time.sleep(1)
#
#     def start(self):
#         """开始捕获过程"""
#         if not self.running:
#             if self.connect():
#                 self.running = True
#                 self.paused = False
#                 self.thread = threading.Thread(target=self.capture_loop)
#                 self.thread.start()
#                 print("开始截图 (按Home键暂停/继续, End键退出)")
#
#     def pause_resume(self):
#         """暂停或继续捕获"""
#         if self.running:
#             self.paused = not self.paused
#             if self.paused:
#                 print("已暂停截图")
#             else:
#                 print("已恢复截图")
#
#     def stop(self):
#         """停止捕获过程"""
#         self.running = False
#         self.paused = False
#         if self.thread:
#             self.thread.join()
#         if self.socket:
#             self.socket.close()
#         print("已停止截图，程序退出")
#
#
# if __name__ == "__main__":
#     capture = MinicapCapture()
#
#     # 设置键盘事件监听
#     keyboard.add_hotkey('home', capture.pause_resume)
#     keyboard.add_hotkey('end', lambda: capture.stop())
#
#     # 启动捕获
#     capture.start()
#
#     # 保持主线程运行
#     try:
#         while capture.running:
#             time.sleep(0.1)
#     except KeyboardInterrupt:
#         capture.stop()

# =========================================================================
# import time
# from utils.adb_utils import *
# from utils.ui2_utils import *
# from setting import *
# import uiautomator2 as uiauto
# import xml.etree.ElementTree as ET
# import re
# import os.path

# device = '9e2bd91c'
# out_path = r'D:\code\python\All_project\adb_install_02\temp\screen'

# dev = uiauto.connect(device)
# dd = ui2(device)
# aa = adb_CLI(device)



# print(time.time())
# popup_exists = aa.popup_exists(popup_list)
# print(popup_exists)
# print(time.time())
# popup_exists_ = aa.popup_exists(popup_list, '安全守护提示您')
# print(popup_exists_)
# print(time.time())
#
# print(time.time())
# popup_exists = dd.popup_exists(popup_list)
# print(popup_exists)
# print(time.time())
# popup_exists_ = dd.popup_exists(popup_list, '安全守护提示您')
# print(popup_exists_)
# print(time.time())

# print(dev.info)
# print(time.time())
# print(dev.app_current()['package'])
# print(time.time())

# print(time.time())
# print(aa.get_Focus())
# print(time.time())

# GG_button, check_, b, first, secend = [], [], [], [], []
# qq = dev()
# dev.watcher.when()

# app_info = dev.app_start('com.tencent.green.ace')
# print(app_info)

# xml_str = dev.dump_hierarchy()
# print(xml_str)
# root = ET.fromstring(xml_str)

# all_texts = {}
# for r in root.iter():
#     clickable = r.attrib.get('clickable')
#     text = r.attrib.get('text')
#     if text and text.strip() != '':
#         all_texts[text.strip()] = clickable
#
# print(all_texts)

# qq[5].click()
# for i in qq:
#     print(i.info)

# if i.info['contentDescription'] == '应用列表':
#     qq[0].click()
# if i.info['text'] == '游戏崩溃了':
#     print(True)
# GG_button.append(i.bounds())
# check_.append(i.bounds()[3])
#     print(i.bounds())

# print(GG_button)
# print(check_)
#
# for c in check_:
#     b.append(check_.count(c))
# print(b)
#
# for jk in range(len(b)):
#     if b[jk] == 6:
#         first.append(GG_button[jk])
#     if b[jk] == 8:
#         secend.append(GG_button[jk])
#
# print(first)
# print(secend)

# AD = Android_device(device)
# print(AD.screen_ocr(out_path, 'ocr'))
# AD.click_word_ocr('tlog_sdk', 'sdk', False)


# print(dev(text='TPTest').bounds())
# dev(text='完成')[0].click(timeout=30)
# dev(text='继续安装')[0].click(timeout=1)


# dd = dev(text='tlog_sdk')
# dd[0].long_click(1)
# ee = dev(text='卸载应用')
# ee[0].click(timeout=1)
# ff = dev(text='卸载')
# ff[0].click(timeout=1)

# from device.Android_dev import *
# device = '1c6e05a'
# pkg_name = 'com.tencent.tmgp.sgame'
# AD = Android_device(device)
# print(AD.pkg_exists(pkg_name, 120))

# ==========================================================================

# from multiprocessing import Process
#
# def aa(T):
#     time.sleep(T)
#
# TT = 5
# p_install = Process(target=aa, args=(TT,))
#
# if __name__ == '__main__':
#     p_install.start()
#     print(p_install.is_alive())
#     while p_install.is_alive() is True:
#         pass
#         print(p_install.is_alive())
#     print(0)

# =================================================================================
# import re
#
# a = 'afzveqfaf11111'
# b = '65413z6f86adf4'
#
# print(re.search('111', a))
# print(type(re.search('111', a)))
# print(re.search('111', b))
# print(type(re.search('111', b)))

# ===============================================================================
# import yaml
#
# def read_yaml(yaml_path):
#     with open(yaml_path, 'r', encoding='utf-8') as f:
#         data = yaml.load(stream=f, Loader=yaml.FullLoader)
#     return data
#
# popup_config = os.path.abspath('./Tools/config/popup_config.yaml')
# y_data = read_yaml(popup_config)
# click_traversal_popup = y_data['click_traversal_popup']
# popup_pkgname = y_data['popup_pkgname']
# devices, popup_, popup_special = [], [], {}
# for i in y_data['special_handling']:
#     for x in i.keys():
#         devices.append(x)
#     for y in i.values():
#         if len(y) == 1 and type(y[0]) == int:
#             popup_.append(y[0])
#         else:
#             popup_.append(y)
# for j in range(len(devices)):
#     popup_special[devices[j]] = popup_[j]
#
# print(click_traversal_popup)
# print(popup_pkgname)
# print(popup_special)
# print(popup_special['9e2bd91c'])
# print(type(popup_special['18fdf3fd']))
# print(type(popup_special['9e2bd91c']))

# =============================================================================
# from task import *
#
# def install_test(device):
#     android = adb_CLI(device)
#     popup_ps = Android_popup(device)
#     pkg_path = r'G:\Business_Area\shell\Andriod_Shell\5.1.X\5.1.1.53884\111'
#     pkg_type = check_endswith(pkg_path)
#
#     for apk in pkg_type['apk']:
#         pkg_name = get_pkg_name(apk)
#         p_install = Process(target=install_process, args=(device, apk))
#         p_install.start()
#         popup_ps.popup_process(timeout=500)
#         p_install.join(timeout=500)
#         android.set_enable(pkg_name, 'shell')
#         android.permission(pkg_name)
#         print(f'第一次启动 {pkg_name}', flush=True)
#         android.start_app(pkg_name)
#         time.sleep(5)
#         popup_ps.popup_process(mode_set='normal')
#         if android.check_app(pkg_name) == False:
#             print(f'第二次启动 {pkg_name}', flush=True)
#             android.start_app(pkg_name)
#             time.sleep(5)
#             popup_ps.popup_process(mode_set='normal')
#             time.sleep(30)
#             if android.check_app(pkg_name) == False:
#                 print(f'{pkg_name} 30s内闪退\n', flush=True)
#                 break
#             else:
#                 t = float(5) * 60
#                 time.sleep(t)
#         else:
#             t = float(5)*60
#             time.sleep(t)
#         name = pkg_name + '_' + str(round(time.time(), 0))
#         android.screen(screen_path, name)
#         check = android.check_app(pkg_name)
#         log_name = log_path + '\\Android\\' + device + '_' + str(round(time.time())) + '_log.log'
#         android.log_out(pkg_name, apk, check, crash_pkg, log_name)
#         android.stop_app(pkg_name)
#         time.sleep(1)


# if __name__ == '__main__':
#     device = '9e2bd91c'
#     install_test(device)

# Android = adb_CLI('8LAILJWWVKCUVK49')
# tencent123 = [48, 33, 42, 31, 33, 42, 48, 8, 9, 10]
# for n in tencent123:
#     Android.KEYCODE_num(n)
# Android.click_word_ocr('安装')

# =====================================================================================
# import tkinter as tk
# from tkinter import Menu
# import sys
#
# class GUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title('演示窗口')
#         self.root.geometry("500x200+1100+150")
#         # 创建主菜单实例
#         self.menubar = Menu(self.root)
#         # 显示菜单,将root根窗口的主菜单设置为menu
#         self.root.config(menu=self.menubar)
#         self.interface()
#
#     def interface(self):
#         """"界面编写位置"""
#         # 在 menubar 上设置菜单名，并关联一系列子菜单
#         self.menubar.add_cascade(label="文件", menu=self.papers())
#         self.menubar.add_cascade(label="查看", menu=self.about())
#
#         self.Button0 = tk.Button(self.root, text="运行", command=self.event)
#         self.Button0.grid(row=0, column=0, padx=20)
#
#         # 使用lambda表达式创建了一个匿名函数，该函数会调用self.add_page方法并传递参数
#         self.Button1 = tk.Button(self.root, text="确定", command=lambda: self.print_tk('hello world'))
#         self.Button1.grid(row=0, column=1, padx=20)
#
#         self.Button2 = tk.Button(self.root, text="退出", command=self.root.destroy, bg="Gray")  # bg=颜色
#         self.Button2.grid(row=0, column=2, padx=20)
#
#         self.Label0 = tk.Label(self.root, text="文本显示")
#         self.Label0.grid(row=1, column=0)
#
#     def papers(self):
#         """
#         fmenu = Menu(self.menubar): 创建子菜单实例
#         tearoff=1: 1的话多了一个虚线,如果点击的话就会发现,这个菜单框可以独立出来显示
#         fmenu.add_separator(): 添加分隔符"--------"
#         """
#         fmenu = Menu(self.menubar, tearoff=0)
#         # 创建单选框
#         for item in ['新建', '打开', '保存', '另存为']:
#             fmenu.add_command(label=item)
#         return fmenu
#
#     def about(self):
#         amenu = Menu(self.menubar, tearoff=0)
#         # 添加复选框
#         for item in ['项目复选框', '文件扩展名', '隐藏的项目']:
#             amenu.add_checkbutton(label=item)
#         return amenu
#
#     def event(self):
#         """按钮事件"""
#         print("运行成功")
#
#     def parameter(self, data):
#         """传入参数"""
#         print(f"获取到的参数: {data}")
#
#     def print_tk(self, data):
#         # 创建文本框用于显示输出
#         output_text = tk.Text(self.root)
#         output_text.pack()
#
#         # 重定向标准输出到文本框
#         redirect_stdout_to_tkinter(output_text)
#
#         # 执行print语句，输出将显示在文本框中
#         print(data)
#
# def redirect_stdout_to_tkinter(text_widget):
#     class StdoutRedirector:
#         def __init__(self, text_widget):
#             self.text_widget = text_widget
#
#         def write(self, message):
#             self.text_widget.insert('end', message)
#             self.text_widget.see('end')
#
#     sys.stdout = StdoutRedirector(text_widget)
#
# if __name__ == '__main__':
#     a = GUI()
#     a.root.mainloop()

# def parameter(data):
#     """传入参数"""
#     print(f"获取到的参数: {data}")
#
# # 创建Tkinter窗口
# window = tk.Tk()
#
# # 创建文本框用于显示输出
# output_text = tk.Text(window)
# output_text.pack()
#
# # 重定向标准输出到文本框
# redirect_stdout_to_tkinter(output_text)
#
# # 执行print语句，输出将显示在文本框中
# print("Hello, Tkinter!")
#
# # 运行Tkinter主循环
# window.mainloop()

# ==============================================================================
'''
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date:2023-12-13 v1.0


import sys
import time
import tkinter as tk
from tkinter import scrolledtext  # 导入滚动文本框的模块

# 生成主窗口，命名 window
root = tk.Tk()
# 定义主窗口标题
root.title('xxx程序')
# 定义主窗口的长宽，窗体距离屏幕上下的距离
root.geometry('800x500+100+60')


# 定义日志输出到tkiner类
class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.insert(tk.END, str)  # 在text末尾追加文字
        self.text_widget.see(tk.END)  # 光标一直追加到文件末尾
        self.text_widget.update()  # 一直更新输出

    def flush(self):
        pass


# 控制台输出函数，输出到t1
def ternimal_print(msg):
    DATE_TIME = time.strftime('[%Y-%m-%d %H:%M:%S]')
    t1.insert('end', f'{DATE_TIME}  {msg}\n')  # 向text文本框末尾追加文字
    t1.see(tk.END)  # 光标一直追加到文件末尾
    t1.update()  # 一直更新输出


# 定义按钮事件相关函数
def fun1():
    sys.stdout = StdoutRedirector(t1)  # 重定向标准输出
    t1.delete(1.0, tk.END)  # 清除text文本框原来文字
    ternimal_print('程序运行开始.....')
    print('这是 按钮1 的输出文字')
    for i in range(30):
        ternimal_print(f'程序运行中。。。{i}')
        time.sleep(0.1)


def fun2():
    sys.stdout = StdoutRedirector(t1)  # 重定向标准输出
    t1.delete(1.0, tk.END)  # 清除原来终端输出的内容
    ternimal_print('程序运行开始.....')
    print('这是 按钮2 的输出文字')
    ternimal_print('程序运行结束')


# 定义按钮相关组件
frm1 = tk.Frame(root)
frm1.pack()
button1 = tk.Button(frm1, text='功能1', font=('宋体', 12, 'bold'), command=fun1)
button1.pack(side='left', padx=20, pady=20, ipadx=20, ipady=10)
button2 = tk.Button(frm1, text='功能2', font=('宋体', 12, 'bold'), command=fun2)
button2.pack(side='left', padx=20, pady=20, ipadx=20, ipady=10)
button3 = tk.Button(frm1, text='退出', font=('宋体', 12, 'bold'), command=root.quit)
button3.pack(side='left', padx=20, pady=20, ipadx=20, ipady=10)

# 定义Laber组件
frm2 = tk.Frame(root)
frm2.pack(anchor='w')
l1 = tk.Label(frm2, text='程序运行日志：', font=('宋体', 12))
l1.pack(side='left', padx=1, pady=1, ipadx=1, ipady=1)

# 定义滚动文本组件
frm3 = tk.Frame(root)
frm3.pack(anchor='w')
t1 = scrolledtext.ScrolledText(frm3, width=200, height=300, bg='#cfdccf', font=('宋体', 13))
t1.pack(fill='both', side='left', expand=True)

# 启动默认打开帮助页面
sys.stdout = StdoutRedirector(t1)  # 重定向标准输出到t1
print('欢迎使用，这是测试文字')

# 启动窗口main
tk.mainloop()
'''

# ======================================================================
import time

'''
import tkinter
import time
import sys
from tkinter import scrolledtext  # 导入滚动文本框的模块

tk = tkinter.Tk()
tk.title('简单示例')
tk.geometry('300x200+200+20')

def comfun(data):
    print(data)

# 控制台输出函数，输出到t1
def ternimal_print(msg):
    DATE_TIME = time.strftime('[%Y-%m-%d %H:%M:%S]')
    t1.insert('end', f'{DATE_TIME}  {msg}\n')  # 向text文本框末尾追加文字
    t1.see(tkinter.END)  # 光标一直追加到文件末尾
    t1.update()  # 一直更新输出

# 定义日志输出到tkiner类
class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.insert(tkinter.END, str)  # 在text末尾追加文字
        self.text_widget.see(tkinter.END)  # 光标一直追加到文件末尾
        self.text_widget.update()  # 一直更新输出

    def flush(self):
        pass

# 菜单条
menubar = tkinter.Menu(tk)
tk.config(menu=menubar)

# 把菜单创建到菜单条上 创建菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)
# 给菜单选项添加内容
for item in ['PHP', 'C', 'C++', 'Python', 'Go', 'JS', 'Mysql', '退出']:
    if item == '退出':
        menu1.add_command(label=item, command=tk.quit)
    else:
        print(item)
        menu1.add_command(label=item, command=lambda: comfun(item))

# 向菜单条上添加菜单选项
menubar.add_cascade(label='语言', menu=menu1)

# 定义滚动文本组件
frm3 = tkinter.Frame(tk)
frm3.pack(anchor='w')
t1 = scrolledtext.ScrolledText(frm3, width=200, height=300, bg='#cfdccf', font=('宋体', 12))
t1.pack(fill='both', side='left', expand=True)

# 启动默认打开帮助页面
sys.stdout = StdoutRedirector(t1)  # 重定向标准输出到t1
print('欢迎使用，这是测试文字')

tk.mainloop()

'''

# ====================================================================================
'''
import sys
import time
import tkinter as tk
from tkinter import scrolledtext  # 导入滚动文本框的模块
from tkinter import filedialog



# 定义日志输出到tkiner类
class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.insert(tk.END, str)  # 在text末尾追加文字
        self.text_widget.see(tk.END)  # 光标一直追加到文件末尾
        self.text_widget.update()  # 一直更新输出

    def flush(self):
        pass

def fun2(data):
    print(data)

def selectPath_file():
    path_ = filedialog.askopenfilename(filetypes=[("安装包", [".apk", ".aab"])])
    var_pkg.set(path_)

# 输入文件夹路径
def selectPath_dir():
    path_ = filedialog.askdirectory()
    var_pkg.set(path_)

def change_enable(data):
    print(f'enable设置为{data}')
    var_enable.set(data)

root = tk.Tk()
root.title('自动化工具')
root.geometry('1000x600+100+50')

var_pkg = tk.StringVar()  # 文件输入路径变量
var_enable = tk.StringVar()

l1 = tk.Label(root, text='设备ID：', font=('宋体', 11))
l1.place(x=5, y=5, anchor='nw')
ent1 = tk.Entry(root, font=('宋体', 12))
ent1.place(x=135, y=5, width=300, height=25, anchor='nw')
l2 = tk.Label(root, text='包体或文件夹：', font=('宋体', 11))
l2.place(x=5, y=30, anchor='nw')
ent2 = tk.Entry(root, font=('宋体', 12), textvariable=var_pkg)
ent2.place(x=135, y=30, width=300, height=25, anchor='nw')
l3 = tk.Label(root, text='enable类型：', font=('宋体', 11))
l3.place(x=5, y=55, anchor='nw')
ent3 = tk.Entry(root, font=('宋体', 12), textvariable=var_enable)
ent3.place(x=135, y=55, width=300, height=25, anchor='nw')
l4 = tk.Label(root, text='运行时间(分钟)：', font=('宋体', 11))
l4.place(x=5, y=80, anchor='nw')
ent4 = tk.Entry(root, font=('宋体', 12))
ent4.place(x=135, y=80, width=300, height=25, anchor='nw')

button1 = tk.Button(root, text='打印', font=('宋体', 12, 'bold'), command=lambda: fun2([ent1.get(), ent2.get(), ent3.get(), ent4.get()]))
button1.place(x=5, y=115, width=100, height=50, anchor='nw')
button2 = tk.Button(root, text='启动', font=('宋体', 12, 'bold'), command=lambda: fun2(ent1.get()))
button2.place(x=105, y=115, width=100, height=50, anchor='nw')
button3 = tk.Button(root, text='退出', font=('宋体', 12, 'bold'), command=root.quit)
button3.place(x=205, y=115, width=100, height=50, anchor='nw')

button4 = tk.Button(root, text='选择安装包', font=('宋体', 11), command=selectPath_file)
button4.place(x=455, y=30, width=100, height=25, anchor='nw')
button5 = tk.Button(root, text='选择文件夹', font=('宋体', 11), command=selectPath_dir)
button5.place(x=555, y=30, width=100, height=25, anchor='nw')

button6 = tk.Menubutton(root, text='选择', font=('宋体', 11), state='active')
button6.place(x=455, y=55, width=50, height=25, anchor='nw')
enable_menu = tk.Menu(button6, tearoff=False)
enable_menu.add_checkbutton(label='sdk测试服', command=lambda: change_enable('0000000000000000090900009000000000000'))
enable_menu.add_checkbutton(label='壳测试服', command=lambda: change_enable('0000000000000000090910009000000000000'))
enable_menu.add_checkbutton(label='43位1', command=lambda: change_enable('1111111111111111111111111111111111111111111'))
enable_menu.add_checkbutton(label='性能', command=lambda: change_enable('000000000000000009009000000000000000000000000000000000000000000000009'))
enable_menu.add_checkbutton(label='正式服', command=lambda: change_enable('1111111111111111111111111111111111111111111'))
button6.config(menu=enable_menu)

# 定义Laber组件
l5 = tk.Label(root, text='程序运行日志：', font=('宋体', 12))
l5.place(x=5, y=175)

# 定义滚动文本组件
t1 = scrolledtext.ScrolledText(root, bg='#cfdccf', font=('宋体', 13))
t1.place(x=5, y=200, width=990, height=395, anchor='nw')

try:
    canvas = tk.Canvas(root, width=100, height=100)
    picture = tk.PhotoImage(file="auto_.png")
    image = canvas.create_image(0, 0, anchor="nw", image=picture)
    canvas.place(x=805, y=5)
except:
    pass


# 启动默认打开帮助页面
sys.stdout = StdoutRedirector(t1)  # 重定向标准输出到t1
print('欢迎使用，这是测试文字')

# 启动窗口main
tk.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
# window.geometry('1000x500+100+50')
# Button = tk.Button
#
# window.title('test')
# btn1 = Button(window, text="Button 1")
# btn2 = Button(window, text="Button 2")
#
# btn1.place(x=10, y=10)
# btn2.place(x=50, y=50)
#
# window.mainloop()
'''

# =============================================================================================
# import threading
# import time
# from pynput.keyboard import Controller, Key, Listener
#
# task_over = False
#
# def main_threading():
#     t_start = time.time()
#     while time.time() < t_start + 10:
#         print('main keep going')
#         time.sleep(1)
#         if task_over == True:
#             break
#     print('main over')
#
#
# def t1_threading():
#     with Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()
#
# def on_press(key):
#     try:
#         print(f'press {key.char}')
#     except AttributeError:
#         print(f'press {key}')
#
# def on_release(key):
#     global task_over
#     print(f'relese {key}')
#     if key == Key.end:
#         task_over = True
#         return False
#
# if __name__ ==  '__main__':
#     main = threading.Thread(target=main_threading)
#     t1 = threading.Thread(target=t1_threading)
#     t1.setDaemon(True)
#     main.start()
#     t1.start()

# ===================================================================================
# import os
# import json
# import time
# from wechat_ocr.ocr_manager import OcrManager, OCR_MAX_TASK_ID
#
# wechat_ocr_dir = r"C:\Users\v_pjinjpan\AppData\Roaming\Tencent\WXWork\WeChatOCR\1.0.1.20\WeChatOCR\WeChatOCR.exe"  # OCR的地址，可以用everythin工具查找一下地址
# wechat_dir = r"C:\Users\v_pjinjpan\AppData\Roaming\Tencent\WXWork\WeChatOCR\1.0.1.20\WeChatOCR"  # 一定是要包含mmmojo.dll的路径
#
#
# def ocr_result_callback(img_path: str, results: dict):
#     """
#     OCR 结果回调函数
#     """
#     result_file = os.path.basename(img_path) + ".json"
#     print(f"识别成功，img_path: {img_path}, result_file: {result_file}")
#
#     with open(result_file, 'w', encoding='utf-8') as f:
#         f.write(json.dumps(results, ensure_ascii=False, indent=2))
#
#     # 打印 results 的内容以便调试
#     print("OCR 结果：", json.dumps(results, ensure_ascii=False, indent=2))
#
#     # 尝试提取识别的文字
#     if 'ocrResult' in results:
#         text_lines = [item['text'] for item in results['ocrResult']]
#         print(f"识别的文字: {text_lines}")
#     else:
#         print("结果中没有 'ocrResult' 键，无法提取文字。")
#
#
# def main():
#     # 创建 OCR 管理器实例
#     ocr_manager = OcrManager(wechat_dir)
#     # 设置 WeChatOCR 目录
#     ocr_manager.SetExePath(wechat_ocr_dir)
#     # 设置微信所在路径
#     ocr_manager.SetUsrLibDir(wechat_dir)
#     # 设置 OCR 识别结果的回调函数
#     ocr_manager.SetOcrResultCallback(ocr_result_callback)
#     # 启动 OCR 服务
#     ocr_manager.StartWeChatOCR()
#     # 开始识别图片
#     ocr_manager.DoOCRTask(r"C:\Users\v_pjinjpan\Downloads\企业微信截图_17660431572602.png")
#     # 等待 OCR 任务完成
#     time.sleep(1)
#     while ocr_manager.m_task_id.qsize() != OCR_MAX_TASK_ID:
#         pass
#     # 结束 OCR 服务
#     ocr_manager.KillWeChatOCR()
#
#
# if __name__ == "__main__":
#     main()

# ======================================================================================
'''
from abc import ABC, abstractmethod
import json
import os
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, asdict


# 定义一个数据类用于存储结构化数据
@dataclass
class UserData:
    """用户数据类"""
    username: str
    email: str
    age: int
    is_active: bool = True


# 定义抽象基类 - 文件处理器接口
class FileHandler(ABC):
    """文件处理抽象基类，定义统一的文件读写接口[1](@ref)[6](@ref)"""

    @abstractmethod
    def read(self, filepath: str) -> Any:
        """
        抽象方法：读取文件内容
        :param filepath: 文件路径
        :return: 解析后的数据
        """
        pass

    @abstractmethod
    def write(self, filepath: str, data: Any) -> None:
        """
        抽象方法：写入数据到文件
        :param filepath: 文件路径
        :param data: 要写入的数据
        """
        pass

    @property
    @abstractmethod
    def supported_extensions(self) -> List[str]:
        """
        抽象属性：返回支持的文件扩展名列表
        :return: 扩展名列表
        """
        pass

    def validate_filepath(self, filepath: str) -> bool:
        """
        具体方法：验证文件路径是否支持
        抽象基类中可以包含具体实现的方法[8](@ref)
        """
        return any(filepath.endswith(ext) for ext in self.supported_extensions)


# JSON文件处理器实现类
class JsonFileHandler(FileHandler):
    """JSON文件处理器，实现抽象基类的接口[2](@ref)[3](@ref)"""

    def __init__(self, indent: int = 4, ensure_ascii: bool = False):
        """
        初始化JSON处理器
        :param indent: JSON格式化缩进空格数
        :param ensure_ascii: 是否确保ASCII编码
        """
        self.indent = indent
        self.ensure_ascii = ensure_ascii

    @property
    def supported_extensions(self) -> List[str]:
        """返回支持的JSON文件扩展名"""
        return ['.json', '.jsonl']

    def read(self, filepath: str) -> Any:
        """
        读取JSON文件内容
        :param filepath: JSON文件路径
        :return: 解析后的Python对象
        :raises FileNotFoundError: 文件不存在
        :raises json.JSONDecodeError: JSON格式错误
        """
        if not self.validate_filepath(filepath):
            raise ValueError(f"不支持的文件格式: {filepath}")

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"文件不存在: {filepath}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"JSON解析错误: {filepath}", e.doc, e.pos)

    def write(self, filepath: str, data: Any) -> None:
        """
        写入数据到JSON文件
        :param filepath: JSON文件路径
        :param data: 要写入的数据
        :raises OSError: 文件写入错误
        :raises TypeError: 数据不可JSON序列化
        """
        if not self.validate_filepath(filepath):
            raise ValueError(f"不支持的文件格式: {filepath}")

        try:
            # 创建目录（如果不存在）
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=self.indent, ensure_ascii=self.ensure_ascii)
        except (OSError, PermissionError) as e:
            raise OSError(f"文件写入失败: {filepath}") from e
        except TypeError as e:
            raise TypeError(f"无法序列化的对象: {type(data)}") from e

    def read_dataclass(self, filepath: str, dataclass_type: type) -> Any:
        """
        扩展方法：将JSON数据读取为数据类实例
        :param filepath: JSON文件路径
        :param dataclass_type: 数据类类型
        :return: 数据类实例
        """
        data_dict = self.read(filepath)
        return dataclass_type(**data_dict)

    def write_dataclass(self, filepath: str, dataclass_instance: Any) -> None:
        """
        扩展方法：将数据类实例写入JSON文件
        :param filepath: JSON文件路径
        :param dataclass_instance: 数据类实例
        """
        data_dict = asdict(dataclass_instance)
        self.write(filepath, data_dict)


# 工厂类用于创建文件处理器
class FileHandlerFactory:
    """文件处理器工厂类"""

    @staticmethod
    def create_handler(file_format: str) -> FileHandler:
        """
        根据文件格式创建对应的处理器
        :param file_format: 文件格式（如'json'）
        :return: 文件处理器实例
        """
        handlers = {
            'json': JsonFileHandler,
            # 可以扩展其他格式的处理器
            # 'csv': CsvFileHandler,
            # 'xml': XmlFileHandler,
        }

        if file_format not in handlers:
            raise ValueError(f"不支持的文件格式: {file_format}")

        return handlers[file_format]()


# 使用示例
def main():
    """主函数演示抽象基类的使用"""

    # 1. 创建JSON文件处理器
    handler = JsonFileHandler(indent=2)
    print(f"支持的扩展名: {handler.supported_extensions}")

    # 2. 创建用户数据
    user_data = UserData(
        username="张三",
        email="zhangsan@example.com",
        age=25,
        is_active=True
    )

    # 3. 写入JSON文件
    filepath = "data/users.json"
    try:
        handler.write_dataclass(filepath, user_data)
        print(f"数据已写入: {filepath}")
    except Exception as e:
        print(f"写入失败: {e}")
        return

    # 4. 读取JSON文件
    try:
        # 读取为字典
        data_dict = handler.read(filepath)
        print(f"读取的数据（字典）: {data_dict}")

        # 读取为数据类实例
        user_from_file = handler.read_dataclass(filepath, UserData)
        print(f"读取的数据（数据类）: {user_from_file}")
        print(f"用户名: {user_from_file.username}")
        print(f"邮箱: {user_from_file.email}")
        print(f"年龄: {user_from_file.age}")
        print(f"是否活跃: {user_from_file.is_active}")

    except FileNotFoundError as e:
        print(f"文件不存在: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
    except Exception as e:
        print(f"读取失败: {e}")

    # 5. 使用工厂模式创建处理器
    print("\n=== 使用工厂模式 ===")
    try:
        factory_handler = FileHandlerFactory.create_handler('json')
        print(f"工厂创建的处理器类型: {type(factory_handler).__name__}")

        # 验证抽象基类的接口契约
        if isinstance(factory_handler, FileHandler):
            print("处理器符合FileHandler接口契约")

        # 测试不支持的文件格式
        invalid_file = "data.txt"
        print(f"文件验证结果: {factory_handler.validate_filepath(invalid_file)}")

    except ValueError as e:
        print(f"工厂创建失败: {e}")

    # 6. 演示抽象基类的强制约束
    print("\n=== 抽象基类约束演示 ===")

    class IncompleteHandler(FileHandler):
        """不完整的处理器实现 - 缺少抽象方法"""

        def read(self, filepath: str) -> Any:
            return {"test": "data"}

        # 缺少write方法和supported_extensions属性

    try:
        # 尝试实例化不完整的处理器会抛出TypeError
        bad_handler = IncompleteHandler()
    except TypeError as e:
        print(f"抽象基类强制约束生效: {e}")


if __name__ == "__main__":
    main()
'''

# ==========================================================================================
# from new_task import *
# from threading import Thread
# from utils.wx_ocr import *
#
#
# wechat_OCR = WeChatOCR(wechat_dir, wechat_ocr_dir)
# wechat_OCR.init()
#
# def popup_process(device, mode_set, pop_mod, timeout: int = 30):
#     popup = AndroidPopup(device, wechat_OCR)
#     popup.popup_process(mode_set, pop_mod, timeout)
#
# install_pkg = r'E:\MTPClientConsole\MTPClientConsole_2.2.93.26585\out_alone\shell_apks\19368\4531910_20260105131715_test_il2cpp_2020117.shell.signed.apk'
# device = '18fdf3fd'
#
#
# install_proc = Thread(target=install_process, args=(device, install_pkg))
# popup_proc = Thread(target=popup_process, args=(device, None, 'install', 60))
#
#
#
# if __name__ == "__main__":
#     install_proc.start()
#     popup_proc.start()


# =============================================================================================
# def aaa(STR):
#     if len(STR.split()) == 1 and 65 <= ord(STR) <= 91:
#         keycode = ord(STR) - 36  # Android数字键码映射
#         print(keycode)
#     else:
#         return False
#
# aaa('a')

# =============================================================================================
# from utils.new_adb import *
# from utils.ui2_utils import *
#
# device = '5fa3254c'
# Android = ui2(device)
# android = AdbCLI(device)
# android.KEYCODE_ALL('T')
# android.KEYCODE_ALL('E')
# android.KEYCODE_ALL('N')
# android.KEYCODE_ALL('C')
# android.KEYCODE_ALL('E')
# android.KEYCODE_ALL('N')
# android.KEYCODE_ALL('T')
# android.KEYCODE_ALL(1)
# android.KEYCODE_ALL(2)
# android.KEYCODE_ALL(3)
# Android.click_word('安装')
# android.click_word_ocr('安装')

# text_lines = ['PerfDog(v11.1.2! ', '模拟器', '爱思导出文件', 'mrpcs tools', '4.9.27.7830', '19368', 'Downloads', 'MTPClientConsole', '此电脑', '3D 对急', 'Downloads', 'HTC U-3w', 'OPPO A5', 'OPPO A11', '视频', '口 图片', '自文档', '音乐', '名称', '修改日期', '本周早些时候(13)', ' cocos cdn full 3.3.3.xsx', ' normal tsdk 3.3.3xlsx', 'x unity cdn full 3.3.3,xlsx', '2025/12/31 17:01', '2025/12/31 17:01', '202512/31 17:00', 'x unity tsdk 3.3.3.xlsx', '2025/12/31 16:59', '生成中世纪大型风帆船图片.png', ' 洛杉矶非血帮、非病帮帮派种类、分布及', '2025/12/31 10:58', 'p 洛杉矶非裔帮派深度研究: 种类、分布与..', '2025/12/31 10:10', 's 01.xlsx', '202512/31 11:34', '2025/12/30 17:27', '生成卓尔精灵图(1).png', '2025/12/30 16:45', '牛成卓尔精灵图png', 'Po月 美国ALICE线深度研究报告.pdf', '火 抖音开发者工具-4.4.1.exe', 'Temp', '2025/12/30 16:45', '2025/12/30 16:22', '2025/12/29 17:23', '2025/12/30 14:27', '上周(2)', '目 com.tencent,stccfl (0.8.0)自动化兼容测...', '2025/12/25 16:41', 'com.vnggames.cfl.crossfirelegends _....', '202512/25 16:41', '上月(27)', '企业微信截图 17660431572602.png', '2025/12/18 17:10', '9819659.glog', 'Windows (C:)', '2025/12/12 15:58', '目TPTest(1.0)自动化兼容测试(OS)报告(1.', '2025/12/12 14:58', '系统 (D:)', 'e', 'o美国五大湖铁锈带深入研究报告.html', '2025/12/11 17:15', '软件(E:)', 'w美国五大湖铁锈带深入研究报告.docx', '202512/11 17:15', '文档(E)', 'AndroidManifest.xml', '2025/12/10 9:39', '新加卷 (G:)', ' tlog sdk(7.9.11.58649.32)自动化兼容.', '2025/12/9 11:18', '新加卷 (H)', '目ANO Tools(7.9.10.31093)自动化兼容测', '2025/12/8 18:01', '目tlog sdk(7.9.10.31093.64)自动化兼容.', '2025/12/8 18:01', 'CD 驱动 (l)', '目 tp2demo(1.0)自动化兼容测试Os)报告', '2025/12/8 18:00', '@ CD 动器 (:1', 'u', '72 个项目选中 1 个项目 311 KB', '类型', 'Microsoft Excel ...', 'Microsoft Excel ...', 'Microsoft Excel ...', 'Microsoft Excel ...', 'PNG 文件', 'Microsoft Edge ...', 'Microsoft Edge ...', 'Microsoft Excel ...', 'PNG 文件', 'PNG 文件', 'Microsoft Edge ...', '应用程序', '文件夹', 'Microsoft Excel ...', 'Microsoft Excel ...', 'PNG 文件', 'GLOG 文件', 'Microsoft Excel ...', 'Chrome HTML D...', 'Microsoft Word ...', 'XIML 文件', 'Microsoft Excel ...', 'Microsoft Excel ...', 'Microsoft Excel ...', 'Microsoft Excel ...', '24 KB', '23 KB', '24 KB', '23 KB', '5709 KB', '649 KB', '553 KB', '1,509 KB', '4449 KB', '3.482 KB', '477 KB', '259,260 KB', '23 KB', '23 KB', '32 KB', '21 KB', '22 KB', '26 KB', '60 KB', '8 KB', '113 KB', '113 KB', '112 KB', '22 KB']
# point = [(107.89, 14.12), (42.4, 14.41), (78.01, 14.41), (73.25, 14.11), (73.77, 13.57), (43.9, 14.89), (82.55, 14.35), (122.24, 13.55), (55.96, 12.72), (62.75, 14.41), (68.86, 13.36), (79.62, 23.66), (60.2, 14.41), (65.29, 13.57), (47.48, 16.96), (49.18, 16.96), (48.33, 19.5), (44.94, 16.96), (28.83, 14.41), (51.72, 14.41), (136.74, 18.63), (157.09, 15.84), (147.74, 15.38), (150.93, 12.72), (103.45, 13.57), (102.6, 13.57), (103.45, 13.57), (135.87, 15.28), (102.6, 13.57), (188.48, 15.61), (241.76, 17.07), (102.6, 13.57), (244.26, 15.29), (101.75, 13.57), (76.31, 13.57), (102.6, 13.57), (100.9, 13.57), (148.67, 17.29), (100.05, 11.87), (129.12, 14.66), (183.15, 11.02), (161.52, 19.75), (54.78, 14.18), (101.75, 11.87), (101.75, 13.57), (101.75, 13.57), (102.8, 15.86), (71.23, 16.96), (246.91, 16.98), (100.9, 11.87), (242.78, 19.0), (102.6, 13.57), (80.55, 15.26), (224.02, 17.27), (105.14, 13.57), (104.66, 16.61), (81.61, 15.62), (102.6, 13.57), (240.05, 14.06), (101.75, 13.57), (56.81, 16.11), (19.8, 14.12), (214.58, 12.64), (101.89, 14.95), (53.42, 14.41), (220.52, 15.31), (102.6, 12.72), (54.27, 15.26), (143.67, 17.71), (95.81, 11.87), (66.99, 14.41), (232.41, 16.21), (97.51, 13.57), (84.42, 17.86), (235.72, 13.57), (94.97, 13.57), (232.45, 16.07), (94.29, 14.96), (97.51, 16.11), (236.57, 15.26), (96.66, 14.41), (100.9, 13.57), (11.87, 5.94), (206.04, 14.41), (26.29, 14.41), (103.61, 13.37), (102.82, 13.96), (101.23, 14.82), (102.76, 13.46), (60.2, 13.57), (105.34, 13.91), (105.42, 14.33), (101.91, 12.93), (58.83, 15.15), (58.51, 14.41), (107.93, 14.19), (51.72, 13.57), (39.85, 14.41), (104.56, 14.0), (103.61, 13.02), (59.35, 14.41), (66.14, 13.57), (102.75, 13.34), (105.14, 11.87), (106.16, 13.7), (59.35, 14.41), (102.75, 13.16), (104.29, 13.57), (104.45, 15.35), (102.73, 12.9), (39.0, 14.41), (39.0, 15.26), (39.0, 14.41), (39.0, 14.41), (53.42, 14.41), (44.94, 14.41), (44.94, 14.41), (51.72, 13.57), (52.57, 11.87), (52.57, 12.72), (45.79, 13.57), (67.83, 13.57), (39.0, 14.41), (39.64, 16.47), (38.16, 14.41), (39.0, 14.41), (39.0, 14.41), (39.0, 14.41), (39.0, 14.41), (34.76, 14.41), (44.6, 16.15), (45.79, 16.11), (42.4, 14.41), (38.16, 14.41)]
# result_dict = {}
# for _ in range(len(text_lines)):
#     result_dict[text_lines[_]] = point[_]
# print(result_dict)

# import json
#
# def json_result(json_path):
#     with open(json_path, 'r', encoding='utf-8') as f:
#         results = json.loads(f.read())
#         if 'ocrResult' in results:
#             result_dict, point = {}, []
#             text_lines = [item['text'] for item in results['ocrResult']]
#             for item in results['ocrResult']:
#                 point.append((round(item['location']['right'] - item['location']['left'], 2),
#                               round(item['location']['bottom'] - item['location']['top'], 2)))
#             for _ in range(len(text_lines)):
#                 result_dict[text_lines[_]] = point[_]
#             # print(f"识别的文字: {text_lines}")
#             # print(f'识别的坐标: {point}')
#             # print(f'识别的对应坐标: {result_dict}')
#             return result_dict
#         else:
#             print("结果中没有 'ocrResult' 键，无法提取文字。")
#
#
# json_path = r'G:\Business_Area\shell\IOS_Shell\新建文件夹\企业微信截图_1767509245258.png.json'
# print(json_result(json_path))

# ==========================================================================================
# from utils.new_adb import *
#
#
# device = '5fa3254c'
# android = AdbCLI(device)
# android.click_word_ocr('兼容性', False)
# android.click_word_ocr('安装')

# =======================================================================================
# from utils.utils import *
#
# password = 'tencent123'
#
# for _ in password:
#     print(_)
#     print(str_word_is_int(_))

# =======================================================================================
# from utils.new_adb import *
# from utils.wx_ocr import *
# from setting import *
#
# device = '5fa3254c'
# android = AdbCLI(device)
# start = time.time()
# out = r'D:\code\python\All_project\adb_install_02\temp\screen'
# while time.time() <= start + 10:
#     name = f'test_{time.time()}'
#     android.screen(out, name)
#     weChat_ocr = WX_ocr(wechat_dir, wechat_ocr_dir)
#     weChat_ocr.ocr_pic(os.path.join(out, name+'.png'))

# while time.time() <= start + 5:
#     print(android.search_word_by_ocr('tlog_sdk'))
#     time.sleep(0.5)

# pop_list = ['com.android.packageinstaller', 'u0 android', 'com.coloros.safecenter']

# while time.time() < start + 10:
#     if android.popup_detection(pop_list):
#         print('当前界面存在弹窗，正在处理')
#         break
#     else:
#         android = AdbCLI(device)
#         print(android.get_focus())

# ========================================================================================
# from new_task import *
#
# device = '5fa3254c'
# androidPopup = AndroidPopup(device)
#
# print(androidPopup._execute_click('应用权限', 'ui2'))

# ========================================================================================
# from setting import *
# from datetime import datetime
# from typing import Dict, List, Optional, Tuple, Union
# from functools import lru_cache
# import os
# import json
# import time
# import re
# import subprocess
# from PIL import Image
# from typing import List, Dict, Union, Optional
# from pathlib import Path
# from wechat_ocr.ocr_manager import OcrManager, OCR_MAX_TASK_ID

'''
def write_log(log_name, comm, res):
    file = open(rf'{log_path}\{log_name}.log', 'a', encoding='utf-8')
    file.write(time.strftime('%H:%M:%S') + '\ncomm:\n' + str(comm) + '\nresult:\n' + res + '=' * 80 + '\n\n')
    file.close()

def cmd_single_run(comm, decode_type='gbk'):
    # 只有一条执行的cmd指令
    obj = subprocess.Popen(comm, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    info, error = obj.communicate()
    try:
        err = error.decode(decode_type)
        result = info.decode(decode_type)
    except:
        try:
            err = error.decode('utf-8')
            result = info.decode('utf-8')
        except:
            err = error.decode('cp936')
            result = info.decode('cp936')
    write_log(time_YMD, comm, result)
    if err != '':
        write_log(time_YMD + '_err', comm, err)
    return result

def absolute_coordinate(img_path: str, pixel_point):
    img = Image.open(img_path)
    width, height = img.size
    ac_x, ac_y, = round(pixel_point[0] / width, 2), round(pixel_point[1] / height, 2)
    return (ac_x, ac_y)

def crop_img(img_path: str, coordinate: tuple, save_path: str = None):
    im = Image.open(img_path)
    img2 = im.crop(coordinate)
    if save_path == None:
        name = os.path.join(os.path.dirname(img_path), str(time.time())+'.png')
    else:
        name = save_path
    img2.save(name)

class AdbCLI:
    """ADB命令行工具类（优化版）"""

    # 命令模板字典，减少字符串拼接
    COMMAND_TEMPLATES = {
        'shell': '{adb_exe} -s {device} shell {command}',
        'push': '{adb_exe} -s {device} push {src} {dst}',
        'pull': '{adb_exe} -s {device} pull {src} {dst}',
        'uninstall': '{adb_exe} -s {device} uninstall {pkg_name}',
        'screencap': '{adb_exe} -s {device} shell screencap -p {path}',
        'am_start': '{adb_exe} -s {device} shell am start {activity}',
        'am_stop': '{adb_exe} -s {device} shell am force-stop {pkg}',
        'pm_list': '{adb_exe} -s {device} shell pm list package {pkg_name}',
        'ps_grep': '{adb_exe} -s {device} shell ps | grep {pkg_name}',
        'getprop': '{adb_exe} -s {device} shell getprop {prop_name}',
        'wm_size': '{adb_exe} -s {device} shell wm size',
        'dumpsys_window': '{adb_exe} -s {device} shell dumpsys window | grep mCurrentFocus',
        'dumpsys_input': '{adb_exe} -s {device} shell dumpsys input | grep SurfaceOrientation',
        'dumpsys_package': '{adb_exe} -s {device} shell dumpsys package {pkg_name} | grep -A 1 android.intent.action.MAIN:',
        'get_focus': '{adb_shell} "dumpsys window | grep mCurrentFocus"',
        'get_process': '{adb_shell} "ps | grep {pkg_name}"',
        'get_log_low': '{adb_shell} "cat /sdcard/sdk/log.log"',
        'get_log_high': '{adb_shell} "cat /sdcard/Android/data/{pkg_name}/files/log.log"',
        'get_shell_log_low': '{adb_shell} "cat /sdcard/sdk/shell.log | grep OpenID"',
        'get_shell_log_high': '{adb_shell} "cat /sdcard/Android/data/{pkg_name}/files/shell.log | grep OpenID"',
        'pull_log_low': '{adb_exe} -s {device} pull /sdcard/sdk/log.log {out_path}',
        'pull_log_high': '{adb_exe} -s {device} pull /sdcard/Android/data/{pkg_name}/files/log.log {out_path}',
        'input_tap': '{adb_shell} input tap {x} {y}',
        'input_swipe': '{adb_shell} input swipe {x1} {y1} {x2} {y2} {duration}',
        'keyevent': '{adb_shell} input keyevent {keycode}',
        'grant_permission': '{adb_shell} pm grant {pkg_name} {permission}',
        'screenshot': '{adb_shell} screencap -p {path}',
        'pull_screenshot': '{adb_exe} -s {device} pull "{remote_path}" "{local_path}"',
        'remove_file': '{adb_shell} rm -rf "{remote_path}"'
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

    def __init__(self, device: str, tools_path: str = tools_path):
        """初始化ADB命令行工具

        Args:
            device: 设备序列号
            tools_path: ADB工具路径
        """
        self.device = device
        self.tools_path = Path(tools_path)
        self.adb_exe = str(self.tools_path / 'adb.exe')
        self.adb_shell = f'{self.adb_exe} -s {self.device} shell '
        self.wx_OCR = WeChatOCR


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

    def click_word_ocr(self, text: str, accurate_match: bool = True) -> bool:
        """通过OCR识别文本并点击"""
        name = f'click_{int(time.time())}'
        screenshot_success = self.screen(str(self._screen_path), name)

        if not screenshot_success:
            return False

        img_path = self._screen_path / f'{name}.png'

        permit = self.wx_OCR.match_text(text, str(img_path), accurate_match)['point']

        # 执行点击
        return self.click(permit)



class WeChatOCR:
    """
    微信OCR封装类，提供类似PaddleOCR的调用接口
    基于wechat-ocr库，调用微信本地OCR引擎进行文字识别
    """

    def __init__(self,
                 wechat_dir: str = None,
                 wechat_ocr_dir: str = None):
        """
        初始化WeChatOCR实例

        Args:
            wechat_dir: 微信安装目录路径，包含mmmojo.dll文件
            wechat_ocr_dir: WeChatOCR.exe程序路径
            auto_find_paths: 是否自动查找路径（当未提供路径时）
        """
        self.wechat_dir = wechat_dir
        self.wechat_ocr_dir = wechat_ocr_dir
        self.ocr_manager = None
        self.results_cache = {}  # 缓存识别结果
        self.callback_results = {}  # 回调函数收集的结果


        if not self.wechat_dir or not self.wechat_ocr_dir:
            raise FileNotFoundError("无法找到微信OCR相关路径，请手动指定路径")


    def _ocr_result_callback(self, img_path: str, results: dict):
        """
        OCR结果回调函数，用于收集识别结果[1](@ref)[4](@ref)
        """
        self.callback_results[img_path] = results

        # 提取文本内容
        if 'ocrResult' in results:
            text_lines = [item['text'] for item in results['ocrResult']]
            # print(f"图片 {os.path.basename(img_path)} 识别完成，共识别到 {len(text_lines)} 行文本")

    def init(self) -> bool:
        """
        初始化OCR引擎，类似PaddleOCR的初始化方式
        Returns:
            bool: 初始化是否成功
        """
        try:
            self.ocr_manager = OcrManager(self.wechat_dir)
            self.ocr_manager.SetExePath(self.wechat_ocr_dir)
            self.ocr_manager.SetUsrLibDir(self.wechat_dir)
            self.ocr_manager.SetOcrResultCallback(self._ocr_result_callback)
            self.ocr_manager.StartWeChatOCR()
            print("微信OCR引擎初始化成功")
            return True
        except Exception as e:
            print(f"OCR引擎初始化失败: {e}")
            return False


    def ocr(self,
            img_path: Union[str, List[str]],
            return_json: bool = False) -> Union[List[Dict], str]:
        """
        识别单张或多张图片，类似PaddleOCR的ocr方法

        Args:
            img_path: 图片路径或图片路径列表
            return_json: 是否返回原始JSON格式

        Returns:
            识别结果列表或JSON字符串
        """
        if self.ocr_manager is None:
            raise RuntimeError("请先调用init()方法初始化OCR引擎")

        # 清空之前的结果缓存
        self.callback_results.clear()

        # 处理单张或多张图片
        if isinstance(img_path, str):
            img_paths = [img_path]
        else:
            img_paths = img_path

        # 提交OCR任务[1](@ref)[6](@ref)
        for path in img_paths:
            if not os.path.exists(path):
                print(f"警告: 图片路径不存在: {path}")
                continue
            self.ocr_manager.DoOCRTask(path)

        # 等待所有任务完成[1](@ref)[4](@ref)
        time.sleep(1)
        while self.ocr_manager.m_task_id.qsize() != OCR_MAX_TASK_ID:
            time.sleep(0.1)

        # start_time = time.time()
        # timeout = 10  # 10秒超时
        #
        # while self.ocr_manager.m_task_id.qsize() != OCR_MAX_TASK_ID:
        #     time.sleep(0.1)
        #     if time.time() - start_time > timeout:
        #         print("OCR任务超时，可能某些任务未完成")
        #         break  # 添加超时退出

        # 收集结果
        all_results = []
        for path in img_paths:
            if path in self.callback_results:
                result = self.callback_results[path]
                if return_json:
                    all_results.append(result)
                else:
                    # 转换为类似PaddleOCR的格式
                    formatted_result = self._format_result(result)
                    all_results.append(formatted_result)
            else:
                all_results.append([] if not return_json else {})

        return all_results if len(img_paths) > 1 else all_results

    def _format_result(self, result: dict) -> List[Dict]:
        """
        将微信OCR结果格式化为类似PaddleOCR的格式[3](@ref)

        Returns:
            List[Dict]: 每个元素包含文本和位置信息
        """
        formatted = []
        if 'ocrResult' not in result:
            return formatted

        for item in result['ocrResult']:
            # 提取文本
            text = item.get('text', '')

            # 提取位置信息（微信OCR返回的是矩形坐标）
            location = item.get('location', {})
            if location:
                # 转换为四角坐标格式
                left = location.get('left', 0)
                top = location.get('top', 0)
                width = location.get('width', 0)
                height = location.get('height', 0)


            # 置信度
            confidence = item.get('confidence', 0.0)

            formatted.append({
                'text': text,
                'confidence': confidence,
                'location': location  # 保留原始位置信息
            })

        return formatted

    def ocr_single(self, img_path: str, detail: bool = True) -> Union[str, List[Dict]]:
        """
        识别单张图片，返回文本或详细信息

        Args:
            img_path: 图片路径
            detail: 是否返回详细信息

        Returns:
            str或List[Dict]: 识别结果
        """
        result = self.ocr(img_path, return_json=False)

        if detail:
            return result
        else:
            # 只返回文本内容
            texts = [item['text'] for item in result]
            return '\n'.join(texts)

    def batch_ocr(self,
                  img_dir: str,
                  extensions: List[str] = None) -> Dict[str, Dict]:
        """
        批量识别目录下的所有图片[5](@ref)

        Args:
            img_dir: 图片目录路径
            extensions: 支持的图片扩展名列表

        Returns:
            Dict[str, List[Dict]]: 文件名到识别结果的映射
        """
        if extensions is None:
            extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']

        # 收集所有图片文件
        img_files = []
        for ext in extensions:
            img_files.extend(list(Path(img_dir).glob(f'*{ext}')))
            img_files.extend(list(Path(img_dir).glob(f'*{ext.upper()}')))

        if not img_files:
            print(f"在目录 {img_dir} 中未找到支持的图片文件")
            return {}

        print(f"找到 {len(img_files)} 张图片，开始批量识别...")

        # 批量识别
        img_paths = [str(file) for file in img_files]
        results = self.ocr(img_paths, return_json=False)

        # 构建结果字典
        result_dict = {}
        for file, result in zip(img_files, results):
            result_dict[file.name] = result

        return result_dict

    def save_results(self,
                     results: Union[List[Dict], Dict],
                     output_dir: str = './ocr_results'):
        """
        保存OCR识别结果到文件[1](@ref)

        Args:
            results: 识别结果
            output_dir: 输出目录
        """
        os.makedirs(output_dir, exist_ok=True)

        if isinstance(results, dict):
            # 批量结果
            for filename, result in results.items():
                if result:  # 非空结果
                    # 保存为JSON
                    json_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.json")
                    with open(json_file, 'w', encoding='utf-8') as f:
                        json.dump(result, f, ensure_ascii=False, indent=2)

                    # 保存为文本
                    txt_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
                    with open(txt_file, 'w', encoding='utf-8') as f:
                        for item in result:
                            f.write(f"{item['text']}\n")
        else:
            # 单张图片结果
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            json_file = os.path.join(output_dir, f"result_{timestamp}.json")
            txt_file = os.path.join(output_dir, f"result_{timestamp}.txt")

            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)

            with open(txt_file, 'w', encoding='utf-8') as f:
                for item in results:
                    f.write(f"{item['text']}\n")

        print(f"结果已保存到目录: {output_dir}")

    def release(self):
        """释放资源，关闭OCR引擎[1](@ref)[6](@ref)"""
        if self.ocr_manager:
            self.ocr_manager.KillWeChatOCR()
            print("微信OCR引擎已关闭")

    def __enter__(self):
        """上下文管理器入口"""
        self.init()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.release()

    def get_version_info(self) -> Dict:
        """获取版本信息"""
        return {
            "wechat_dir": self.wechat_dir,
            "wechat_ocr_dir": self.wechat_ocr_dir,
            "library": "wechat-ocr",
            "description": "微信本地OCR引擎封装"
        }

    def box_center_point(self, ocr_results) -> dict:
        # results = self.ocr(img_path)[0]
        res = {}
        for result in ocr_results:
            con_point = result['location']
            res[result['text']] = (round((float(con_point['left'])+float(con_point['right']))/2, 2),
                                   round((float(con_point['top'])+float(con_point['bottom']))/2, 2))
        return res

    def box_center_crop(self, img_path, ocr_results):
        # results = self.ocr(img_path)[0]
        for result in ocr_results:
            con_point = result['location']
            point = (con_point['left'], con_point['top'], con_point['right'], con_point['bottom'])
            crop_img(img_path, point)

    def match_text(self, img_path: str, text: str, accurate_match: bool=True) -> dict:
        results = self.ocr(img_path)[0]
        # print(results)
        # self.box_center_crop(img_path, results)
        box_point = self.box_center_point(results)
        for Key in box_point.keys():
            pixel_point = box_point[Key]
            # print(pixel_point)
            if accurate_match == True and text == Key:
                return {
                    'match_res': True,
                    'sample': text,
                    'obj_match': Key,
                    'point': absolute_coordinate(img_path, pixel_point)
                }
            elif accurate_match == False and re.search(text, Key):
                return {
                    'match_res': True,
                    'sample': text,
                    'obj_match': Key,
                    'point': absolute_coordinate(img_path, pixel_point)
                }
            else:
                continue
        return {
                'match_res': False,
                'sample': text,
                'obj_match': None,
                'point': (0, 0)
            }

'''


#  =====================================================================================
# from utils.POW_handing import *
# from utils.adb_utils import *
# from threading import Thread
# from utils.wx_ocr import *
# from utils.utils import *
# from setting import *
#
# wechat_OCR = WeChatOCR(wechat_dir, wechat_ocr_dir)
# wechat_OCR.init()
#
#
# def install_process(device, pkg, ocr_server):
#     """安装过程处理"""
#     android = AdbCLI(device, ocr_server)
#     print(f"安装包: {pkg}")
#     pkg_name = ''
#
#     file_ext = os.path.splitext(pkg)[1].lower()
#     if file_ext == '.apk':
#         pkg_name = get_pkg_name(pkg)
#     elif file_ext == '.aab':
#         pkg_name = get_aab_name(pkg)
#     else:
#         print(f'不支持的文件类型: {file_ext}', flush=True)
#
#     start = time.time()
#     android.reinstall_pkg(pkg)
#     end = time.time()
#     if android.pkg_exists(pkg_name):
#         print('安装成功')
#     else:
#         print('安装失败')
#     install_time = round(end - start)
#     print(f'耗时: {install_time}s')
#     android.KEYCODE_ALL('HOME')
#
# def popup_process(device, mode_set, pop_mod, timeout: int = 30):
#     popup = AndroidPopup(device, wechat_OCR)
#     popup.popup_process(mode_set, pop_mod, timeout)
#
# install_pkg = r'E:\MTPClientConsole\MTPClientConsole_2.2.93.26585\out_alone\shell_apks\19368\4531910_20260105131715_test_il2cpp_2020117.shell.signed.apk'
# device = '9e2bd91c'
#
#
# install_proc = Thread(target=install_process, args=(device, install_pkg, wechat_OCR))
# popup_proc = Thread(target=popup_process, args=(device, None, 'install', 60))
#
#
# if __name__ == "__main__":
#     install_proc.start()
#     popup_proc.start()


#  =====================================================================================
# from setting import *
# from utils.wx_ocr import *
# from utils.new_adb import *
#
#
# wechat_OCR = WeChatOCR(wechat_dir, wechat_ocr_dir)
# wechat_OCR.init()
# device = '18fdf3fd'
# android = AdbCLI(device)
# print(android.click_word_ocr(wechat_OCR, '安装'))


#
# device = '9e2bd91c'
# android = AdbCLI(device)
# start = time.time()
# out = r'D:\code\python\All_project\adb_install_02\temp\screen'
#
# name = f'test_{time.time()}'
# android.screen(out, name)
#
#
# android.click_word_ocr(wechat_OCR, '浏览器', False)

# print(wechat_OCR.match_text(os.path.join(out, name+'.png'), '浏览器'))
# android.click_word_ocr('应用商店')

# print(results[0])
# print(results[0][2]['text'])

# while time.time() <= start + 10:
#     name = f'test_{time.time()}'
#     android.screen(out, name)
#     results = wechat_OCR.ocr_single(os.path.join(out, name+'.png'))
#     print(results)

# results = wechat_OCR.batch_ocr(r'D:\code\python\All_project\adb_install_02\temp\screen')
# print(results)

# ===============================================================================
# import yaml
# from typing import List, Dict, Any, Optional, Union
# from setting import *
#
# def read_yaml(yaml_path):
#     with open(yaml_path, 'r', encoding='utf-8') as f:
#         data = yaml.load(stream=f, Loader=yaml.FullLoader)
#     return data
#
#
# def popup_data() -> Dict[str, Any]:
#     """读取弹窗配置数据（优化版）"""
#     y_data = read_yaml(popup_config_path)
#
#     # 使用字典推导式简化代码[5](@ref)
#     popup_special = {}
#     for item in y_data['special_handling']:
#         print(type(item))
#         for device, value in item.items():
#             popup_special[device] = value
#
#     return {
#         'click_traversal_popup': y_data['click_traversal_popup'],
#         'popup_pkgname': y_data['popup_pkgname'],
#         'popup_special': popup_special
#     }
#
# print(popup_data())

# ===============================================================================================
# from utils.utils import *
# from setting import *
#
#
# def popup_data() -> dict:
#     """读取弹窗配置数据（优化版）"""
#     y_data = read_yaml(popup_config_path)
#
#     # 使用字典推导式简化代码[5](@ref)
#     popup_special = {}
#     for item in y_data['special_handling']:
#         for device, value in item.items():
#             popup_special[device] = value
#
#     return {
#         'click_traversal_popup': y_data['click_traversal_popup'],
#         'popup_pkgname': y_data['popup_pkgname'],
#         'popup_special': popup_special
#     }
#
# def popup_process(mode_set = None, pop_mod='normal', timeout: int = 30):
#     """
#     弹窗处理（优化版）
#     使用字典映射替代多个if判断[6](@ref)
#     pop_mod=['normal', 'install', 'permission']
#     """
#     popup_dict = {'install': 'install_pkgname', 'permission': 'system_pkgname'}
#     start_time = time.time()
#     popup_data_ = popup_data()
#
#     click_traversal_popup = popup_data_['click_traversal_popup']
#     if pop_mod == 'normal':
#         popup_pkgname_list = []
#         for pkgname in popup_data_['popup_pkgname'].keys():
#             print(pkgname)
#             for pkg in popup_data_['popup_pkgname'][pkgname]:
#                 popup_pkgname_list.append(pkg)
#     else:
#         if pop_mod == 'install' or 'permission':
#             popup_pkgname_list = popup_data_['popup_pkgname'][popup_dict[pop_mod]]
#         else:
#             return False
#
#     return popup_pkgname_list
#
# print(popup_process(pop_mod='permission'))

# =============================================================================================
# from utils.adb_utils import *
# from utils.wx_ocr import *
# from setting import *
#
# device = 'dfc5f4ee'
# pkg = r'G:\Business_Area\shell\need_shell\Android\app_so_buluodi1.apk'
# wechat_OCR = WeChatOCR(wechat_dir, wechat_ocr_dir)
# android = AdbCLI(device, wechat_OCR)
# wechat_OCR.init()
# print(android.reinstall_pkg(pkg))

# =================================================================================================
# from task import *
# from gui import *
# from device import Android_dev as Android
#
#
# wechat_ocr = WeChatOCR(wechat_dir, wechat_ocr_dir)
# wechat_ocr.init()
#
#
# def main(OS, device, pkg_path, Time, clean, enable, run):
#     Task = run_task(device, pkg_path, wechat_ocr)
#     pkgs_list = check_endswith(pkg_path)
#     if OS == 'android':
#         print(device, flush=True)
#         an_dev = Android.Android_device(device)
#     else:
#         MPE_name = device
#         usb = mobile_phone_emulator.get(MPE_name)
#         print(usb, flush=True)
#         adb_connect(usb)
#         an_dev = Android.Android_device(usb)
#
#     Run = 'run'
#     if run == '否':
#         Run = False
#
#     Task.pkg_run(enable, Run, Time)
#     if clean == '是':
#         for a in pkgs_list['apk']+pkgs_list['aab']:
#             pkg_name = get_pkg_name(a)
#             an_dev.uninstall_pkg(pkg_name)
#         print('Android 测试应用已删除', flush=True)
#
#
# if __name__ == "__main__":
#     Init = gui_init()
#     OS, device, pkg_path, Time, clean, enable, run = \
#         Init['OS'], Init['Devices'], Init['Path'], float(Init['Time']), Init['Clean'], Init['Enable'], Init['Run']
#     # device = '127.0.0.1:5555'
#     # pkg_path = r'G:\Business_Area\sdk\7.9.X\7.9.22.10274\tptest'
#     main('android', device, pkg_path, Time, '是', 'sdk', 'none')

# ======================================================================================
# from utils.adb_utils import *
# from utils.wx_ocr import *
# from setting import *
#
# we_ocr = WeChatOCR(wechat_dir, wechat_ocr_dir)
# we_ocr.init()
#
# device = '709ccd85'
# Android = AdbCLI(device, we_ocr)
#
# for _ in range(6):
#     Android.KEYCODE_ALL(0)
# Android.KEYCODE_BUTTON('ENTER')

# =========================================================================================
# from utils.utils import *
# from utils.adb_utils import *
# from utils.wx_ocr import *
# from setting import *
#
#
# we_ocr = WeChatOCR(wechat_dir, wechat_ocr_dir)
# we_ocr.init()
#
# device = '9e2bd91c'
# Android = AdbCLI(device, we_ocr)
#
# password = {
#     'aa': 'qwer1234qwer1234',
#     'kk': '124zmckdp'
# }
#
# for i in text_split_2_ascii(password['kk']):
#     Android.KEYCODE_ALL(i)

# ==============================================================================================
import re



