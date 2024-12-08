import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialogButtonBox,QItemDelegate,QListView,QDialog,QAction,QMenuBar,QSpacerItem,QSizePolicy ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout,QListWidgetItem
from PyQt5.QtCore import QAbstractListModel, QObject,Qt,QSize,pyqtSignal,QFile,QTextStream,QTimer
from PyQt5.QtGui import QFont,QIcon,QPixmap,QCursor,QPainter
from Funciones_Generales import * 

class FolderDialog(QDialog):
    def __init__(self, folder):
        super().__init__()
        self.folder = folder
        self.setWindowTitle("Folder Details")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        self.name_edit.setText(self.folder.name)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_edit)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)




class Organizacion_datos(QWidget):
    aniadir=pyqtSignal(QListView)
    click =pyqtSignal(QListView)
    actualizar_nombre=pyqtSignal(QListView,QListWidgetItem,int)
    borrar=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.InicializarUi()
        self.ConfigUI()


    def InicializarUi(self):
        self.setWindowTitle("SecurityBox")
        self.setStyleSheet("""
            QWidget {
                background-color: #505457 ;
            }
        """)


    def ConfigUI(self):
        self.Contenedor_G=QFrame()
        self.Layout = QVBoxLayout(self)
        self.Plantilla=QVBoxLayout(self.Contenedor_G)
        self.Layout.setContentsMargins(0,0,0,0)
        self.Contenedor_G.setFrameShape(QFrame.StyledPanel)
        self.Contenedor_G.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Layout.addWidget(self.Contenedor_G)
        self.Principal()
        self.TimerCursor()


#-------------------------------------------------------------------------------------------------------
#Ajustes visuales
    def AjustesLabels(self,elem):
        elem.setStyleSheet("""QLabel{color: white;}""")


    def botones(self,button):
        button.setFixedWidth(24)
        button.setFixedHeight(34)
        button.setIconSize(button.size()) 
        button.setStyleSheet("""
            QPushButton {
                background-color :transparent;
                font-size: 18px;
            }
        """)


    def AjustesbotonesSuperior(self,button,button2):
        button.setIcon(QIcon('img/technology.png'))#Le asigno un icono
        button2.setIcon(QIcon('img/Star.png'))#Le asigno un icono
        self.botones(button)
        self.botones(button2) 


    def AjustesbotonesInferior(self,button,button2):
        button.setIcon(QIcon('img/arrow.png'))
        button2.setIcon(QIcon('img/addition-button.png'))
        self.botones(button)
        self.botones(button2) 


    def  AjustesLista (self): 
        self.list.setViewMode(QListView.ListMode)
        self.list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list.setResizeMode(QListView.Adjust)
        self.list.setFixedHeight(400)
        self.list.hide()
#----------------------------------------------------------------------




#Contenedores
    def Contenedor(self,elem,icon,conte):
        Plantilla=QHBoxLayout(conte)
        Plantilla.setContentsMargins(0,0,0,0)
        Plantilla.addWidget(icon)
        Plantilla.addWidget(elem)


    def ContenedorEtiq(self,cont1,cont2,cont3):
        Plantilla=QVBoxLayout(cont3)
        Plantilla.setContentsMargins(0,0,0,0)
        Plantilla.addWidget(cont1)
        Plantilla.addWidget(cont2)


    def encabezado(self,carpeta,mostrarcar,Crear,cont):
        Plantilla=QHBoxLayout(cont)
        Plantilla.addWidget(mostrarcar)
        Plantilla.addWidget(carpeta)
        Plantilla.addWidget(Crear)


    def Carpetas(self,contEncabezado,espaciador,list,Contenedor):
        Plantilla=QVBoxLayout(Contenedor)
        Plantilla.setContentsMargins(0,0,0,90)
        Plantilla.addWidget(contEncabezado)
        Plantilla.addItem(espaciador)
        Plantilla.addWidget(list)
#-------------------------------------------------------------




#Ajustes Funcionales Visuales
    def cursor_sobre_areas(self,cursor_pos):
        sobre_favoritos = self.Favorit.rect().contains(self.Favorit.mapFromGlobal(cursor_pos))
        sobre_elementos = self.Todos_elem.rect().contains(self.Todos_elem.mapFromGlobal(cursor_pos))
        return sobre_favoritos, sobre_elementos


    def cambiar_icono_elementos(self, sobre_elementos):
        if sobre_elementos:
            self.iconTodos.setIcon(QIcon('img/technology blue.png'))
        else:
            self.iconTodos.setIcon(QIcon('img/technology.png'))


    def cambiar_icono_favoritos(self, sobre_favoritos):
        if sobre_favoritos:
            self.iconFav.setIcon(QIcon('img/Star blue.png'))
        else:
            self.iconFav.setIcon(QIcon('img/Star.png'))


    def Verificar_cursor(self):
        cursor_pos = QCursor.pos()
        sobre_favoritos, sobre_elementos = self.cursor_sobre_areas(cursor_pos)
        if self.selected_label:
            if self.selected_label == self.Todos_elem:
                self.cambiar_icono_favoritos(sobre_favoritos)
            elif self.selected_label == self.Favorit:
                self.cambiar_icono_elementos(sobre_elementos)
        else:
            self.cambiar_icono_elementos(sobre_elementos)
            self.cambiar_icono_favoritos(sobre_favoritos)


    def TimerCursor(self):
        temporizador = QTimer(self)
        temporizador.timeout.connect(self.Verificar_cursor)
        temporizador.start(100)


    def cambio(self,icon,e ):
        #Funcion que alterna la lista carpetas ver o no
        if(self.ant2==0):
            icon.setIcon(QIcon('img/arrow-down.png'))
            self.ant2=1
            self.list.show()#muestro la lista
        elif(self.ant2==1):
            icon.setIcon(QIcon('img/arrow.png'))
            self.ant2=0
            self.list.hide()#oculto la lista


    def Accion(self,elem,s,icon):
        # Función que se activa cuando se presiona el QLabel
        # Desactivar el QLabel previamente seleccionado
        if self.selected_label:
            font = self.selected_label.font()
            font.setWeight(QFont.Normal)
            self.selected_label.setStyleSheet('''
            QLabel{
                color: white;
            }
            QLabel:hover {
                color:#001385;
            }
            ''')
            if(self.ant==2):
                icon.setIcon(QIcon('img/technology.png'))
            elif(self.ant==1):
                icon.setIcon(QIcon('img/Star.png'))
            self.selected_label.setFont(font)
        # Activar el QLabel seleccionado actualmente
        font = elem.font()
        font.setWeight(QFont.Bold)
        if(s==1):
            icon.setIcon(QIcon('img/technology blue.png'))
            self.ant=1
        else:
            icon.setIcon(QIcon('img/Star blue.png'))
            self.ant=2
        elem.setFont(font)
        elem.setStyleSheet('''
            QLabel{
                color:#001385
            }
        ''')
        # Almacenar el QLabel seleccionado actualmente
        self.selected_label = elem
#----------------------------------------------------------------------



#Secciones
    def Seccion_Superior(self,ContenedorEtiq):
        ContenedorTodos =QFrame()
        ContenedorFav   =QFrame()
        self.Todos_elem =QLabel("Todos los Elementos ")
        self.Favorit    =QLabel("Favoritos")
        self.iconTodos  =QPushButton()
        self.iconFav    =QPushButton()
    #Ajustes de Elementos
        self.AjustesbotonesSuperior(self.iconTodos,self.iconFav)
        self.AjustesLabels(self.Favorit)
        self.AjustesLabels(self.Todos_elem)
    #Contenedores configurados
        self.Contenedor(self.Todos_elem,self.iconTodos,ContenedorTodos)
        self.Contenedor(self.Favorit,self.iconFav,ContenedorFav)
        self.ContenedorEtiq(ContenedorTodos,ContenedorFav,ContenedorEtiq)
        self.selected_label = None  #variable  de instancia usada como flag para saber el icono activo
        self.ant=int(-1)            #variable de uso tipo flag para llevar un registro de qué QLabel estaba  
#                                   seleccionado "Todos los Elementos" 1 "Favoritos" 2
        self.text=None              #variable Encargada de almacenar nombre modificado y 
#                                    usada para actualizar
        self.actual=None            #variable Encargada de almacenar el nombre actua
#                                    de la carpeta con cada modificacion 
        self.Todos_elem.mousePressEvent=lambda event:self.Accion(self.Todos_elem,1,self.iconTodos)
        self.Favorit.mousePressEvent=lambda event:self.Accion(self.Favorit,2,self.iconFav)


    def Seccion_Inferior(self,Contenedor):
        carpeta        =QLabel("Carpetas")
        mostrarcar     =QPushButton()
        Crear          =QPushButton() 
        self.ultimoitem=None          
        self.list      =QListView(self)
        espaciador     =QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        contEncabezado =QFrame()
        self.ant2=0                 #variable de uso tipo flag para saber el icono activo
        # Ajustes Visuales
        self.AjustesLista()
        self.AjustesbotonesInferior(mostrarcar,Crear)
        #---------------------------------------------------
        self.encabezado(carpeta,mostrarcar,Crear,contEncabezado)
        self.Carpetas(contEncabezado,espaciador,self.list,Contenedor)

        mostrarcar.mousePressEvent=lambda event:self.cambio(mostrarcar,espaciador)




#------------------------------------------------------------------------------------------------------
    def Principal(self):
        ContenedorOpciones  =QFrame()
        ContenedorCarpetas  =QFrame()
        self.Seccion_Superior(ContenedorOpciones)
        self.Seccion_Inferior(ContenedorCarpetas)
        self.Plantilla.addWidget(ContenedorOpciones)
        self.Plantilla.addWidget(ContenedorCarpetas)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Organizacion_datos()
    window.show()
    sys.exit(app.exec_())

