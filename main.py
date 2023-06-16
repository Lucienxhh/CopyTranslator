from time import sleep
from copier import Clipboard, AutoCopier
from ui import Ui_Dialog
from translator import Translator
from sys import argv, exit
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QThread, Signal, Qt
from PySide2.QtGui import QIcon, QPixmap
from icon import icon
import xml.etree.ElementTree as ET

class MainWindow(QWidget):  
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(
            Qt.WindowMinimizeButtonHint |      # Enable minimize button
            Qt.WindowCloseButtonHint |         # Enable close button
            Qt.WindowStaysOnTopHint)           # Window stays on top
        pixmap = QPixmap()
        pixmap.loadFromData(icon)
        self.setWindowIcon(QIcon(pixmap))

        self.ui = Ui_Dialog()   # Create UI
        self.ui.setupUi(self)   # Import UI

        self.checker = Checker(self.ui)

    def run(self):
        self.checker.start()
    
    def closeEvent(self, event):
        self.checker.close()
        event.accept()
        tran.close()
        
class Checker(QThread):
    singal = Signal(str, str)
    def __init__(self, ui):
        super().__init__()
        self.clipboard = Clipboard()
        self.isworking = True
        self.singal.connect(ui.changeText)
    
    def close(self):
        self.isworking = False
        self.wait()
        print("checker is free")

    def run(self):
        while self.isworking:
            flag, text = self.clipboard.getText() # Get clipboard content
            if flag:                              # If new copied content
                tran_text = tran.translate(text)  # Get translated text
                self.singal.emit(text, tran_text) # Send text to UI thread
                sleep(1)
            else:
                sleep(0.5)
    
        self.singal.disconnect()

if __name__ == "__main__":
    tree = ET.parse("config.xml")
    root = tree.getroot()

    headless = bool(int(root.find("headless").text))
    autocopy = bool(int(root.find("autocopy").text))
    refresh_rate = int(root.find("refresh_rate").text)
    refresh_time = float(root.find("refresh_time").text)

    app = QApplication(argv)   # Create application
    tran = Translator(headless=headless, refresh_time=refresh_time, refresh_rate=refresh_rate) # Create translator
    myWindow = MainWindow()    # Create window
    
    if autocopy:
        AutoCopier() 

    myWindow.show()            # Show window
    myWindow.run()             # Run window
    exit(app.exec_())          # Run program until closed
