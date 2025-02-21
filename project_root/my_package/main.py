import sys
import os
import json

def get_resource_path(relative_path):
    """ 실행 파일 내부 또는 개발 환경에서 리소스 파일의 경로를 찾음 """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller 실행 환경
    else:
        base_path = os.path.dirname(__file__)  # 일반 실행 환경
    
    return os.path.join(base_path, relative_path)

# 예제: hello 폴더 내부의 파일 읽기
config_path = get_resource_path("my_package/hello/config.json")

with open(config_path, "r", encoding="utf-8") as f:
    config_data = json.load(f)
    print("Config Loaded:", config_data)
