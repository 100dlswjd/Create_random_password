# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 207)
        MainWindow.setMinimumSize(QSize(450, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_create_password = QLabel(self.centralwidget)
        self.label_create_password.setObjectName(u"label_create_password")

        self.horizontalLayout.addWidget(self.label_create_password)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_create_password = QPushButton(self.centralwidget)
        self.pushButton_create_password.setObjectName(u"pushButton_create_password")

        self.horizontalLayout.addWidget(self.pushButton_create_password)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label_find_password = QLabel(self.centralwidget)
        self.label_find_password.setObjectName(u"label_find_password")

        self.horizontalLayout_2.addWidget(self.label_find_password)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_find_password = QPushButton(self.centralwidget)
        self.pushButton_find_password.setObjectName(u"pushButton_find_password")
        self.pushButton_find_password.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButton_find_password)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_find_timer = QLabel(self.centralwidget)
        self.label_find_timer.setObjectName(u"label_find_timer")
        self.label_find_timer.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_find_timer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_time_min = QLabel(self.centralwidget)
        self.label_time_min.setObjectName(u"label_time_min")
        self.label_time_min.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_time_min)

        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_time)

        self.label_time_sec = QLabel(self.centralwidget)
        self.label_time_sec.setObjectName(u"label_time_sec")
        self.label_time_sec.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_time_sec)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_create_password.setText(QCoreApplication.translate("MainWindow", u"\uc0dd\uc131\ub41c \ube44\ubc00\ubc88\ud638 : ", None))
        self.pushButton_create_password.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638 \ub79c\ub364 \uc0dd\uc131", None))
        self.label_find_password.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638 \ucc3e\uae30 : ", None))
        self.pushButton_find_password.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638 \ucc3e\uae30", None))
        self.label_find_timer.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\ub294\ub370 \uac78\ub9b0 \uc2dc\uac04", None))
        self.label_time_min.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_time_sec.setText(QCoreApplication.translate("MainWindow", u"00", None))
    # retranslateUi

