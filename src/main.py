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

class BoolSignal(QObject):
    ChangeState = Signal(bool)

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

        self.create_password = Password()
        self.find_password = Password()

        self.create_password_msg = StrSignal()
        self.find_password_msg = StrSignal()
        self.timer_msg = StrSignal()
        self.state = BoolSignal()
        
        self.pushButton_create_password.clicked.connect(self.btn_create_password_handler)
        self.pushButton_find_password.clicked.connect(self.btn_find_password_handler)

        self.create_password_msg.msg.connect(self.create_password_msg_handler)
        self.find_password_msg.msg.connect(self.find_password_msg_handler)
        self.timer_msg.msg.connect(self.timer_msg_handler)
        self.state.ChangeState.connect(self.change_state_handler)

        self.exit_event = Event()
        self.exit_event.clear()
        
    def create_password_thread_handler(self, exit_event : Event, msg : StrSignal, create_password : Password, size : int):
        start_time = time.time()
        while time.time() - start_time < 1:
            create_password.create(size)
            msg.msg.emit(create_password.password)
            time.sleep(random.uniform(0,.05))
            if exit_event.is_set() == True:
                break

    def find_password_thread_handler(self, exit_event : Event, state : BoolSignal, msg : StrSignal, timer_msg : StrSignal, find_password : Password, size : int):
        find_time = time.time()
        state.ChangeState.emit(False)
        while self.create_password.password != self.find_password.password:
            find_password.create(size)
            msg.msg.emit(self.find_password.password)
            timer_msg.msg.emit(str(int(time.time() - find_time)))
            #time.sleep(0.000001)
            if exit_event.is_set() == True:
                break
        state.ChangeState.emit(True)

    @Slot()
    def btn_create_password_handler(self):
        create_password_thread = Thread(target = self.create_password_thread_handler, args = (self.exit_event, self.create_password_msg, self.create_password, self.spinBox_password_len.value()))        
        create_password_thread.start()
        self.spinBox_password_len.setEnabled(False)
        self.pushButton_find_password.setEnabled(True)
    
    @Slot()
    def btn_find_password_handler(self):
        find_password_thread = Thread(target = self.find_password_thread_handler, args = (self.exit_event, self.state, self.find_password_msg, self.timer_msg, self.find_password, self.spinBox_password_len.value()))        
        find_password_thread.start()

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

    @Slot(bool)
    def change_state_handler(self, state : bool):
        self.pushButton_create_password.setEnabled(state)
        self.pushButton_find_password.setEnabled(state)
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.exit_event.set()
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()