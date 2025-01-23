
from install_depencies import install_required_libraries

# 定义需要检查并安装的库列表
required_libraries = ['pynput', 'pyautogui']

# 调用函数进行库检查和安装
install_required_libraries(required_libraries)

# 下面是你原有的逻辑，添加鼠标点击监听
from pynput.mouse import Listener
import pyautogui

# 当鼠标点击时触发
def on_click(x, y, button, pressed):
    if pressed:  # 只在按下鼠标按钮时触发
        print(f"Mouse clicked at: x={x}, y={y}")  # 打印坐标

# 创建鼠标监听器
with Listener(on_click=on_click) as listener:
    listener.join()  # 启动监听器