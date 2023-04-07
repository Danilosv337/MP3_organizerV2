from interfaces.a.ui_main_window import *
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QIcon
from modules.system import teste_walk
import eyed3

class App(QWidget,Ui_Form):
    def __init__(self,parent= None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QIcon(":/IMGS/icone_mp3.png"))
        self.way= ''
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_select.clicked.connect(self.get_directory)
        self.btn_organizer.clicked.connect(lambda: self.organize(self.way))
        self.mp3_load.setValue(0)


    def get_directory(self):
        self.way = QFileDialog.getExistingDirectory()
        self.inputtext_way.setText(f"{self.way}")
    def organize(self,way):
        try:
            files = teste_walk(way)
            if files == []: 
                self.edittext_message.setStyleSheet("font-size: 20px; color: red;")
                self.edittext_message.setText('Sem Arquivos ".mp3"')
                return
            self.mp3_load.setMaximum(len(files))
            num: int = 0
            for way_file,file in files:
                num += 1
                self.mp3_load.setValue(num)
                audio = eyed3.load(way_file)
                if not audio.tag:
                    audio.initTag()
                audio.tag.title = file.replace(".mp3","")
                audio.tag.save(version=(2,3,0))
            self.edittext_message.setStyleSheet("font-size: 20px; color: green;")
            self.edittext_message.setText("Finalizado!")
        except Exception as erro:
            with open("mp3organizer.log","a") as logfile:
                logfile.write(erro)
            self.edittext_message.setStyleSheet("font-size: 20px; color: red;")
            self.edittext_message.setText('Ocorreu um erro')


            
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except Exception:
            pass
        
            