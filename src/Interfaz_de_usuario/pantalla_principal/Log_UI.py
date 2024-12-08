
import sys
from PyQt5.QtWidgets import QGroupBox,QSizePolicy,QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QIcon,QPixmap
from Funciones_Generales import *


class Log_UI (QWidget):
    signup=pyqtSignal()
    Ingreso=pyqtSignal()  
    recuperacion=pyqtSignal()  


    def __init__(self):
        super().__init__()
        Inicializar(self)
        Config(self)
        Titulo(self)
        self.Logeo_Contenedor()



# Ajustes
    def AjustesLabels(self,User,Password,Error,error2):
        User.setStyleSheet("""QLabel{margin-left:75px;}""")
        Password.setStyleSheet("""QLabel{margin-left:75px;}""")
        Error.setStyleSheet("""QLabel{color: red;margin-left: 95px;}""")
        error2.setStyleSheet("""QLabel{color: red;margin-left: 175px;}""")
        error2.hide()
        Error.hide()


    def OlvideConfig (self,Olvide):
        Olvide.setStyleSheet("""QPushButton{background:transparent;margin-left: 150px;color: cyan;font-size: 15px;font-family: 'Arial';text-decoration:underline;} QPushButton:hover{color: blue; text-decoration:underline;}""")
        Olvide.setFixedWidth(350)
        Olvide.setFixedHeight(20)
#-------------------------------------------------------------------------------------------------------


#Caraga Contenedores
    def contenedor(self,entrada,boton,cont):
        Plantilla=QHBoxLayout()
        Plantilla.addWidget(entrada)
        Plantilla.addWidget(boton)
        cont.setLayout(Plantilla)
        cont.setFixedWidth(418)
        cont.setStyleSheet("""
            QFrame{
                margin-left:74px;
            }
            QPushButton{  
                background:transparent;              
                height:40px;
                border-radius: 20px; 
                border-bottom: 1px solid white;
                border-right: 1px solid white;
            } 
        """)


    def ContenedorBotones(self,boton,boton1,boton2):
        bPlantilla=QHBoxLayout(boton)
        bPlantilla.addWidget(boton1)
        bPlantilla.addWidget(boton2)


    def ContenedorInteractivo(self,elem1,elem2,Plantilla):
        Plantilla.addWidget(elem1,1)
        Plantilla.addWidget(elem2,9)


    def ContenedorMensajes(self,Error2,Error,Olvide,boton,Plantilla):
        Plantilla.addWidget(Error)
        Plantilla.addWidget(Error2)
        Plantilla.addWidget(Olvide)
        Plantilla.addWidget(boton)
#--------------------------------------------------------------------------------------------------------------

    def Logeo_Contenedor(self):
    #Contenedores y Diseños
        Interactive_UI      =QFrame()
        boton               =QFrame()
        Contpassw           =QFrame()
        ContUser            =QFrame()
        Plantilla           =QVBoxLayout(Interactive_UI)
    #Declaracion de Widgets        
        User                =QLabel("Usuario")
        Password            =QLabel("Contraseña")
        self.Error          =QLabel("* Usuario o Contraseña Incorrectas")
        self.Error2         =QLabel("* No Hay datos")
        Olvide              =QPushButton("Olvide mi contraseña")
        self.User_i         =QLineEdit()
        self.Password_i     =QLineEdit()
        login_button        =QPushButton("Log In")
        signup_button       =QPushButton("Sign Up")
        Ver_Passw           =QPushButton()
        IconUser            =QPushButton()
    # Ajustes Visuales
        Ajustes(self.User_i,Interactive_UI,300,0,0)
        Ajustes(self.Password_i,Interactive_UI,300,0,1)
        AjustesItems(Ver_Passw,0,0)
        AjustesItems(IconUser,1,0)
        self.AjustesLabels(User,Password,self.Error,self.Error2)
        self.OlvideConfig(Olvide)
        botonesconfig(login_button)
        botonesconfig(signup_button)

        Plantilla.setContentsMargins(0,20,0,20)
    # Carga de los Contenedores
        self.contenedor(self.User_i,IconUser,ContUser)
        self.contenedor(self.Password_i,Ver_Passw,Contpassw)
        self.ContenedorBotones(boton,login_button,signup_button)
        self.ContenedorInteractivo(User,ContUser,Plantilla)
        self.ContenedorInteractivo(Password,Contpassw,Plantilla)
        self.ContenedorMensajes(self.Error2,self.Error,Olvide,boton,Plantilla)
    #Llamadas a Funciones 
        Olvide.clicked.connect(self.recuperar)
        Ver_Passw.clicked.connect(lambda:toggle_visibility(self.Password_i,Ver_Passw))
        signup_button.clicked.connect(lambda :self.enviar(1))
        login_button.clicked.connect(lambda : self.enviar(2))
        self.Plantilla.addWidget(Interactive_UI,1,Qt.AlignCenter)


    def enviar(self,flag):
        if(flag == 1):
            self.signup.emit()
        else: 
            self.Ingreso.emit()


    def Ingresar(self):
        if (self.User_i.text() == "")and(self.Password_i.text()==""):
            if (self.Error.isVisible):
                self.Error.hide()
            self.Error2.show()
            return
        else:
            return self.User_i.text(),self.Password_i.text()


    def Mensaje (self):
        if(self.Error2.isVisible):
            self.Error2.hide()
        self.Error.show()    


    def recuperar (self):
        self.recuperacion.emit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Log_UI()
    main_window.show()
    sys.exit(app.exec_())

