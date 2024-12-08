

import sys
import os
import requests
import hashlib
from PyQt5.QtWidgets import QApplication,QGroupBox,QListWidget,QListWidgetItem, QComboBox, QVBoxLayout, QFrame, QListView,QCheckBox, QLineEdit, QPushButton, QHBoxLayout, QWidget, QInputDialog, QMessageBox,QAbstractItemView
from PyQt5.QtCore import Qt,QTimer,pyqtSignal
from PyQt5.QtGui import QCursor, QIcon,QIntValidator,QFont,QStandardItemModel, QStandardItem,QPixmap
from Configuraciones.config_creacion import *


class Creacion(QFrame):
    gene=pyqtSignal()
    closse=pyqtSignal()
    def __init__(self): 
        super().__init__()
        self.InicializacionIU()
        self.configUI()


    def InicializacionIU(self):
        self.setWindowTitle("SecurityBox")
        self.setFixedSize(453,680)
        self.setStyleSheet("""
            QWidget {
                background-color: #353435 ;
            }
            QLineEdit{
                border:none;
                border-bottom:2px solid black;
            }
        """)


    def configUI(self):
        # Layout principal
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        Main=QFrame()
        self.Main_layout=QVBoxLayout()
        self.Main_layout.setContentsMargins(25,0,25,0)

        self.cabeza()
        self.Carpeta()
        self.Main_layout.addWidget(self.contG)
        self.Main_layout.addWidget(self.carpetass)
        Main.setLayout(self.Main_layout)
        Main.setFixedHeight(400)
        self.layout.addWidget(Main,Qt.AlignBottom)
        self.layout.addWidget(self.Pie_de_pagina,4,Qt.AlignBottom)


    def cabeza(self):
        NombreL = QLabel('Nombre')
        UsuarioL= QLabel('Usuario')
        Nombre  = QLineEdit("")
        Usuario = QLineEdit("")
        Password= QLineEdit("")
        
        Password.setEchoMode(QLineEdit.Password)
        Nombre.setFixedHeight(20)
        Usuario.setFixedHeight(20)
        Password.setFixedHeight(20)

        self.verificador=QPushButton()
        self.ojo=QPushButton()
        self.generador=QPushButton()
        self.verificador.setIcon(QIcon('img/verificar.png'))
        self.ojo.setIcon(QIcon('img/ojo-tachado.png'))
        self.generador.setIcon(QIcon('img/technology.png'))

        Button_config(self.verificador,20,20)
        Button_config2(self.ojo)
        Button_config2(self.generador)

        Contnom       = QGroupBox()
        Contuser      = QGroupBox()
        ContPassw     = QGroupBox('Password')
        self.contG         = QGroupBox()
        contenedor(Nombre,NombreL,Contnom) # Contenedor Nombre
        contenedor(Usuario,UsuarioL,Contuser) # Contenedor Usuario
        contenedorcontra(Password,self.verificador,self.ojo,self.generador,ContPassw) # Contenedor Password
        contenedorGeneral(Contnom,Contuser,ContPassw,self.contG)#Contenedor Datos
        self.ojo.clicked.connect( lambda :self.toggle_visibility(Password,self.ojo))
        self.generador.clicked.connect(self.enviar)
        self.verificador.clicked.connect(lambda:self.Comprometida(Password))


    def Carpeta(self):
        self.carpetas=QComboBox()
        self.carpetas.addItem('Sin Carpeta')
        self.Fav=QLabel("Favorito")
        self.Favoritos= QCheckBox()

        self.Guardar=QPushButton()
        self.Cancelar=QPushButton()
        self.Guardar.setIcon(QIcon('img/guardar.png'))
        self.Cancelar.setIcon(QIcon('img/cancel.png'))

        Button_config(self.Guardar,55,35)
        Button_config(self.Cancelar,55,35)
        contfav       = QGroupBox()
        self.carpetass      = QGroupBox('Carpetas')
        self.Pie_de_pagina = QGroupBox()
        contenedorfavo(self.Fav,self.Favoritos,contfav)#Contenedor de Favoritos
        contenedorcarpetasfav(self.carpetas,contfav,self.carpetass)#Contenedor de carpetas
        contenedorPie(self.Guardar,self.Cancelar,self.Pie_de_pagina)
        self.Cancelar.clicked.connect(self.Cancel)



    def enviar(self):
        # Emitir la señal  al presionar el botón "plus"
        self.gene.emit()


    def toggle_visibility(self,password_input,button):
        if password_input.echoMode() == QLineEdit.Password:
            password_input.setEchoMode(QLineEdit.Normal)
            button.setIcon(QIcon('img/ojo.png'))  # Cambiar el icono a uno que muestre la contraseña
        else:
            password_input.setEchoMode(QLineEdit.Password)
            button.setIcon(QIcon('img/ojo-tachado.png')) 


    def Comprometida(self,password):
        contra = password.text()
        if contra:
    # Calcular el hash SHA-1 de la contraseña
            sha1_hash = hashlib.sha1(contra.encode()).hexdigest().upper()
            prefix_hash = sha1_hash[:5]
            suffix_hash = sha1_hash[5:]
    # Consultar la API de "Have I Been Pwned"
            url = f"https://api.pwnedpasswords.com/range/{prefix_hash}"
            response = requests.get(url)
            if response.status_code == 200:
                hash_matches = [line.split(":") for line in response.text.splitlines()]
        
                compro = 0
                found_match = False
                for hash_suffix, count in hash_matches:
                    if hash_suffix == suffix_hash:
                        compro=int(count)
                        found_match = True
                        break
            msg_box = QMessageBox(self)
            msg_box.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint|Qt.FramelessWindowHint)

            if found_match:
                mensaje=f"¡Cuidado! Esta contraseña ha sido comprometida {compro} veces en filtraciones."
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(mensaje)
                msg_box.setStyleSheet("""
                QMessageBox {
                    background-color: yellow; 
                    border: none; 
                }
                QMessageBox QLabel {
                    background-color: yellow; /* Cambiar el color del texto en la barra de título */
                }
                """)
                msg_box.exec_()
            else:
                mensaje="La contraseña no ha sido comprometida."

                icon = QIcon("img/check.png")
                pixmap = icon.pixmap(64, 64)
                msg_box.setIconPixmap(pixmap)
                msg_box.setText(mensaje)
                msg_box.setStyleSheet("""
                QMessageBox {
                    background-color: blue; 
                    border: none; 
                }
                QMessageBox QLabel {
                    background-color: blue; /* Cambiar el color del texto en la barra de título */
                }                  
                """)
                msg_box.exec_()


    def Cancel (self):
        self.close()
        self.closse.emit()


    def aniadir(self,fol):
        self.carpetas.addItem(fol)


    def edit(self,ind,nue):
        self.carpetas.setItemText((ind+1),nue)
    


    def eliminar(self,fol):
        # Buscar el índice de la carpeta a eliminar en el QComboBox
        index = self.carpetas.findText(fol)
        # Verificar si se encontró la carpeta
        if index != -1:
        # Eliminar la carpeta del QComboBox
            self.carpetas.removeItem(index)
        # Seleccionar automáticamente la opción "Sin Carpeta"
            self.carpetas.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Creacion()
    main_window.show()
    sys.exit(app.exec_())

