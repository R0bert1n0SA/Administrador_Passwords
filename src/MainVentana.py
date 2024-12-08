import sys
from PyQt5.QtWidgets import QGroupBox,QAction,QMenuBar,QSpacerItem,QSizePolicy ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout,QStackedWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon,QPixmap
from Interfaz_de_usuario.Logica_de_negocio.LogicaNegocio import LogicaNegocio



class Gestor_UI(QMainWindow,LogicaNegocio):
    def __init__(self): 
        super().__init__()
        self.Inicializar()
        self.config()


    def Inicializar(self):
        self.setWindowTitle("SecurityBox")
        icono = QIcon("img/Logo.png")
        self.setWindowIcon(icono)
        self.setGeometry(100, 100, 1200, 600)
        self.showMaximized()
        self.setMinimumSize(1000, 500)  # Establecer tamaño mínimo
        self.setMaximumSize(1600, 1200)  # Establecer tamaño máximo     


    def config(self):
        self.Contenido=QStackedWidget()
        self.setCentralWidget(self.Contenido)
        self.Contenido.addWidget(self.Acceso)
        self.Acceso.signup.connect(lambda: self.mostrar_aplicacion(self.Acceso,self.Registrar))
        self.Acceso.recuperacion.connect(lambda: self.mostrar_aplicacion(self.Acceso,self.RecuperarCount))
        self.Contenido.addWidget(self.Registrar)
        self.Registrar.Login.connect(lambda : self.mostrar_aplicacion(self.Registrar,self.Acceso))
        self.Contenido.addWidget(self.Interior)
        self.Contenido.addWidget(self.RecuperarCount)
        self.RecuperarCount.Login.connect(lambda : self.mostrar_aplicacion(self.RecuperarCount,self.Acceso))


    def mostrar_aplicacion(self,anterior,actual):
        anterior.hide()
        self.Contenido.setCurrentWidget(actual)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Gestor_UI()
    main_window.show()
    sys.exit(app.exec_())
