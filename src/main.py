import sys
import time
import random
import string
import itertools

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Slot, Signal, QObject
from PySide6.QtGui import QCloseEvent

from ui.main_form import Ui_MainWindow

from threading import Thread, Event, Lock

class StrSignal(QObject):
    msg = Signal(str)

class BoolSignal(QObject):
    ChangeState = Signal(bool)

class Password:
    def __init__(self):        
        self.password = ""
        self.ord_list = []
        
    def create(self, size : int, chars : str = string.ascii_letters + string.digits + string.punctuation):
        self.ord_list = []
        self.password = [random.choice(chars) for _ in range(size)]
        self.ord_list_update()
        self.password = ''.join(self.password)

    def ord_list_update(self):
        for idx in self.password:
            self.ord_list.append(ord(idx))

    def select_create(self, select : list):
        # 33 ~ 64
        # 65 ~ 96
        # 97 ~ 126
        # 비밀번호는 33 ~ 126 사이의 값만 사용함
        self.ord_list = []
        self.password = []

        for idx in select:
            self.password.append(chr(idx))

        self.password = ''.join(self.password)
        self.ord_list_update()
    
    def show(self):
        print(f"ord_list : {self.ord_list}")
        print(f"password : {self.password}")
        
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

        self.lock = Lock()
        self.exit_event = Event()
        self.exit_event.clear()
        
    def create_password_thread_handler(self,msg : StrSignal, create_password : Password, size : int):        
        for idx in range(10):
            create_password.create(size)
            msg.msg.emit(create_password.password)
            time.sleep(random.uniform(0,.05))
        

    def find_password_thread_handler(self,
                                    lock : Lock,
                                    exit_event : Event,
                                    thread_id : int,
                                    state : BoolSignal,
                                    msg : StrSignal,
                                    timer_msg : StrSignal,
                                    find_password : Password,
                                    target_password,
                                    size : int,
                                    start_ord : int,
                                    end_ord : int):
        find_time = time.time()
        state.ChangeState.emit(False)

        for tem in itertools.product(range(start_ord, end_ord), repeat=size):
            
            #lock.acquire()

            if target_password == find_password.password:
                break
            
            if exit_event.is_set():
                break
            
            find_password.select_create(tem)
            msg.msg.emit(find_password.password)
            timer_msg.msg.emit(str(int(time.time() - find_time)))
            time.sleep(random.uniform(0,.000001))

            #print(f"thread_id : {thread_id} tem : {tem} find_password : {find_password.password}")
            #lock.release()

        if target_password == find_password.password:
            state.ChangeState.emit(True)

    @Slot()
    def btn_create_password_handler(self):
        create_password_thread = Thread(target = self.create_password_thread_handler, args = (self.create_password_msg, self.create_password, self.spinBox_password_len.value()))        
        create_password_thread.start()
        self.spinBox_password_len.setEnabled(False)
        self.pushButton_find_password.setEnabled(True)
    
    @Slot()
    def btn_find_password_handler(self):        
        self.find_password_thread_1 = Thread(target = self.find_password_thread_handler, args = (self.lock, self.exit_event, 1, self.state, self.find_password_msg, self.timer_msg, self.find_password, self.create_password.password, self.spinBox_password_len.value(), 33, 127)) # 47
        #self.find_password_thread_2 = Thread(target = self.find_password_thread_handler, args = (self.lock, self.exit_event, 2, self.state, self.find_password_msg, self.timer_msg, self.find_password, self.create_password.password, self.spinBox_password_len.value(), 81, 127)) # 46
        
        self.find_password_thread_1.start()
        #self.find_password_thread_2.start()

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
        try:
            self.find_password_thread_1.join(1)
            self.find_password_thread_2.join(1)
        except:
            pass
        return super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()