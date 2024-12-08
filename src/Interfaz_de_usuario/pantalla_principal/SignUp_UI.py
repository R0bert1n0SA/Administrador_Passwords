import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QGroupBox,QAction,QMenuBar,QSpacerItem,QSizePolicy ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame,QHBoxLayout
from PyQt5.QtCore import Qt,QSize,pyqtSignal,QFile,QTextStream
from PyQt5.QtGui import QFont,QIcon,QPixmap
from Funciones_Generales import *

class SignUp_UI(QWidget):
    Login=pyqtSignal()
    def __init__(self): 
        super().__init__()
        Inicializar(self)
        Config(self)
        Titulo(self)
        self.SignUp_Contenedor()



    def AjustesLabels(self,email,Password,PasswordConf,Mensaje,Mensajeconf):
        email.setStyleSheet("""QLabel{
                margin-left:35px;                
                color: white;
                font-size: 15px;
                font-family: 'sans-serif';
                font-weight: bold;
            }""")
        Password.setStyleSheet("""QLabel{
                margin-left:35px;                
                color: white;
                font-size: 15px;
                font-family: 'sans-serif';
                font-weight: bold;
            }""")
        PasswordConf.setStyleSheet("""QLabel{
                margin-left:35px;
                color: white;
                font-size: 15px;
                font-family: 'sans-serif';
                font-weight: bold;
            }""")
        Mensaje.setStyleSheet("""QLabel{
                background:transparet;
                color: white;
                font-size: 11px;
                font-family: 'Arial';
                font-weight: ligther; 
                margin-left: 25px; 
            }""")
        Mensajeconf.setStyleSheet("""QLabel{color: white;
                font-size: 11px;
                font-family: 'Arial';
                font-weight: ligther;  
                margin-left: 25px;                  
            }""")


    def EmailCont(self,email,email_i,Contemail):
        Plantilla=QVBoxLayout(Contemail)
        Plantilla.addWidget(email)
        Plantilla.addWidget(email_i)
        Contemail.setFixedHeight(80)


    def InputConstructor(self,Passwd_i,mostrar,Cont):
        Plantilla=QHBoxLayout(Cont)
        Plantilla.addWidget(Passwd_i)
        Plantilla.addWidget(mostrar)
        Cont.setFixedWidth(380)
        Cont.setStyleSheet("""QFrame{margin-left: 20px;}""")


    def Passwdcont(self,entrada,passcont,Mensaje,cont):
        Plantilla=QVBoxLayout(cont)
        Plantilla.addWidget(entrada)
        Plantilla.addWidget(passcont)
        Plantilla.addWidget(Mensaje)
        cont.setFixedHeight(110)


    def SignUp_Contenedor(self):
    #Contenedores y Diseños
        Interactive_UI =QFrame()
        boton          =QFrame()
        Contemail      =QFrame()
        PasswdContGen  =QFrame()
        PasswdContGen2 =QFrame()
        Contpassw      =QFrame()
        Contpassw2     =QFrame()
        Plantilla      =QVBoxLayout(Interactive_UI)
        bPlantilla     =QHBoxLayout(boton)
    #Declaracion de Widgets        
        email          =QLabel("Email")
        Password       =QLabel("Contraseña")
        PasswordConf   =QLabel("Contraseña")
        Mensaje        =QLabel("* Contraseña minimo 12 caracteres Use [0...9],[A-Z],[a-z] y alfanumericos  ")
        Mensajeconf    =QLabel("* Contraseña minimo 12 caracteres Use [0...9],[A-Z],[a-z] y alfanumericos  ")
        email_i        =QLineEdit()
        Password_i     =QLineEdit()
        Password_iConf =QLineEdit()
        login_button   =QPushButton("Enviar")
        signup_button  =QPushButton("Cancelar")
        Ver_Passw      =QPushButton()
        Ver_Passwconf  =QPushButton()

        Password.setMargin(0)  # Establece el margen inferior de Password a 0
        PasswordConf.setMargin(0)
        Ajustes (email_i,Interactive_UI,360,1,0)
        Ajustes (Password_i,Interactive_UI,320,1,1)
        Ajustes (Password_iConf,Interactive_UI,320,1,1)
        AjustesItems(Ver_Passw,0,1)
        AjustesItems(Ver_Passwconf,0,1)
        self.AjustesLabels(email,Password,PasswordConf,Mensaje,Mensajeconf)
        botonesconfig(login_button)
        botonesconfig(signup_button)


        self.EmailCont(email,email_i,Contemail)
        self.InputConstructor(Password_i,Ver_Passw,PasswdContGen)
        self.Passwdcont(Password,PasswdContGen,Mensaje,Contpassw)
        self.InputConstructor(Password_iConf,Ver_Passwconf,PasswdContGen2)
        self.Passwdcont(PasswordConf,PasswdContGen2,Mensajeconf,Contpassw2)

        bPlantilla.addWidget(login_button)
        bPlantilla.addWidget(signup_button)
        Plantilla.addWidget(Contemail)
        Plantilla.addWidget(Contpassw)
        Plantilla.addWidget(Contpassw2)
        Plantilla.addWidget(boton)
        self.Plantilla.addWidget(Interactive_UI,1,Qt.AlignCenter)

        signup_button.clicked.connect(self.enviar)
        Ver_Passw.clicked.connect(lambda:toggle_visibility(Password_i,Ver_Passw))
        Ver_Passwconf.clicked.connect(lambda:toggle_visibility(Password_iConf,Ver_Passwconf))



    def enviar(self):
        self.Login.emit()   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SignUp_UI()
    main_window.show()
    sys.exit(app.exec_())




"""
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,QVBoxLayout
from PyQt5.QtCore import Qt

class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sign Up")
        self.setGeometry(100, 100, 400, 200)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit(self)
        self.character_counter = QLabel("0/12")
        
        layout = QVBoxLayout()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.character_counter)
        self.setLayout(layout)

        self.password_input.textChanged.connect(self.updateCharacterCount)

    def updateCharacterCount(self):
        text_length = len(self.password_input.text())
        self.character_counter.setText(f"{text_length}/12")

        if text_length >= 12:
            self.character_counter.setStyleSheet("color: white; background-color: red;")
        else:
            self.character_counter.setStyleSheet("color: white; background-color: transparent;")

if __name__ == "__main__":
    app = QApplication([])
    window = SignUpWindow()
    window.show()
    app.exec_()


class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sign Up")
        self.setGeometry(100, 100, 400, 200)

        self.password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit(self)
        self.feedback_label = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.feedback_label)
        layout.setAlignment(self.password_label, Qt.AlignLeft)
        layout.setAlignment(self.password_input, Qt.AlignLeft)
        layout.setAlignment(self.feedback_label, Qt.AlignLeft)

        self.password_input.textChanged.connect(self.check_password_strength)

        self.setLayout(layout)

    def check_password_strength(self):
        password = self.password_input.text()
        if len(password) < 12:
            self.feedback_label.setText("La contraseña es corta. Debe tener al menos 12 caracteres.")
        elif not any(c.isupper() for c in password):
            self.feedback_label.setText("La contraseña debe contener al menos una letra mayúscula.")
        elif not any(c.islower() for c in password):
            self.feedback_label.setText("La contraseña debe contener al menos una letra minúscula.")
        elif not any(c.isdigit() for c in password):
            self.feedback_label.setText("La contraseña debe contener al menos un número.")
        elif not any(c.isalnum() for c in password):
            self.feedback_label.setText("La contraseña debe contener caracteres alfanuméricos.")
        else:
            self.feedback_label.setText("Contraseña segura.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setCentralWidget(SignUpWindow())
    window.show()
    sys.exit(app.exec_())


"""