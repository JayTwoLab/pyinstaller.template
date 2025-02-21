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

## How to make executable file
- Execute `run_pyinstaller.cmd`
```sh
pyinstaller --onefile --add-data "my_package/hello;my_package/hello" my_package/main.py
```
 
 
