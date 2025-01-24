from install_depencies import install_required_libraries

# 定义需要检查并安装的库列表
required_libraries = ['random', 'pyautogui', 'time']

# 调用函数进行库检查和安装
install_required_libraries(required_libraries)

import pyautogui
import time
import random

# 配置坐标参数
coordinates = {
    'config_button': (2439, 442),  # 配置按钮坐标
    'product_link': (887, 575),  # 商品链接坐标
    'right_click_position': (2099, 668),  # 右键点击的位置
    'paste_modal': (940, 753),  # 粘贴网页源码的文本框位置
    'transform_link': (695, 468),  # 转链页面粘贴位置
    'transform_button': (640, 686),  # 转链按钮位置
    'copy_button': (633, 1025),  # 复制按钮位置
    'save_button': (1851, 1269),  # 保存按钮位置
    'paste_first_page': (1060, 686)  # 第一个页面的粘贴位置
}

# 模拟点击商品配置页中的“配置”按钮，弹出modal页面
def click_config_button():
    pyautogui.click(x=coordinates['config_button'][0], y=coordinates['config_button'][1])  
    time.sleep(2)

def click_product_link_and_copy_source():
    # 点击商品名称链接
    pyautogui.click(x=coordinates['product_link'][0], y=coordinates['product_link'][1])  
    time.sleep(2)  # 等待页面加载

    # random_mouse_move()
    
    # 移动到右键点击位置
    # current_position = pyautogui.position()
    # target_position = (coordinates['right_click_position'][0], coordinates['right_click_position'][1])

    # move_mouse_along_curve(current_position, target_position, duration=2)

    pyautogui.moveTo(x=coordinates['right_click_position'][0], y=coordinates['right_click_position'][1])
    pyautogui.click(button='right')
    time.sleep(1)
    
    # 模拟按下“上箭头”两次，选择倒数第二个选项（查看网页源码）
    pyautogui.typewrite(['up', 'up', 'enter']) 
    time.sleep(2)
    
    # 选择全选并复制网页源码
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

def close_extra_tabs():
    # 关闭当前标签页
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)

def switch_to_first_tab():
    pyautogui.hotkey('ctrl', '1')
    time.sleep(1)

# 切换回原始页面并粘贴网页源码到文本框
def paste_source_code_in_modal():
    pyautogui.click(x=coordinates['paste_modal'][0], y=coordinates['paste_modal'][1])
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

def copy_link_and_go_to_transform():
    pyautogui.moveTo(x=coordinates['product_link'][0], y=coordinates['product_link'][1])
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.typewrite(['up', 'up', 'up', 'enter'])

    # 切换到转链页面
    pyautogui.hotkey('ctrl', '2')
    time.sleep(1)

    # 粘贴链接
    pyautogui.click(x=coordinates['transform_link'][0], y=coordinates['transform_link'][1])
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # 点击转链按钮
    pyautogui.click(x=coordinates['transform_button'][0], y=coordinates['transform_button'][1])
    time.sleep(2)

    # 点击复制按钮
    pyautogui.click(x=coordinates['copy_button'][0], y=coordinates['copy_button'][1])
    time.sleep(1)

    # 切换回第一个页面
    pyautogui.hotkey('ctrl', '1')
    time.sleep(1)

    # 粘贴到文本框
    pyautogui.click(x=coordinates['paste_first_page'][0], y=coordinates['paste_first_page'][1])
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # 点击保存按钮
    pyautogui.click(x=coordinates['save_button'][0], y=coordinates['save_button'][1])
    time.sleep(3)

def random_scroll():
    # 假设页面可滚动的范围
    for _ in range(5):  # 控制滚动的次数
        direction = random.choice(['up', 'down'])  # 随机选择向上或向下滚动
        distance = random.randint(200, 2800)  # 随机滚动的幅度

        if direction == 'down':
            pyautogui.scroll(-distance)  # 向下滚动
        else:
            pyautogui.scroll(distance)  # 向上滚动

        time.sleep(random.uniform(1, 3))  # 随机间隔时间

    # 模拟快速滚动到顶部
    time.sleep(random.uniform(2, 3))
    pyautogui.scroll(1000)  # 快速滚动到顶部
    time.sleep(random.uniform(1, 2))  # 稍作停顿

    # 再随机滚动一些内容，向下滚动更多
    for _ in range(3):
        distance = random.randint(800, 1500)  # 向下滚动较大的距离
        pyautogui.scroll(-distance)
        time.sleep(random.uniform(2, 4))  # 每次滚动后等待一段时间

def random_mouse_move():
    screen_width, screen_height = pyautogui.size()
    for _ in range(1):  # 控制鼠标随机移动次数
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=random.uniform(0.5, 1.5))  # 随机移动鼠标
        time.sleep(random.uniform(1, 2)) 

def bezier_curve(p0, p3, steps=100):
    """
    计算从 p0 到 p3 的二次贝塞尔曲线的路径
    p0: 起点
    p3: 终点
    steps: 步数
    """
    # 生成随机的控制点 p1
    p1 = (random.randint(p0[0], p3[0]), random.randint(p0[1], p3[1]))

    curve_points = []
    for t in range(steps + 1):
        t = t / steps
        # 二次贝塞尔公式
        x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p3[0]
        y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p3[1]
        curve_points.append((x, y))
    return curve_points

# 让鼠标沿贝塞尔曲线平滑移动
def move_mouse_along_curve(p0, p3, duration=1):
    """
    让鼠标沿着贝塞尔曲线平滑移动
    p0: 当前鼠标位置
    p3: 目标位置
    duration: 整个路径的移动时间
    """
    curve_points = bezier_curve(p0, p3)
    
    for point in curve_points:
        pyautogui.moveTo(point[0], point[1], duration)
        time.sleep(1)

def main():
    click_config_button()
    click_product_link_and_copy_source()
    close_extra_tabs()
    close_extra_tabs()
    switch_to_first_tab()
    paste_source_code_in_modal()
    copy_link_and_go_to_transform()

if __name__ == "__main__":
    iterations = 5
    for _ in range(iterations):
        main()
