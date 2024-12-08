from PyQt5.QtWidgets import QSpacerItem,QInputDialog,QSizePolicy,QListWidgetItem ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout
from PyQt5.QtCore import Qt,QSize,pyqtSignal,QFile,QTextStream
from PyQt5.QtGui import QFont,QIcon,QPixmap


#Codigos de Pantalla Principal 
def Inicializar(self):
    self.setWindowTitle("SecurityBox")
    self.setGeometry(100, 100, 800, 600)
    self.showMaximized()
    self.setMinimumSize(800, 500)  # Establecer tamaño mínimo
    self.setMaximumSize(1600, 1200)  # Establecer tamaño máximo     
    self.setStyleSheet("""
        QWidget {
            background-color: #505457 ;
        }
    """)


def Config(self):
    self.Layout = QVBoxLayout(self)
    self.Layout.setContentsMargins(0,0,0,0)
    self.Contenedor_G=QFrame()
    self.Contenedor_G.setFrameShape(QFrame.StyledPanel)
    self.Contenedor_G.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.Plantilla=QVBoxLayout(self.Contenedor_G)
    self.Plantilla.setContentsMargins(0,0,0,80)
    self.Layout.addWidget(self.Contenedor_G)


def Titulo(self):
    self.Plantilla.addSpacing(70) 
    titulo = QLabel("SecurityBox")
    icono_label = QLabel()
    pixmap = QPixmap("img/Logo.png")  # Cargar el ícono desde un archivo
    icono_label.setPixmap(pixmap)
    encabezado=QFrame()
    encabezadop=QHBoxLayout(encabezado)
    titulo.setStyleSheet("""QLabel{                
                color: white;
                font-size: 55px;
                font-family: 'sans-serif';
                font-weight: bold;
        } 
        """)
        
    encabezadop.addWidget(icono_label)
    encabezadop.addWidget(titulo)
    encabezado.setFixedWidth(480)
    self.Plantilla.addWidget(encabezado,0,Qt.AlignTop|Qt.AlignCenter)


def estilos_CSS(Interactive_UI,flag):
    if(flag==1):
        Interactive_UI.setFixedSize(430,400)
        Interactive_UI.setStyleSheet("""
            QFrame{
                background-color: black;
            } 
            QLineEdit{
                color : white;
                outline: none;
                background:#8700FC;
                font-size: 15px;
                border: 2px solid white;
                border-radius: 6px;
                border-right: none;                
            }                    
        """)
    else:
        Interactive_UI.setFixedSize(500,300)
        Interactive_UI.setStyleSheet("""
            QFrame{
                background-color: black;
            }
            QLabel{
                color: white;
                font-size: 15px;
                font-family: 'sans-serif';
                font-weight: bold;                    
            } 
            QLineEdit{
                background:transparent;
                font-size: 15px;
                border: none;
                border-bottom: 1px solid #fff;
                border-left: 1px solid #fff;
                color : white;
                outline: none;
            }                       
        """)


def Ajustes (User_i,Interactive_UI,a,flag,flag2):   
    User_i.setFixedWidth(a)
    User_i.setFixedHeight(31)
    if (flag2 == 1):
        User_i.setPlaceholderText("Ingrese contraseña") 
        User_i.setEchoMode(QLineEdit.Password)
    else:
        User_i.setPlaceholderText("Ingrese su Email") 
    if (flag == 1):
        if(flag2 == 0):
            User_i.setStyleSheet("""QLineEdit{margin-left:35px;border-right:2px solid white;}""")
    estilos_CSS(Interactive_UI,flag)


def AjustesItems(Ver_Passw,flag,flag2):
    Ver_Passw.setIconSize(Ver_Passw.size())  # Ajusta el tamaño del ícono al tamaño del botón
    Ver_Passw.setFixedWidth(30)
    Ver_Passw.setFixedHeight(31)
    if (flag==1):
        Ver_Passw.setIcon(QIcon("img/user.png"))
    else:
        Ver_Passw.setIcon(QIcon('img/ojo-tachado.png'))
    
    if (flag2==1):
            Ver_Passw.setStyleSheet("""            
            QPushButton{
                background:#8700FC;
                border: 2px solid white;
                border-left: none;                 
            }
        """)


def botonesconfig(buton):
    buton.setFixedWidth(150)
    buton.setFixedHeight(40)
    buton.setStyleSheet("""    
        QPushButton {
            background-color :#723185;
            height:40px;
            font-size: 18px;
            border-radius: 20px; 
        }
        QPushButton:hover {
            border: 2px solid white;
        }
    """)











def toggle_visibility(password_input,button):
    if password_input.echoMode() == QLineEdit.Password:
        password_input.setEchoMode(QLineEdit.Normal)
        button.setIcon(QIcon('img/ojo.png'))  # Cambiar el icono a uno que muestre la contraseña
    else:
        password_input.setEchoMode(QLineEdit.Password)
        button.setIcon(QIcon('img/ojo-tachado.png')) 

#------------------------------------------------------------------------------------------------

def cerrar (elem1,elem2, elem3):
    elem1.close()
    elem2.hide()
    elem3.show()


def Ajustes2(icono,icon,name,lapiz):
    icono.setObjectName("icono")
    icono.setPixmap(icon.pixmap(24, 24))
    icono.setFixedWidth(25)        
    name.setObjectName("titulo") 
    lapiz.setIcon(QIcon('img/pencil.png'))
    lapiz.setFixedWidth(24)
    lapiz.setFixedHeight(34)
    lapiz.setIconSize(lapiz.size()) 
    lapiz.setStyleSheet("""
            QPushButton {
                background-color :transparent;
                font-size: 18px;
            }
        """)
    lapiz.hide()     


    def aniadirE(self,fol):
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