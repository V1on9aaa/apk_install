import os
import re
import pathlib
import subprocess
import time
import shutil
import xml.etree.ElementTree as ET
import logging
import socket
import yaml
from setting import *
from PIL import Image
from typing import List, Dict, Any, Optional, Union


logging.disable(logging.DEBUG)
time_YMD = time.strftime('%Y-%m-%d')

def read_yaml(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
    return data

def write_log(log_name, comm, res):
    file = open(rf'{log_path}\{log_name}.log', 'a', encoding='utf-8')
    file.write(time.strftime('%H:%M:%S') + '\ncomm:\n' + str(comm) + '\nresult:\n' + res + '=' * 80 + '\n\n')
    file.close()

def cmd_single_run(comm, decode_type='gbk'):
    '''只有一条执行的cmd指令'''
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

def devices():
    comm = f'{tools_path}\\adb.exe devices'
    check = cmd_single_run(comm, 'gbk').split('\r\n')
    if len(check) == 3:
        return 'no device'
    elif len(check) < 3:
        check = cmd_single_run(comm, 'gbk').split('\r\n')
    try:
        check.pop(-1)
        check.pop(-1)
        check.pop(0)
        return check
    except:
        return 'no device'

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

def check_port(port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))

    if result == 0:
        return True
    else:
        return False

def adb_connect(device):
    comm = rf'{tools_path}\adb.exe connect {device}'
    res = cmd_single_run(comm)

def get_size(pkg):
    size = os.path.getsize(pkg)
    return size

def check_endswith(path):
    apks, apk, aab, ipa, other = [], [], [], [], []
    pkg_list = {}
    if os.path.isdir:
        for file in pathlib.Path(path).glob("**/*"):
            if file.name.endswith('.aab'):
                aab.append(str(file))
            elif file.name.endswith('.apks'):
                apks.append(str(file))
            elif file.name.endswith('.apk'):
                apk.append(str(file))
            elif file.name.endswith('.ipa'):
                ipa.append(str(file))
            else:
                other.append(str(file))
    else:
        if path.name.endswith('.aab'):
            aab.append(str(path))
        elif path.name.endswith('.apks'):
            apks.append(str(path))
        elif path.name.endswith('.apk'):
            apk.append(str(path))
        elif path.name.endswith('.ipa'):
            ipa.append(str(path))
        else:
            other.append(str(path))
    pkg_list['apk'], pkg_list['aab'], pkg_list['apks'], pkg_list['ipa'], pkg_list['other'] = apk, aab, apks, ipa, other
    return pkg_list


def get_apk_name(pkg):
    comm = rf'{tools_path}\aapt2.exe dump packagename "{pkg}"'
    pkg_name = cmd_single_run(comm, decode_type='utf-8').split('\r')[0]
    if pkg_name == '':
        raise
    return pkg_name

def get_aab_name(aab):
    comm = f'java -jar {tools_path}\\bundletool.jar dump resources --bundle={aab}'
    res = cmd_single_run(comm)
    pkgname = res.split("'")[1]
    return pkgname

def get_pkg_name(pkg_path):
    if check_apk_aab(pkg_path) == '.apk':
        return get_apk_name(pkg_path)
    elif check_apk_aab(pkg_path) == '.aab':
        return get_aab_name(pkg_path)
    else:
        return False

def extract(ori_file, mode='universal'):
    '''aab提取'''
    print(f'提取aab文件{ori_file}', flush=True)
    new_file = f'{ori_file}.apks'
    # comm = f'java -jar {tools_path}\\bundletool.jar build-apks --bundle={ori_file} --output={new_file}.apks --overwrite --ks="{tools_path}\\test.keystore" --ks-pass=pass:123456 --ks-key-alias=test --key-pass=pass:123456'
    if mode == 'universal':
        comm = f'java -jar {tools_path}\\bundletool.jar build-apks --bundle={ori_file} --output={new_file} --mode={mode}'
    else:
        comm = f'java -jar {tools_path}\\bundletool.jar build-apks --bundle={ori_file} --output={new_file}'
    result = cmd_single_run(comm)
    return result

def ext_aab(aab):
    for x in range(len(aab)):
        name = str(aab[x])
        extract(aab[x], name)

def align(apk, tools_path):
    '''4k对齐'''
    time_HMS = time.strftime('%H:%M:%S')
    new_name = apk.split('.apk')[0] + '_resign.apk'
    comm = rf'{tools_path}\zipalign.exe -p -f -v 4 {apk} {new_name}'
    info = cmd_single_run(comm)
    if re.search(r'Verification succesful', info) != None:
        print(f'4k对齐完成: {apk} {time_HMS}', flush=True)
    else:
        print(f'4k对齐失败: {apk} {time_HMS}', flush=True)
    return new_name

def sign(pkg, jar, keystore, keystore_password, sign_version=None):
    '''重签名'''
    if sign_version is None:
        sign_version = ['true', 'true', 'false']
    comm = rf'java -jar {jar} sign --ks {keystore} --v1-signing-enabled {str(sign_version[0]).lower()} --v2-signing-enabled {str(sign_version[1]).lower()} --v3-signing-enabled {str(sign_version[2]).lower()} {pkg}'
    obj = subprocess.Popen(comm, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    obj.stdin.write(keystore_password.encode('utf-8'))
    obj.stdin.write('\n'.encode('utf-8'))
    info, err = obj.communicate()
    result = info.decode('gbk')
    print(f'重签名: {pkg}', flush=True)
    # print(result, end='')
    return result

def check_sign(pkg, tools_path):
    '''检查是否重签名'''
    comm = rf'{tools_path}\jarsigner.exe -verify {pkg}'
    result = cmd_single_run(comm)
    if re.search(r'jar 已验证', result) != None:
        print('已验证签名 ' + str(pkg), flush=True)
    elif re.search(r'jar 未签名', result) != None:
        print('未签名' + str(pkg), flush=True)

def amend_xml_element_text(xml, element_name, new_cont):
    doc = ET.parse(xml)
    root = doc.getroot()
    sub = root.find(element_name)
    sub.text = new_cont
    doc.write(xml)

def check_sign_ver(pkg):
    '''检查重签名的等级'''
    order = rf'java -jar {tools_path}\apksigner.jar verify -v {pkg}'
    obj = subprocess.Popen(order, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    info, err = obj.communicate()
    result = info.decode('gbk')
    print(result, end='', flush=True)
    return result

def check_apk_aab(pkg):
    file_ext = os.path.splitext(pkg)[1].lower()
    if file_ext == '.apk' or '.aab':
        return file_ext
    else:
        return False

def check_key(dics, d_key):
    for key in dics.keys():
        if key == d_key:
            return True
    return False

def rm_document(path):
    for i in pathlib.Path(path).glob("**/*"):
        os.remove(i)

def mv_document(old_path, new_path):
    for i in pathlib.Path(old_path).glob("**/*"):
        fpath, fname = os.path.split(i)
        shutil.move(i, new_path + '\\' + fname)

def del_document(path):
    for s in os.listdir(path):
        os.remove(path+'/'+s)

def absolute_coordinate(img_path: str, pixel_point):
    img = Image.open(img_path)
    width, height = img.size
    ac_x, ac_y, = round(pixel_point[0] / width, 2), round(pixel_point[1] / height, 2)
    return (ac_x, ac_y)

def text_split_2_ascii(text: str):
    text_list = []
    for t in text:
        if str_word_is_int(t):
            text_list.append(int(t))
        else:
            text_list.append(t)
    return text_list

def ascii_conversion(text: str or int):
    try:
        if type(text) == str:
            return ord(text)
        else:
            return chr(text)
    except:
        raise 'The length of the string should be 1'

def str_word_is_int(text: str):
    try:
        if 48 <= ord(text) <= 57:
            return True
        else:
            return False
    except:
        raise 'The length of the string should be 1'

def crop_img(img_path: str, coordinate: tuple, save_path: str = None):
    im = Image.open(img_path)
    img2 = im.crop(coordinate)
    if save_path == None:
        name = os.path.join(os.path.dirname(img_path), str(time.time())+'.png')
    else:
        name = save_path
    img2.save(name)

def android_pkgs_list(pkg_path: str) -> list or bool:
    if os.path.isdir(pkg_path):
        p_list = check_endswith(pkg_path)
        return p_list['apk']+p_list['aab']
    else:
        if check_apk_aab(pkg_path):
            return [pkg_path]
        else:
            return False

# 辅助函数优化
def popup_data() -> Dict[str, Any]:
    """读取弹窗配置数据（优化版）"""
    y_data = read_yaml(popup_config_path)

    # 使用字典推导式简化代码[5](@ref)
    popup_special = {}
    for item in y_data['special_handling']:
        for device, value in item.items():
            popup_special[device] = value

    return {
        'click_traversal_popup': y_data['click_traversal_popup'],
        'popup_pkgname': y_data['popup_pkgname'],
        'popup_special': popup_special
    }
