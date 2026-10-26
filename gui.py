from gooey import Gooey, GooeyParser
from setting import *
import subprocess
import time
from utils.utils import *

# time_YMD = time.strftime('%Y-%m-%d')
#
# def cmd_single_run(comm, decode_type='gbk'):
#     '''只有一条执行的cmd指令'''
#     obj = subprocess.Popen(comm, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     info, error = obj.communicate()
#     try:
#         err = error.decode(decode_type)
#         result = info.decode(decode_type)
#     except:
#         try:
#             err = error.decode('utf-8')
#             result = info.decode('utf-8')
#         except:
#             err = error.decode('cp936')
#             result = info.decode('cp936')
#     write_log(time_YMD, comm, result)
#     if err != '':
#         write_log(time_YMD + '_err', comm, err)
#     return result
#
# def write_log(log_name, comm, res):
#     file = open(rf'{log_path}\{log_name}.log', 'a', encoding='utf-8')
#     file.write(time.strftime('%H:%M:%S') + '\ncomm:\n' + str(comm) + '\nresult:\n' + res + '=' * 80 + '\n\n')
#     file.close()
#
# def devices():
#     comm = f'{tools_path}\\adb.exe devices'
#     check = cmd_single_run(comm, 'gbk').split('\r\n')
#     if len(check) == 3:
#         return 'no device'
#     elif len(check) < 3:
#         check = cmd_single_run(comm, 'gbk').split('\r\n')
#     try:
#         check.pop(-1)
#         check.pop(-1)
#         check.pop(0)
#         return check
#     except:
#         return 'no device'

def android_dev_info():
    android_devices = []
    Devices = devices()
    for i in range(3):
        if Devices == 'no device':
            Devices = devices()
            if Devices == 'no device':
                continue
            else:
                break
    for device in Devices:
        android_devices.append(device.split('\t'))
    return android_devices

@Gooey(program_name="兼容自动化（apk/aab/ipa）", language="chinese", default_size=(800, 600))
def gui_init():
    Android_devices = android_dev_info()
    # IOS_devices = ios_dev_info()
    MPE_devices = mobile_phone_emulator
    # a_d, i_d, M_d = [], [], []
    a_d, M_d = [], []
    if Android_devices != 'no device':
        for msg in Android_devices:
            if msg[1] != 'device':
                a_d.append(msg[0] + ' ' + 'disconnect')
            else:
                a_d.append(msg[0])
    else:
        a_d = ['no devices']
    # if IOS_devices != 'no ios device':
    #     for msg in IOS_devices:
    #         i_d.append(f'Name: {msg[1]}  Ver: {msg[2]}')
    # else:
    #     i_d = ['no devices']
    for MPE_dev in MPE_devices.keys():
        M_d.append(MPE_dev)

    min = ['1', '2', '3', '5', '10', '15', '30']
    parser = GooeyParser(description='请选择配置')
    machine = parser.add_subparsers(dest='result')
    android = machine.add_parser('android')
    android.add_argument('devices', widget='Dropdown', metavar='设备', choices=a_d, default=a_d[0])
    android.add_argument('time', widget='Dropdown', metavar='运行时间（分钟）', choices=min, default='3')
    android.add_argument('path', widget="DirChooser", metavar='安装包或文件夹')
    android.add_argument('enable', widget="Dropdown", metavar='enable类型', choices=['sdk', 'shell', 'all_1', 'perf_68'],
                         default='sdk', help='all_1: 全为1，perf_68: 性能enable')
    android.add_argument('run', widget='Dropdown', metavar='安装后运行', choices=['是', '否'], default='是')
    android.add_argument('clean', widget='Dropdown', metavar='是否卸载已验证安装包', choices=['是', '否'], default='否')
    # android.add_argument('run_pkg', widget='Dropdown', metavar='运行对象', choices=['apk+aab', 'apk', 'aab'],
    #                      default='apk+aab')

    # ios = machine.add_parser('ios')
    # ios.add_argument('devices', widget='Dropdown', metavar='设备', choices=i_d, default=i_d[0])
    # ios.add_argument('time', widget='Dropdown', metavar='运行时间', choices=min, default='3')
    # ios.add_argument('enable', widget='Dropdown', metavar='enable类型', choices=['sdk', 'shell'], default='sdk')
    # ios.add_argument('path', widget="DirChooser", metavar='安装包文件夹')
    # ios.add_argument('clean', widget='Dropdown', metavar='是否卸载已验证安装包', choices=['是', '否'], default='否')

    MPE = machine.add_parser('安卓模拟器')
    MPE.add_argument('devices', widget='Dropdown', metavar='设备', choices=M_d, default=M_d[0])
    MPE.add_argument('time', widget='Dropdown', metavar='运行时间', choices=min, default='3')
    MPE.add_argument('path', widget="DirChooser", metavar='安装包文件夹')
    MPE.add_argument('enable', widget="Dropdown", metavar='enable类型', choices=['sdk', 'shell', 'all_1', 'perf_68'],
                     default='sdk')
    MPE.add_argument('run', widget='Dropdown', metavar='安装后运行', choices=['是', '否'], default='是')
    MPE.add_argument('clean', widget='Dropdown', metavar='是否卸载已验证安装包', choices=['是', '否'], default='否')
    # MPE.add_argument('run_pkg', widget='Dropdown', metavar='运行对象', choices=['apk+aab', 'apk', 'aab'],
    #                  default='apk+aab')

    args = parser.parse_args()
    if args.result == 'android':
        OS = 'android'
    # elif args.result == 'ios':
    #     OS = 'ios'
    else:
        OS = 'MPE'
    res = {
        'OS': OS,
        'Devices': args.devices,
        'Path': args.path,
        'Time': args.time,
        'Clean': args.clean,
        'Enable': args.enable,
        # 'Run_pkg': args.run_pkg,
        'Run': args.run,
    }
    return res
