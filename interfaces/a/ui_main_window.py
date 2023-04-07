# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowZTaAVr.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"QWidget#Form{\n"
"background-color: ;\n"
"	background-color: qlineargradient(spread:pad, x1:0.481, y1:0.0170455, x2:0.471, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(154, 153, 150, 255));\n"
"}\n"
"QLabel{\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton{\n"
"background-color: white;\n"
"color: black;\n"
"text-transform: uppercase;\n"
"border: 1 px solid gray;\n"
"padding: 8px;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(230,230,230);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(28, 113, 216);\n"
"color: white;\n"
"border: 2px solid gray;\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_select = QPushButton(self.frame)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_select, 4, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"max-height: 100px;\n"
"max-width: 100px;")
        self.label.setPixmap(QPixmap(u":/IMGS/icone_mp3.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1, Qt.AlignHCenter)

        self.inputtext_way = QLineEdit(self.frame)
        self.inputtext_way.setObjectName(u"inputtext_way")

        self.gridLayout_2.addWidget(self.inputtext_way, 1, 1, 1, 2)

        self.btn_organizer = QPushButton(self.frame)
        self.btn_organizer.setObjectName(u"btn_organizer")
        self.btn_organizer.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_organizer, 4, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.mp3_load = QProgressBar(self.frame)
        self.mp3_load.setObjectName(u"mp3_load")
        self.mp3_load.setValue(24)

        self.gridLayout_2.addWidget(self.mp3_load, 3, 0, 1, 3)

        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_close, 4, 2, 1, 1)

        self.edittext_message = QLabel(self.frame)
        self.edittext_message.setObjectName(u"edittext_message")
        self.edittext_message.setStyleSheet(u"font-size: 10px;")
        self.edittext_message.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.edittext_message, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_select.setText(QCoreApplication.translate("Form", u"Selecionar", None))
        self.label.setText("")
        self.inputtext_way.setPlaceholderText(QCoreApplication.translate("Form", u"Selecione a pasta Destino", None))
        self.btn_organizer.setText(QCoreApplication.translate("Form", u"Organizar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pasta:", None))
        self.btn_close.setText(QCoreApplication.translate("Form", u"Sair", None))
        self.edittext_message.setText("")
    # retranslateUi

