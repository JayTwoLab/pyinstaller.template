# pyinstaller.template
- How to add a whole specific folder (including subdirectories) in PyInstaller.

## Template Code
- See `project_root` directory.
```
project_root/
│── my_package/                # package folder
│   │── __init__.py            # For package recognition (you can leave it empty)
│   │── main.py                # Python files to run
│   │── hello/                  # Resource folder to include
│   │   │── config.json         # Example Resource File
│   │   │── data.txt            # Data files to add
│   │   └── assets/             # Subfolders (can be included in PyInstaller)
│   │       ├── image.png       # Image file
│   │       ├── sound.wav       # Audio Files
│   │       └── settings.yaml   # Configuration file
│── setup.py                    # Select: PyInstaller execution script
```

- `main.py`
```python
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
``` 

## How to make executable file
- Execute `run_pyinstaller.cmd`
```sh
pyinstaller --onefile --add-data "my_package/hello;my_package/hello" my_package/main.py
```
 
 
