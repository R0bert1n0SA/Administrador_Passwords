
import sys
from PyQt5.QtWidgets import QSizePolicy,QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QIcon,QPixmap
from Funciones_Generales import *

class Recuperar (QWidget):

    Login =pyqtSignal()
    def __init__(self):
        super().__init__()
        Inicializar(self)
        Config(self)
        Titulo(self)
        self.Seccion()


# Ajustes
    def Ajustes(self, cont):
        cont  .setStyleSheet("""
            QFrame{
                background: black; 
                border: 2px solid blue;
            }""")
        cont.setFixedSize(600 ,300)


    def Ajustes_Visuales_CSS(self,Titulo, Descrip,ingreso):
        Titulo.setStyleSheet("""
            QLabel{
                border:none;
                color:white;
                font-size: 20px;
                font-weight: bolder;
                Padding:7px;
            }""")
        Descrip.setStyleSheet("""
            QLabel{
                border:none;
                color:white;
                font-size: 15px;
                Padding:7px;             
            }""")
        ingreso.setStyleSheet("""
            QLineEdit{
                font-size: 10px;
                border: 1px solid #fff;
                color : white;
                Padding: 7px;
                Margin-left : 10px;
            }""")
        Descrip.setText("Introduce correo electrónico o número de móvil para buscar tu cuenta y restablecer contraseña")
        Descrip.setWordWrap(True)
        ingreso.setFixedHeight(30)
        ingreso.setFixedWidth(400)
        ingreso.setPlaceholderText("Correo Electronico o Numero de Movil")


    def botonesconfig(self,buton):
        buton.setFixedWidth(100)
        buton.setFixedHeight(30)
        buton.setStyleSheet("""
            QPushButton {
                background-color :#1056CC;
                height:20px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color :#163870;            
                border: 2px solid white;
            }
        """)

#--------------------------------------------------------------------------------------------------------------
#Carga Contenedores
    def Config_Recu(self,Titulo, Descrip,ingreso,Cont):
        Plantilla = QVBoxLayout(Cont)
        self.Ajustes_Visuales_CSS(Titulo,Descrip,ingreso)
        Plantilla.addWidget(Titulo)
        Plantilla.addWidget(Descrip,1,Qt.AlignTop)
        Plantilla.addWidget(ingreso)
        Cont.setFixedSize(560 ,180)
        Cont.setStyleSheet("""QFrame{border:none;}""")


    def Contenedor_botones(self,Cancelar,Enviar,Cont):
        Plantilla= QHBoxLayout(Cont)
        Plantilla.addWidget(Cancelar)
        Plantilla.addWidget(Enviar)
        Cont.setFixedSize(320 ,70)
        Cont.setStyleSheet("""QFrame{border:none;}""")

#--------------------------------------------------------------------------------------------------------------

    def Seccion (self):
    #Contenedores y Diseños
        Interactive_UI      =QFrame()
        Recuperar_Cont      =QFrame()
        Botones             =QFrame()
        Plantilla           =QVBoxLayout(Interactive_UI)
        Titulo              =QLabel("Recuperacion de Cuenta")
        Descripcion         =QLabel()
        Ingreso             =QLineEdit()
        Cancelar            =QPushButton("Cancelar")
        Enviar              =QPushButton("Enviar")
    # Ajustes Visuales
        self.Ajustes(Interactive_UI)
        self.botonesconfig(Cancelar)
        self.botonesconfig(Enviar)
    # Carga de los Contenedores
        self.Config_Recu(Titulo,Descripcion,Ingreso,Recuperar_Cont)
        self.Contenedor_botones(Cancelar,Enviar,Botones)
        Plantilla.addWidget(Recuperar_Cont,1,Qt.AlignTop)
        Plantilla.addWidget(Botones,3,Qt.AlignRight)
    #Llamadas a Funciones 
        Cancelar.clicked.connect(self.Cancelar_Click)
        self.Plantilla.addWidget(Interactive_UI,1,Qt.AlignCenter)


    def Cancelar_Click(self):
        self.Login.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Recuperar()
    main_window.show()
    sys.exit(app.exec_())
