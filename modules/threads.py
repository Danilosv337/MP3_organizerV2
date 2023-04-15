from PySide6.QtCore import QObject,Signal
import eyed3

class threadProcess(QObject):
    started = Signal()
    progressed = Signal(bool,str)
    finished = Signal()

    def setlista(self,lista):
        self.lista = lista

    def run(self):
        self.started.emit()
        for way_file , file in self.lista:
            try:
                audio = eyed3.load(way_file)
                if not audio.tag:
                    audio.initTag()
                audio.tag.title = file.replace(".mp3","")
                audio.tag.save(version=(2,3,0))
                self.progressed.emit(True,f"{file}")
            except Exception as erro:
                self.progressed.emit(False,f"{file}")
                with open("mp3organizer.log","a") as logfile:
                    logfile.write(f"O arquivo {file} Apresentou o erro: \n \
                                  {erro} \n\n")
        self.finished.emit()

