import sys
from PyQt5.QtWidgets import QGroupBox,QAction,QMenuBar,QSpacerItem,QSizePolicy ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout
from PyQt5.QtCore import Qt,QSize,pyqtSignal,QFile,QTextStream
from PyQt5.QtGui import QFont,QIcon,QPixmap
from Interfaz_de_usuario.Logica_de_negocio.LogicaNegocioInteriorAPP import LogicaNegocioInterior

class Interior_app(QWidget,LogicaNegocioInterior):
    #login_button_clicked = pyqtSignal()
    creacion              = pyqtSignal()
#Constructor y config
    def __init__(self): 
        super().__init__()
        self.zonaT.setStyleSheet("""QFrame{border:1px solid cyan;}""")
        self.SeccionG              =QFrame()
        self.Inicializar()
        self.config()


    def Inicializar(self):
        self.setWindowTitle("SecurityBox")
        self.setGeometry(100, 100, 1200, 600)
        self.showMaximized()
        self.setMinimumSize(1000, 570)  # Establecer tamaño mínimo
        self.setMaximumSize(1600, 1200)  # Establecer tamaño máximo     
        self.setStyleSheet("""
            QWidget {
                background-color: #505457 ;
            }
        """)


    def config(self):
        self.Contenedor_G=QFrame()
        self.Layout = QVBoxLayout(self)
        self.Plantilla=QVBoxLayout(self.Contenedor_G)
        self.Plantilla.setContentsMargins(0,0,0,0)
        self.Plantilla.setStretch(2,2)
        self.Layout.setContentsMargins(0,0,0,0)
        self.Contenedor_G.setFrameShape(QFrame.StyledPanel)
        self.Contenedor_G.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Layout.addWidget(self.Contenedor_G)
        self.Principal()
#------------------------------------------------------------------------------------




#Config Visual
    def Ajustes (self,elem):
        elem.setFixedHeight(70)


    def AjustesS(self,Seccion,a):
        Seccion.setFixedWidth(a)


    def AjustesWidgetsMax(self,a,b,c,d):
        self.Usuario.setFixedWidth(a)
        self.Usuario.setFixedHeight(b)
        self.almacenamiento_window.setFixedWidth(c)
        self.almacenamiento_window.setFixedHeight(b)
        self.zonaT.setFixedWidth(d)


    def AjustesWidgetsMin(self,a,b,c,d):
        self.Usuario.setFixedWidth(a)
        self.Usuario.setFixedHeight(b)
        self.almacenamiento_window.setFixedWidth(a)
        self.almacenamiento_window.setFixedHeight(c)
        self.zonaT.setFixedWidth(d)


    def Seccion(self,s2,elemento):
        Plantilla=QVBoxLayout(s2)
        Plantilla.setContentsMargins(1,0,0,0)
        Plantilla.addWidget(elemento,Qt.AlignTop|Qt.AlignCenter)
#---------------------------------------------------------------------------------------------------
#Funciones Principales

    def AjustesBarra_busqueda(self,Barra_busqueda): 
    #Diseña la seccion de la barra de busqueda
        Barra_busqueda.setPlaceholderText("Buscar...")
        Barra_busqueda.setFixedHeight(40)
        Barra_busqueda.setFixedWidth(300)
        Barra_busqueda.setStyleSheet("""
                QLineEdit{
                    background:#4077D3;
                    font-size: 15px;
                    font-family: Arial;
                    font-Weight: bolder;
                    color: solid Black;
                    border: 2px solid white;
                    border-radius: 10px;
                    Padding: 5px;
                }""")


    def Superior(self,Bar,contenedor):
        Plantilla=QHBoxLayout(contenedor)
        Plantilla.addWidget(Bar,Qt.AlignTop|Qt.AlignCenter)


    def Principal(self):
        espaciador =QSpacerItem(0,0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        superior   =QFrame()
        Seccion1   =QFrame()
        Seccion2   =QFrame()
        Seccion3   =QFrame()
        Plantilla  =QHBoxLayout(self.SeccionG)
        Barra_busqueda = QLineEdit(self)
        

    #configuracion visual
        self.Ajustes(superior)
        self.AjustesBarra_busqueda(Barra_busqueda)
    #configuracion interna
        self.Superior(Barra_busqueda,superior)
        self.Seccion(Seccion1,self.Usuario)
        self.Seccion(Seccion2,self.almacenamiento_window)
        self.Seccion(Seccion3,self.zonaT)


        Plantilla.setContentsMargins(0,0,0,0)
        Plantilla.addWidget(Seccion1)
        Plantilla.addWidget(Seccion2)
        Plantilla.addWidget(Seccion3)
        Plantilla.addItem(espaciador)

        self.almacenamiento_window.Crear.connect(self.Enviar)
        self.Plantilla.addWidget(superior)
        self.Plantilla.setSpacing(0)
        self.Plantilla.addWidget(self.SeccionG)


    def resizeEvent(self, event):
    # Detecta el cambio de tamaño de la ventana
        new_size = event.size()
        if new_size.width() > 1200 or new_size.height() > 600:
            self.AjustesWidgetsMax(270,670,300,690)
            self.AjustesS(self.SeccionG,1598)
        else:
            self.AjustesWidgetsMin(300,520,525,540)
            self.AjustesS(self.SeccionG,1510)


    def Enviar(self):
        self.creacion.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Interior_app()
    main_window.show()
    sys.exit(app.exec_())
