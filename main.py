from sys import argv 
from PySide6.QtWidgets import QApplication
from interfaces.system_window import App

with open("layout/style.qss","r") as s:
    _style = s.read()

qt = QApplication(argv)
app = App()
app.setStyleSheet(_style)
app.show()
qt.exec()