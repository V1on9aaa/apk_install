import os
import time

tools_path = os.path.abspath('Tools')
log_path = os.path.abspath(r'temp\log')
screen_path = os.path.abspath(r'temp\screen')
config_path = os.path.abspath(r'Tools\config')
unzip_path = os.path.abspath(r'temp\aab_splits')
popup_config_path = os.path.join(config_path, 'popup_config.yaml')
wechat_ocr_dir = os.path.join(tools_path, 'wx_ocr\WeChatOCR.exe')
wechat_dir = os.path.join(tools_path, 'wx_ocr')

time_YMD = time.strftime('%Y-%m-%d')


crash_pkg = ('com.seasun.jxsj3.xsj', 'com.YoStarJP.Arknights',
            'com.lightpaw.godsquest.aligames', 'com.pubg.krmobile', 'com.netease.sky', )

mobile_phone_emulator = {
    '5555': '127.0.0.1:5555',
    '5556': '127.0.0.1:5556',
    'MuMu': '127.0.0.1:7555',
    'MuMu12': '127.0.0.1:16384',
    '逍遥': '127.0.0.1:21503',
    '夜神': '127.0.0.1:62001',
    '夜神64': '127.0.0.1:62025',
    '手机模拟大师': '127.0.0.1:9974',
    '5554': 'emulator-5554',

}

sdk_pkg_name = {
    'tlog_sdk': 'com.tencent.sdk',
    'tlog_sdk_ano': 'com.tencent.sdk_ano',
    'ACE_Tools': 'com.tencent.green.ace',
    'ANO_Tools': 'com.tencent.green.ace.ano'
}

pkg_password = {
    'com.coloros.safecenter': 'tencent123',
    'BiometricPrompt': '000000'
}

