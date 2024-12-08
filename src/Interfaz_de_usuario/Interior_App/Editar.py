import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QAbstractItemView,QListWidget,QGroupBox,QCheckBox,QAction,QComboBox,QMenuBar,QSpacerItem,QSizePolicy,QListWidgetItem ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout
from PyQt5.QtCore import Qt,QSize,pyqtSignal,QFile,QTextStream
from PyQt5.QtGui import QFont,QIcon,QPixmap
from PyQt5.QtCore import pyqtSignal
from Funciones_Generales import *

class Editar(QWidget):
    verificar=pyqtSignal(str)
    generador=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.InicializarUi()
        self.ConfigUi()


    def InicializarUi(self):
        self.setWindowTitle("SecurityBox") 
        self.setFixedSize(690,600) 
        self.setStyleSheet("""
            QWidget {
                background:#253248;
            }
        """)


    def ConfigUi(self): 
        self.Contenedor_G=QFrame()
        self.Layout = QVBoxLayout(self)
        self.Plantilla=QVBoxLayout(self.Contenedor_G)
        self.Plantilla.setContentsMargins(145,20,145,0)
        self.Layout.setContentsMargins(0,0,0,0)
        self.Contenedor_G.setFrameShape(QFrame.StyledPanel)
        self.Contenedor_G.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Layout.addWidget(self.Contenedor_G)
        self.Principal()
        self.Inferior()


    def AjustesTitulo(self,Crear):
        Crear.setAlignment(Qt.AlignLeft)
        Crear.setStyleSheet('''
            color:white;
            font-size:17px;
        ''')


    def AjustesContenedorPrincipal(self,cont):
        cont.setStyleSheet("""
            QFrame{
                background: #7A7E85;
                border:none;
            }                              
        """)


    def AjustesContenedoresInternos(self,cont):
        cont.setStyleSheet("""
            QFrame{
                background: #7A7E85;
                border: 1px solid black;        
                margin: 0px;
                padding: 0px;          
            }                
            QFrame:hover {
                background:green;         
            }                
            QLabel{
                background: transparent;
                border:none;
                font-size:15px;
                font-weight: bolder;
                color:black; 
                font-family:"Arial";
            }
            QLineEdit{
                background: transparent;  
                border:none;
                font-size:10px;           
                border-bottom :1px solid blue;       
                color: white;
                font-size: 12pt;
            }
        """)


    def Ajustes_Boton(self,boton,num):
        if(num == 1):
            boton.setIcon(QIcon('img/verificar.png')) 
        if(num == 2):
            boton.setIcon(QIcon('img/ojo-tachado.png'))
        if(num == 3 ):
            boton.setIcon(QIcon('img/technology.png'))
        boton.setFixedWidth(20)
        boton.setFixedHeight(20)
        boton.setIconSize(boton.size()) 
        boton.setStyleSheet("""
                QPushButton {
                    border:none;
                    background:transparent 
                }            
            """)


    def CargaContenedorPrincipal(self,Datos,Nombre,Usuario,Password):
        Plantilla= QVBoxLayout(Datos)
        Plantilla.setContentsMargins(0,0,0,7)
        Plantilla.addWidget(Nombre)
        Plantilla.addWidget(Usuario)
        Plantilla.addWidget(Password)
        Datos.setFixedHeight(210)


    def CargaContenedor(self,Datos,dato1,dato2,tam):
        Plantilla= QVBoxLayout(Datos)
        Plantilla.setContentsMargins(9,10,9,10)
        Plantilla.addWidget(dato1,1,Qt.AlignTop)
        Plantilla.addWidget(dato2,Qt.AlignTop)
        Datos.setFixedHeight(tam)
        Datos.setFixedWidth(398)


    def Cargar_Input_password(self,Inpass,Input,boton1, boton2, boton3):
        Input.setFixedWidth(220)
        Inpass.setStyleSheet("""
            QFrame{
                background: transparent;
                border: none;        
                margin: 0px;
                padding: 0px;          
            }                
            QFrame:hover {
                background:green;         
            }                
        """) 
        Plantilla= QHBoxLayout(Inpass)
        Plantilla.setContentsMargins(0,0,0,0)
        Plantilla.addWidget(Input,1,Qt.AlignTop)
        Plantilla.addWidget(boton1,Qt.AlignTop)
        Plantilla.addWidget(boton2,Qt.AlignTop)
        Plantilla.addWidget(boton3,Qt.AlignTop)


    def contenedorfavo(self,parametro1,parametro2,cont):
        layout=QHBoxLayout()
        layout.addWidget(parametro1,9,Qt.AlignLeft)
        layout.addWidget(parametro2,Qt.AlignRight)
        cont.setLayout(layout)
        cont.setFixedHeight(50)
        cont.setStyleSheet('''
            QCheckBox{
                background:#7A7E85;
            }
            QLabel{
                font-weight: bold;
                font-size: 12px;
                font-family:'Arial';
            }
        ''')


    def contenedorcarpetasfav(self,parametro1,parametro2,cont):
        Plantilla=QVBoxLayout(cont)
        Plantilla.setContentsMargins(0,0,0,0)
        Plantilla.addWidget(parametro1,3)
        Plantilla.addWidget(parametro2,1,Qt.AlignTop)
        cont.setFixedHeight(70)
        cont.setStyleSheet('''
            QGroupBox{
                border:none;
                background:#7A7E85;
            }

        ''')


    def Principal(self):
        Crear         =QLabel("Editar Elemento")
        Datos         =QFrame()
        Nombre        =QFrame()
        Usuario       =QFrame()
        Password      =QFrame()
        IPassword_Cont=QFrame()
        nombre        =QLabel("Nombre")
        usuario       =QLabel("Usuario")
        password      =QLabel("Password")
        self.Inombre  =QLineEdit()
        self.Iusuario =QLineEdit()
        self.Ipassword=QLineEdit()
        boton         =QPushButton()
        boton2        =QPushButton()
        boton3        =QPushButton()
        self.Ipassword.setEchoMode(QLineEdit.Password)
    #Estilizando elementos
        self.AjustesTitulo(Crear)
        self.Ajustes_Boton(boton,1)
        self.Ajustes_Boton(boton2,2)
        self.Ajustes_Boton(boton3,3)
        self.AjustesContenedoresInternos(Nombre)
        self.AjustesContenedoresInternos(Password)
        self.AjustesContenedoresInternos(Usuario)
        self.AjustesContenedorPrincipal(Datos)
        self.AjustesContenedoresInternos(IPassword_Cont)
    #Armando los contenedores
        self.CargaContenedor(Nombre,nombre,self.Inombre,70)
        self.CargaContenedor(Usuario,usuario,self.Iusuario,70)
        self.Cargar_Input_password(IPassword_Cont,self.Ipassword,boton,boton2,boton3)
        self.CargaContenedor(Password,password,IPassword_Cont,70)
        self.CargaContenedorPrincipal(Datos,Nombre,Usuario,Password)
        
    #------------------------------------------------------------------
        boton.clicked.connect(lambda:self.Comprometida(self.Ipassword.text()))
        boton2.clicked.connect( lambda :toggle_visibility(self.Ipassword,boton2))
        ''' 
        self.generador.clicked.connect(self.enviar)
        '''
        self.Plantilla.addWidget(Crear)
        self.Plantilla.addWidget(Datos,1,Qt.AlignTop)


    def Inferior(self):
        Carpeta       =QFrame()
        self.opciones =QComboBox()        
        self.Fav      =QLabel("Favorito")
        self.Favoritos= QCheckBox()          
        contfav       = QFrame()
        self.carpetass= QGroupBox('Carpetas')     
        
        self.opciones.addItem('Sin Carpeta')
        self.AjustesContenedorPrincipal(Carpeta)
        self.contenedorfavo(self.Fav,self.Favoritos,contfav)#Contenedor de Favoritos
        self.contenedorcarpetasfav(self.opciones,contfav,self.carpetass)#Contenedor de carpetas
        self.CargaContenedor(Carpeta,self.carpetass,contfav,160)
        self.Plantilla.addWidget(Carpeta,1,Qt.AlignTop)


    def Comprometida(self,Input):
        self.verificar.emit(Input)


    def aniadir(self,fol):
        self.opciones.addItem(fol)


    def edit(self,ind,nue):
        self.opciones.setItemText((ind+1),nue)
    


    def eliminar(self,fol):
        # Buscar el índice de la carpeta a eliminar en el QComboBox
        index = self.opciones.findText(fol)
        # Verificar si se encontró la carpeta
        if index != -1:
        # Eliminar la carpeta del QComboBox
            self.opciones.removeItem(index)
        # Seleccionar automáticamente la opción "Sin Carpeta"
            self.opciones.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Editar()
    main_window.show()
    sys.exit(app.exec_())