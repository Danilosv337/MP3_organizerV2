from sys import argv 
from PySide6.QtWidgets import QApplication
from interfaces.system_window import App


qt = QApplication(argv)
app = App()
app.show()
qt.exec()