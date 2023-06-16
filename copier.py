from pyperclip import paste
from platform import system
class Clipboard():
    def __init__(self):
        self.setParameters()

    # 设置基本参数，不同平台的换行和转接符不同
    def setParameters(self):
        if system() == "Windows":
            self.line_break = "\r\n"
            self.hyphen = ""
        elif system() == "Linux":
            self.line_break = "\n"
            self.hyphen = "-"
        else:
            self.line_break = "\n"
            self.hyphen = "-"
        self.old = "old"
    
    def getText(self):
        try:
            new = paste()                              # 获取粘贴板上的文本
        except Exception:
            print("fail to get clipboard")
            new = ""
        finally:
            if new == self.old:
                return False, ""
            else:
                self.old = new
                new = new.replace(self.line_break, " ") # 去除换行符
                new = new.replace(self.hyphen, "")      # 去除行尾转接符
                return True, new

from pynput.mouse import Listener, Button
from pynput.keyboard import Key, Controller

class AutoCopier():
    __press_xy = (0, 0)  # 私有变量 鼠标左键按下时的位置

    def __init__(self):
        self.keyboard = Controller()                     # 初始化键盘控制器
        self.listener = Listener(on_click=self.on_click) # 初始化鼠标监听器
        self.listener.start()                            # 开启鼠标监听器线程

    # 点击函数
    def on_click(self, x, y, button, pressed):           
        if button == Button.left:             # 左键点击
            if pressed:                       # 左键按下
                self.__press_xy = (x, y)      # 记录当前鼠标位置
            else:                             # 左键松开           
                if self.__press_xy != (x, y): # 按下位置和松开位置不一致
                    self.copy()               # 说明操作是划词，执行复制函数
    
    # 复制函数
    def copy(self): 
        with self.keyboard.pressed(Key.ctrl): # 按下ctrl，with语句结束后自动松开
            self.keyboard.press('c')          # 按下c
            self.keyboard.release('c')        # 松开c

    # 等待线程终止
    def wait_to_stop(self):
        self.listener.join()

# for test
if __name__ == '__main__':
    at = AutoCopier()
    at.wait_to_stop()