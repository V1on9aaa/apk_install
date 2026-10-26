import os
import json
import time
import re
from utils.utils import *
from typing import List, Dict, Union, Optional
from pathlib import Path
from wechat_ocr.ocr_manager import OcrManager, OCR_MAX_TASK_ID


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
        # print(img_path, text, accurate_match)
        results = self.ocr(img_path)
        log_name = '2026-1-13'
        comm = img_path
        write_log(log_name, comm, str(results))
        # print(results)
        # self.box_center_crop(img_path, results)
        box_point = self.box_center_point(results[0])
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

