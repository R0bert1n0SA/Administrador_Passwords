import sys
from PyQt5.QtWidgets import QAbstractItemView,QListWidget,QGroupBox,QAction,QMenuBar,QSpacerItem,QSizePolicy,QListWidgetItem ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout
from PyQt5.QtCore import Qt,QSize,pyqtSignal,QFile,QTextStream
from PyQt5.QtGui import QFont,QIcon,QPixmap
from PyQt5.QtCore import pyqtSignal

class Almacenamiento(QFrame):
    Crear    = pyqtSignal()
    Editar   = pyqtSignal()
    def __init__(self): 
        super().__init__()
        self.InicializarUi()
        self.ConfigUi()


    def InicializarUi(self):
        self.setWindowTitle("SecurityBox")
        self.setFixedSize(290,650)   
        self.setStyleSheet("""
            QWidget {
                background-color: gray;
            }
        """)


    def ConfigUi(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.Almacenamiento_interfaz()


    def AjustesLista(self,list, plus):
        list.setFixedWidth(300)
        list.setFocusPolicy(Qt.NoFocus)
        list.setStyleSheet('''
            QListWidget{
                background: #253248;
            }               
            QListWidget::item{
                background: transparent; 
                opacity: 1;            
            }
            QListWidget::item:selected{
                background:rgba(100, 100, 200, 0.5);       
                border-left: 5px solid blue;
                Padding:0px;
            }       
        ''')


    def AjustesBoton(self,plus):
        plus.setObjectName("agregar")
        plus.setIcon(QIcon('img/plus.png')) 
        plus.setIconSize(plus.size())  # Ajusta el tamaño del ícono al tamaño del botón
        plus.setFixedWidth(250)
        plus.setFixedHeight(36)
        plus.setStyleSheet("""
            QPushButton {
                background:blue;
                border-radius: 5px;
                height:40px;
                border: 1px solid gray;
            }
            QPushButton:hover {
                background:red;
                border: 1px solid black;
            }
        """) 


    def Fuentes(self,font,size,negrita):
        font.setPointSize(size)
        if(negrita == 0):
            font.setBold(True)


    def contenedor(self,plus,cont,contG,list):
        Plantilla=QVBoxLayout()
        Plantilla.setAlignment(Qt.AlignBottom)  # Alinear al inicio
        Plantilla.setContentsMargins(0,0,0,0)
        self.contenedor_boton(plus,cont)
        Plantilla.addWidget(list)
        Plantilla.addWidget(cont)
        contG.setLayout(Plantilla)


    def contenedor_boton(self,buton,cont):
        Layout=QHBoxLayout()
        Layout.setContentsMargins(0,0,0,0)
        Layout.addWidget(buton)
        cont.setLayout(Layout)
        cont.setFixedWidth(300)
        cont.setFixedHeight(60)





    def Almacenamiento_interfaz(self):
        self.list = QListWidget()
        plus      = QPushButton("")
        self.itemactual = None
        #self.Barraseleccionado.hide()
        self.AgregarElementos()
    #Contenedores
        contG=QFrame()
        cont=QFrame()
    #Ajustes visuales
        self.AjustesLista(self.list,plus)
        self.AjustesBoton(plus)
        self.contenedor(plus,cont,contG,self.list)
        self.list.itemClicked.connect(self.edicion)
        plus.clicked.connect(self.crear)
        self.layout.addWidget(contG)


    def ElementoCarga(self,contenedor,sitio,usuario,elemento):
        Plantilla = QVBoxLayout(contenedor)
        Plantilla.addWidget(sitio)
        Plantilla.addWidget(usuario)
        contenedor.setStyleSheet("""QWidget{background:transparent;border:none;}""")
        elemento.setIcon(QIcon("img/star blue.png"))
        elemento.setSizeHint(contenedor.sizeHint())


    def CargarLista(self,a):
        nombre_usuario = "Nombre de usuario"
        font_sitio   = QFont()        
        font_usuario = QFont()
        sitio        = QLabel(a)
        usuario      = QLabel(nombre_usuario)
        contenedor   = QFrame()
        elemento     = QListWidgetItem()

        self.Fuentes(font_sitio,8,0)
        self.Fuentes(font_usuario,8,1)
        sitio.setFont(font_sitio)
        usuario.setFont(font_usuario)        
        self.ElementoCarga(contenedor,sitio,usuario,elemento)
        self.list.addItem(elemento)
        self.list.setItemWidget(elemento, contenedor)


    def crear(self):
        self.Crear.emit()




    def edicion(self):
        self.Editar.emit()


    def AgregarElementos(self):
        a="Google"
        b="Gmail"
        c="tumbler"
        self.CargarLista(a)
        self.CargarLista(b)
        self.CargarLista(c)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Almacenamiento()
    main_window.show()
    sys.exit(app.exec_())