from utils.ui2_utils import *
from utils.adb_utils import *
from utils.POW_handing import *
from utils.utils import *
from setting import *
from threading import Thread


size_2_time = {
    '50': 30,
    '100': 45,
    '200': 60,
    '512': 120,
    '1024': 300,
    '2048': 600,
    '5120': 900,
    '10240': 1200
}

ver_2_time = {
    '4': 3, '5': 3, '6': 3, '7': 3, '8': 2, '9': 2, '10': 1.5, '11': 1.5, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1
}

class run_task:
    def __init__(self, device, pkg_path, wechat_OCR):
        self.device = device
        self.pkg_path = pkg_path
        self.wechat_OCR = wechat_OCR
        self.adb_server = AdbCLI(self.device, self.wechat_OCR)
        self.ui2_server = ui2(self.device)
        self.popup_handing = AndroidPopup(self.device, self.wechat_OCR)


    def pkg_run(self, enable_mode: str='sdk', mode_set: str or bool='run', run_time: float=3.0):
        pkg_list = android_pkgs_list(self.pkg_path)
        for pkg in pkg_list:
            install_time = self.install_time(pkg)
            # print(install_time)
            install_proc = Thread(target=self.install_process, args=(pkg, self.wechat_OCR))
            popup_proc_install = Thread(target=self.popup_process, args=(None, 'install', install_time) )
            popup_proc = Thread(target=self.popup_process, args=('normal', 'normal', 10))
            install_proc.start()
            popup_proc_install.start()
            install_proc.join()

            if mode_set != 'run':
                continue
            pkg_name = get_pkg_name(pkg)
            if not self.adb_server.pkg_exists(pkg_name):
                print(f'未找到包名 {pkg_name}，暂时跳过\n')
                continue
            self.adb_server.set_enable(pkg_name, enable_mode)
            self.adb_server.start_app(pkg_name)
            start_time = time.time()
            time.sleep(3)
            popup_proc.start()
            # popup_proc.join()
            restart_time = 1
            half_time = round((start_time + (run_time * 60)/2), 2)
            self.adb_server.check_app(pkg_name)
            self.adb_server.screen(screen_path, self.device+'_'+pkg_name+'_start_'+str(round((time.time()))))
            time.sleep(5)
            while time.time() < start_time + run_time * 60:
                if not pkg_name in self.adb_server.get_focus():
                    self.adb_server.check_app(pkg_name)
                    print(f'{pkg_name}启动{str(round(time.time()-start_time))}秒不在前台，尝试重启{str(restart_time)}次')
                    self.adb_server.stop_app(pkg_name)
                    time.sleep(0.5)
                    self.adb_server.start_app(pkg_name)
                    time.sleep(1)
                    restart_time += 1
                if restart_time > 3:
                    print('尝试重启3次失败')
                    break
                if round(time.time(), 2) == half_time:
                    self.adb_server.check_app(pkg_name)
            self.adb_server.check_app(pkg_name)
            self.adb_server.screen(screen_path, self.device+'_'+pkg_name+'_end_'+str(round((time.time()))))
            self.adb_server.stop_app(pkg_name)
            # print('popup: ' + str(install_proc.is_alive()))
            # print('popup: ' + str(popup_proc_install.is_alive()))
            # print('popup: ' + str(popup_proc.is_alive()))


    def install_process(self, pkg, ocr_server):
        """安装过程处理"""
        android = AdbCLI(self.device, ocr_server)
        print(f"安装包: {pkg}")
        pkg_name = ''
        if get_pkg_name(pkg):
            pkg_name = get_pkg_name(pkg)
        else:
            print(f'不支持的文件类型: {pkg}', flush=True)

        start = time.time()
        android.reinstall_pkg(pkg)
        end = time.time()
        if android.pkg_exists(pkg_name):
            print('安装成功')
        else:
            print('安装失败')
        install_time = round(end - start)
        print(f'耗时: {install_time}s')
        android.KEYCODE_ALL('HOME')

    def popup_process(self, mode_set, pop_mod, timeout: int = 30):
        popup = AndroidPopup(self.device, self.wechat_OCR)
        popup.popup_process(mode_set, pop_mod, timeout)

    def install_time(self, pkg):
        pkg_size = get_size(pkg)/1024/1024
        dev_ver = self.adb_server.ver()
        for s in size_2_time.keys():
            if int(s) > int(pkg_size):
                install_time = size_2_time[s]
                return install_time * ver_2_time[str(dev_ver)]
        return 1500


# from utils.wx_ocr import *
# if __name__ == "__main__":
#     device = "9e2bd91c"
#     pkg = r'G:\Business_Area\sdk\7.9.X\7.9.24.60446\demo'
#     wechat_ocr = WeChatOCR(wechat_dir, wechat_ocr_dir)
#     wechat_ocr.init()
#     task = run_task(device, pkg, wechat_ocr)
#     task.pkg_run('sdk', 'None', 0.5)
