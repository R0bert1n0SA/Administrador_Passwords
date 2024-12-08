

import sys
from PyQt5.QtWidgets import QApplication,QListWidget, QWidget, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtCore import pyqtSignal
from Interior.Configuraciones.config_app import *

class Almacenamiento(QFrame):
    signal = pyqtSignal()#señal para ctivar la ventana de crear
    def __init__(self): 
        super().__init__()
        self.InicializarUi()
        self.ConfigUi()

    def InicializarUi(self):
        self.setWindowTitle("SecurityBox")
        self.setFixedSize(303,680)
        self.setStyleSheet("""
            QWidget {
                background-color: gray;
            }
        """)
    
    def ConfigUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.Almacenamiento_interfaz()

    def Almacenamiento_interfaz(self):
        self.list = QListWidget()
        self.list.setFixedWidth(300)
        self.list.setStyleSheet('''
            QListWidget{
                background: white;
            }
        ''')

        plus = QPushButton("")
        plus.setObjectName("agregar")
        plus.setIcon(QIcon('img/plus.png')) 
        Button_config2(plus,250,36,'e')
        plus.clicked.connect(self.enviar)
        contG=QGroupBox("")
        cont=QGroupBox("")
        contenedor_general(plus,cont,contG,self.list)
        self.layout.addWidget(contG)

    def enviar(self):
        # Emitir la señal  al presionar el botón "plus"
        self.signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Almacenamiento()
    main_window.show()
    sys.exit(app.exec_())

