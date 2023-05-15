import sys
import time
import random
import string

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Slot, Signal, QObject
from PySide6.QtGui import QCloseEvent

from ui.main_form import Ui_MainWindow

from threading import Thread, Event

class StrSignal(QObject):
    msg = Signal(str)

class Password:
    def __init__(self):        
        self.password = ""
        
    def create(self, size : int, chars : str = string.ascii_letters + string.digits + string.punctuation):
        self.password = [random.choice(chars) for _ in range(size)]
        self.password = ''.join(self.password)
        
    def __del__(self):
        pass

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit_flag = False

        self.create_password = Password()
        self.find_password = Password()

        self.create_password_msg = StrSignal()
        self.find_password_msg = StrSignal()
        self.timer_msg = StrSignal()
        
        self.pushButton_create_password.clicked.connect(self.btn_create_password_handler)
        self.pushButton_find_password.clicked.connect(self.btn_find_password_handler)

        self.create_password_msg.msg.connect(self.create_password_msg_handler)
        self.find_password_msg.msg.connect(self.find_password_msg_handler)
        self.timer_msg.msg.connect(self.timer_msg_handler)
            
        self.create_password_thread = Thread(target = self.create_password_thread_handler)
        self.create_password_event = Event()
        self.create_password_event.set()
        self.create_password_thread.start()

        self.find_password_thread = Thread(target = self.find_password_thread_handler)
        self.find_password_event = Event()
        self.find_password_event.set()
        self.find_password_thread.start()

    def create_password_thread_handler(self):
        while self.exit_flag == False:
            while self.create_password_event.is_set() == False:
                start_time = time.time()
                while time.time() - start_time < 1:
                    self.spinBox_password_len.setEnabled(False)
                    self.create_password.create(self.spinBox_password_len.value())
                    self.create_password_msg.msg.emit(self.create_password.password)
                    time.sleep(random.uniform(0,.05))
                self.create_password_event.set()
            time.sleep(0)

    def find_password_thread_handler(self):
        while self.exit_flag == False:            
            while self.find_password_event.is_set() == False:
                self.pushButton_create_password.setEnabled(False)
                self.pushButton_find_password.setEnabled(False)
                find_time = time.time()
                while self.create_password.password != self.find_password.password:
                    self.find_password.create(self.spinBox_password_len.value())
                    self.find_password_msg.msg.emit(self.find_password.password)
                    self.timer_msg.msg.emit(str(int(time.time() - find_time)))
                self.find_password_event.set()
                self.pushButton_create_password.setEnabled(True)
                self.pushButton_find_password.setEnabled(True)

    @Slot()
    def btn_create_password_handler(self):
        self.create_password_event.clear()
        self.pushButton_find_password.setEnabled(True)
    
    @Slot()
    def btn_find_password_handler(self):
        self.find_password_event.clear()

    @Slot(str)
    def create_password_msg_handler(self, msg : str):
        self.label_create_password.setText(f"생성된 비밀 번호 : {msg}")

    @Slot(str)
    def find_password_msg_handler(self, msg : str):
        self.label_find_password.setText(f"비밀번호 찾기 : {msg}")

    @Slot(str)
    def timer_msg_handler(self, msg : str):
        msg = int(msg)
        self.label_time_min.setText(str(msg // 60))
        self.label_time_sec.setText(str(msg % 60))
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.exit_flag = True
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()