from PyQt5.QtCore import Qt,pyqtSignal,QObject
from PyQt5.QtWidgets import QDialog
import hashlib
import requests
from Interfaz_de_usuario.Interior_App.Almacenamiento_UI import *
from Interfaz_de_usuario.Interior_App.OpcionesVisualizacion_UI import *
from Interfaz_de_usuario.Interior_App.WorkSpace import *
from Funciones_Generales import *



class LogicaNegocioInterior (QObject):
    def __init__(self):
        super().__init__()
        self.almacenamiento_window = Almacenamiento()
        self.Usuario               = Organizacion_datos()
        self.zonaT                 = Workspace()        
        self.almacenamiento_window.Crear.connect(self.mostrar)
        self.almacenamiento_window.Editar.connect(self.mostrarE)
        self.zonaT.dato.connect(self.Corraborar)



    def mostrar(self):
        self.zonaT.mostrarcrear()


    def mostrarE(self):
        self.zonaT.mostrarEditar()


    def Corraborar(self,contra):
        msg_box = QMessageBox(self)
        msg_box.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint|Qt.FramelessWindowHint)
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
        else:
            mensaje="Ingrese una contraseña."
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



'''
    def EditarE(self,list,item,flag):
        if(flag==1):
            dato=list.itemWidget(item).findChild(QLabel,"titulo").text()
            cadena=self.Editar_carpeta(dato,list,item)
            if(cadena != None) and (cadena != dato):
                self.zonaT.editE(dato,cadena)
            print (dato)
            flag=2



    def Eliminar(self,name,list,item):
        indice=list.indexFromItem(item).row()
        list.takeItem(indice)
        self.zonaT.eliminarE(name)

'''



























#sign up controlller
#