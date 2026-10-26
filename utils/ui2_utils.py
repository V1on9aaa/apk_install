import os
import re
import time
import subprocess
import uiautomator2 as uiauto2
import xml.etree.ElementTree as ET
# from setting import *
from utils.utils import *



class ui2():
    def __init__(self, device):
        self.Device = device
        self.dev_uiauto = uiauto2.connect(device)

    def install_pkg(self, pkg_path):
        self.dev_uiauto.app_install(pkg_path)

    def uninstall(self, pkg_name):
        self.dev_uiauto.app_uninstall(pkg_name)

    def start_app(self, pkg_name):
        self.dev_uiauto.app_start(pkg_name)

    def stop_app(self, pkg_name):
        self.stop_app(pkg_name)

    def get_text_bounds(self, text):
        try:
            return self.dev_uiauto(text=text).bounds()
        except:
            return False

    def get_content_bounds(self, text):
        try:
            return self.dev_uiauto(contentDescription=text).bounds()
        except:
            return False

    def click_word(self, word, accurate_match=True):
        try:
            if accurate_match == True:
                self.dev_uiauto(text=word)[0].click(timeout=30)
            else:
                self.dev_uiauto(textContains=word)[0].click(timeout=30)
            return True
        except:
            return False

    def popup_exists(self, popup_list, text_location=None):
        popup, text = 0, None
        if text_location != None:
            if self.search_text(text_location):
                text = 1
            else:
                text = 0
        for pkgname in popup_list:
            Focus = self.dev_uiauto.app_current()['package']
            focus = re.search(pkgname, Focus)
            if focus != None:
                popup = 1
        return {'popup': popup, 'text': text}

    def search_text(self, text):
        all_texts = self.get_ui2_text()
        for ua2_text in all_texts.keys():
            if ua2_text == text:
                return True
        return False

    def get_ui2_text(self):
        dev = self.dev_uiauto
        xml_str = dev.dump_hierarchy()
        root = ET.fromstring(xml_str)

        all_texts = {}
        for element in root.iter():
            clickable = element.attrib.get('clickable')
            text = element.attrib.get('text')
            if text and text.strip() != '':
                all_texts[text.strip()] = clickable
        # print(all_texts)
        log_name = '2026-1-13'
        write_log(log_name, 'ua2', str(all_texts))
        return all_texts

# uat2 = ui2('9e2bd91c')
# uat2.get_ui2_text()
