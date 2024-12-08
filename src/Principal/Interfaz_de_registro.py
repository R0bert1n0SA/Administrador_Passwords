
import sys
from PyQt5.QtWidgets import QAction,QMenuBar ,QMenu,QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton, QFrame
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QFont,QIcon,QPixmap
from Principal.config import *


class Sign_upWindow(QWidget):
    login_button_clicked = pyqtSignal()
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("SecurityBox")
        self.setGeometry(100, 100, 900, 400)

        layout = QVBoxLayout(self)
        self.setStyleSheet("""
            QWidget {
                background-color: gray;
            }
        """)

        title_label = QLabel("Crear Cuenta")
        Titulo_Config(title_label)
        layout.addWidget(title_label)


        container = QFrame()
        container.setObjectName("container")
        container.setFrameShape(QFrame.StyledPanel)
        container.setStyleSheet("""
            QFrame#container {
                background-color:black;
                padding: 20px;
            }
        """)
        container.setFixedWidth(400)
        container.setFixedHeight(600)
        container_layout = QVBoxLayout(container)

    # Definicion de Campo para usuario 
        User = QLabel("Name:")
        user2=QLabel("Last_Name")
        Name_style(User)
        Name_style(user2)

    #Input/ingreso de datos
        self.name_input = QLineEdit()
        Input_style(self.name_input,0,1)   
        self.Lastname_input = QLineEdit()
        Input_style(self.Lastname_input,0,1) 

    # Definicion de Campo para email 
        email = QLabel("Email:")
        Name_style(email)

    #Input/ingreso de datos
        self.email_input = QLineEdit()
        Input_style(self.email_input,0,1)

    # Definicion de Campo para Password
        password_label= QLabel("Password:")
        p = QLabel("Password:")
        Name_style(password_label)
        Name_style(p)
    #Input/ingreso de datos   
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        Input_style(self.password_input,1,1)
        
        self.password_inputc = QLineEdit()
        self.password_inputc.setEchoMode(QLineEdit.Password)
        Input_style(self.password_inputc,1,1)
        
        button = QPushButton(self)
        Button_config2(button,1,1)  # Configuracion de Botones 
        button.clicked.connect(lambda:toggle_visibility(self.password_input,button))

        buttonc = QPushButton()
        Button_config2(buttonc,1,1)
        buttonc.clicked.connect(lambda:toggle_visibility(self.password_inputc,buttonc))

    #Boton Inicio de Sesion    
        Enviar_button = QPushButton("Enviar")
        Enviar_button.setObjectName("Enviar")
        Button_config(Enviar_button)  # Configuracion de Botones 
    #Boton Crear cuenta  
        cancel_button = QPushButton("Cancel")
        cancel_button.setObjectName("Cancelar")
        Button_config(cancel_button)
        cancel_button.clicked.connect(self.enviar)


    #Contenedores Individules para agrupar las distintas partes
        user_group_box = QFrame()
        Email_group_box = QFrame()
        password_group_box = QFrame()
        botones=QGroupBox("")
        group_box = QFrame()

        contenedor_usuario(user_group_box, User, user2, self.name_input, self.Lastname_input)
        contemail(Email_group_box, email, self.email_input)
        contepassword(password_group_box, password_label,p, self.password_input,self.password_inputc,button,buttonc)
        contenedor_botones(Enviar_button,cancel_button,botones)
        contetotal(group_box, user_group_box, Email_group_box, password_group_box,botones)
        
        container_layout.addWidget(group_box)
        container_layout.setSpacing(0)
        layout.addWidget(container)
        layout.setAlignment(Qt.AlignCenter)

    def enviar(self):
        self.login_button_clicked.emit()   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Sign_upWindow()
    main_window.show()
    sys.exit(app.exec_())

    