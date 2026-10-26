from task import *
from gui import *
from utils.adb_utils import *
from utils.wx_ocr import *


wechat_ocr = WeChatOCR(wechat_dir, wechat_ocr_dir)
wechat_ocr.init()


def main(OS, device, pkg_path, Time, clean, enable, run):
    if OS != 'android':
        device = mobile_phone_emulator[device]
        adb_connect(device)
    Task = run_task(device, pkg_path, wechat_ocr)
    pkgs_list = check_endswith(pkg_path)
    Android = AdbCLI(device, wechat_ocr)
    Android.set_off_time()

    Run = 'run'
    if run == '否':
        Run = False

    Task.pkg_run(enable, Run, Time)
    if clean == '是':
        for a in pkgs_list['apk']+pkgs_list['aab']:
            pkg_name = get_pkg_name(a)
            Android.uninstall_pkg(pkg_name)
        print('Android 测试应用已删除', flush=True)


if __name__ == "__main__":
    Init = gui_init()
    OS, device, pkg_path, Time, clean, enable, run = \
        Init['OS'], Init['Devices'], Init['Path'], float(Init['Time']), Init['Clean'], Init['Enable'], Init['Run']
    main(OS, device, pkg_path, Time, Init['Clean'], Init['Enable'], Init['Run'])
