import sys
import os
import json

def get_resource_path(relative_path):
    """ Locate the path to the resource file inside the executable file or in the development environment """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller Running Environment
    else:
        base_path = os.path.dirname(__file__)  # general execution environment
    
    return os.path.join(base_path, relative_path)

# Example: Reading files inside the hello folder
config_path = get_resource_path("my_package/hello/config.json")

with open(config_path, "r", encoding="utf-8") as f:
    config_data = json.load(f)
    print("Config Loaded:", config_data)
