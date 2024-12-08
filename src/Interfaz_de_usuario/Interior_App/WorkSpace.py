import sys
from PyQt5.QtWidgets import QStackedWidget,QListWidget,QAction,QMenuBar,QSpacerItem,QSizePolicy ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout
from PyQt5.QtCore import Qt,QSize,pyqtSignal,QFile,QTextStream,QTimer
from PyQt5.QtGui import QFont,QIcon,QPixmap,QCursor
from .Crear_elemento import *
from .Editar import *



class Workspace(QWidget):
    aniadir=pyqtSignal(str)
    borrar=pyqtSignal(str)
    dato =pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.crear = Crear_Pestania()
        self.editar= Editar()
        self.InicializarUi()
        self.ConfigUI()


    def InicializarUi(self):
        self.setWindowTitle("SecurityBox")
        self.setFixedSize(500,670)   
        self.setStyleSheet("""
            QWidget {
                background-color: #505457 ;
            }
        """)


    def ConfigUI(self):
        self.Contenedor_G=QFrame()
        self.Layout = QVBoxLayout(self)
        self.Plantilla=QVBoxLayout(self.Contenedor_G)
        self.Plantilla.setContentsMargins(0,0,0,0)
        self.Layout.setContentsMargins(0,0,0,0)
        self.Contenedor_G.setFrameShape(QFrame.StyledPanel)
        self.Contenedor_G.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.principal()
        self.Layout.addWidget(self.Contenedor_G)


    def AjustesBoton(self,boton,flag):
        if flag==1:
            boton.setIcon(QIcon('img/guardar.png')) 
        else:
            boton.setIcon(QIcon('img/cancel.png'))
        boton.setFixedWidth(50)
        boton.setFixedHeight(50)
        boton.setIconSize(boton.size()) 
        boton.setStyleSheet("""       
            QPushButton {
                border:1px solid gray;
                background:#39373B  ;
            }
            QPushButton:hover {
                border:2px solid black;
                background:#282629   ;
            }            
        """)


    def CargaBarra(self,cont, boton1,boton2):
        Plantilla= QHBoxLayout(cont)
        Plantilla.setContentsMargins(1,0,1,0)
        Plantilla.addWidget(boton1)
        Plantilla.setSpacing(570)
        Plantilla.addWidget(boton2)
        cont.setFixedHeight(70)
        cont.hide()


    def principal (self):
        self.Contenido= QStackedWidget()
        self.barraInf = QFrame()
        image_label   = QLabel(self)
        guardar       = QPushButton()
        cancel        = QPushButton()     
        self.actual=image_label
        self.AjustesBoton(guardar,1)
        self.AjustesBoton(cancel,2)
        self.CargaBarra(self.barraInf,guardar,cancel)
        self.Contenido.setContentsMargins(0,0,0,0)
        image_label.setPixmap(QPixmap('img/Workspace_Logo.png'))
        image_label.setScaledContents(True)  
        self.Contenido.addWidget(image_label)
        self.Contenido.addWidget(self.crear)
        self.Contenido.addWidget(self.editar)
        self.Plantilla.addWidget(self.Contenido,Qt.AlignCenter)
        self.Plantilla.addWidget(self.barraInf,Qt.AlignBottom)
        self.crear.verificar.connect(self.Comprobacion)
        self.editar.verificar.connect(self.Comprobacion)
        cancel.clicked.connect(lambda : cerrar(self.actual,self.barraInf,image_label))
        cancel.clicked.connect(lambda : cerrar(self.actual,self.barraInf,image_label))

# funciones implementadas por la logica de negocio
    def mostrarcrear(self):
        if (self.actual != self.crear):
            self.actual.hide()
            self.Contenido.setCurrentWidget(self.crear)
            self.actual=self.crear
            self.barraInf.show()


    def mostrarEditar(self):
        if (self.actual != self.editar):
            self.actual.hide()
            self.Contenido.setCurrentWidget(self.editar)
            self.actual=self.editar 
            self.barraInf.show()


    def Comprobacion(self,contra):
        self.dato.emit(contra)




    def aniadirE(self,fol):
        self.crear.aniadir(fol)
    #


    def editE(self ,actual,nue):
        self.crear.edit(actual,nue)
    

    def eliminarE(self,fol):
        self.crear.eliminar(fol)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Workspace()
    window.show()
    sys.exit(app.exec_())