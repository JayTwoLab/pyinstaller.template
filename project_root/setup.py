from setuptools import setup
import py2exe

setup(
    options={
        "py2exe": {
            "includes": ["importlib.resources"],
            "bundle_files": 1,
            "compressed": True,
        }
    },
    data_files=[("my_package/hello", ["my_package/hello/config.json", "my_package/hello/data.txt"])],
    zipfile=None,
    windows=[{"script": "my_package/main.py"}],
)
