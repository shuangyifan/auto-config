# install_libs.py
import subprocess
import sys

def install_required_libraries(libraries):
    for lib in libraries:
        try:
            # 尝试导入库
            __import__(lib)
            print(f"{lib} is already installed.")
        except ModuleNotFoundError:
            # 如果库未安装，则尝试安装
            print(f"{lib} is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"{lib} installed successfully.")
