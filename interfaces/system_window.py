from interfaces.a.ui_main_window import *
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import QThread
from modules.threads import threadProcess
from modules.system import get_files
import eyed3



class App(QWidget,Ui_Form):
    def __init__(self,parent= None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowIcon(QIcon(":/IMGS/icone_mp3.png"))
        self.way= ''
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(500,300)
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_select.clicked.connect(self.get_directory)
        self.btn_organizer.clicked.connect(self.start_organize)
        # self.btn_organizer.clicked.connect(lambda: self.start_organize())
        self.mp3_load.setValue(0)
        self.lista,self.lista2,self.lista3 = [],[],[]

    def hardprocess(self,lista):
        self._worker = threadProcess()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread
        worker.setlista(lista)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)
        worker.started.connect(self.startHardprocess)
        worker.progressed.connect(self.progressHardprocess)
        worker.finished.connect(self.finishHardprocess)
        thread.start()
    def hardprocess2(self,lista):
        self._worker2 = threadProcess()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2
        worker.setlista(lista)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)
        worker.started.connect(self.startHardprocess)
        worker.progressed.connect(self.progressHardprocess)
        worker.finished.connect(self.finishHardprocess)
        thread.start()
    def hardprocess3(self,lista):
        self._worker3 = threadProcess()
        self._thread3 = QThread()

        worker = self._worker3
        thread = self._thread3
        worker.setlista(lista)
        worker.moveToThread(thread)
        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(worker.deleteLater)
        worker.started.connect(self.startHardprocess)
        worker.progressed.connect(self.progressHardprocess)
        worker.finished.connect(self.finishHardprocess)
        thread.start()

    def startHardprocess(self):
        self.finished_threads = 0
        self.btn_organizer.setDisabled(True)
        self.num = 0
    def progressHardprocess(self,sucess,value):
        if sucess:
            self.edittext_message.setStyleSheet("font-size: 20px; color: green;")
            self.edittext_message.setText(f"Música {value} Finalizada!")
        else:
            self.edittext_message.setStyleSheet("font-size: 20px; color: red;")
            self.edittext_message.setText(f"Erro na música: {value}")
        self.num +=1
        self.mp3_load.setValue(self.num)
    def finishHardprocess(self):
        self.finished_threads += 1
        if self.finished_threads == 3:
            self.btn_organizer.setEnabled(True)




    def get_directory(self):
        self.way = QFileDialog.getExistingDirectory()
        self.inputtext_way.setText(f"{self.way}")

    def start_organize(self):
        files = get_files(self.way)
        self.mp3_load.setMaximum(len(files))
        if files == []:
            self.edittext_message.setStyleSheet("font-size: 20px; color: red;")
            self.edittext_message.setText('Sem Arquivos ".mp3"')
            return
        self.progressorganize, num = 0,0
        for x in files:
            if num == 0:
                self.lista.append(x)
                num += 1
                continue
            elif num == 1:
                self.lista2.append(x)
                num += 1
                continue
            else:
                self.lista3.append(x)
                num = 0
                continue

        if self.lista != []:
            self.hardprocess(self.lista)
        if self.lista2 != []:
            self.hardprocess2(self.lista2)
        if self.lista3 != []:
            self.hardprocess3(self.lista3)


    def organize(self,lista):
        for way_file, file in lista:
            try:
                self.progressorganize += 1
                self.mp3_load.setValue(self.progressorganize)
                audio = eyed3.load(way_file)
                if not audio.tag or audio.tag == None:
                    audio.initTag()
                audio.tag.title = file.replace(".mp3","")
                audio.tag.save(version=(2,3,0))
                self.edittext_message.setStyleSheet("font-size: 20px; color: green;")
                self.edittext_message.setText(f"Música {file} Finalizada!")
            except Exception as erro:
                with open("mp3organizer.log","a") as logfile:
                    logfile.write(f"O arquivo {file} Apresentou o erro: \n \
                                  {erro} \n\n")
                    self.edittext_message.setStyleSheet("font-size: 20px; color: red;")
                    self.edittext_message.setText(f'Erro na música: {file}')

            
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        except Exception:
            pass
        
            