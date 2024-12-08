
import sys
from PyQt5.QtWidgets import QFrame,QLineEdit,QPushButton,QGroupBox,QGridLayout, QHBoxLayout, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QFrame
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QFont,QIcon,QPixmap

def Titulo_Config(title_label):
    title_label.setAlignment(Qt.AlignCenter)
    font = QFont("Arial", 30, QFont.Bold)
    title_label.setFont(font)
    title_label.setStyleSheet("""
        QLabel{
            color: black
        }
    """)

def Name_style (campo):
    campo.setStyleSheet("""
        QLabel {
            background-color:black;
            color: white;
            font-size: 15px;
            font-family: 'sans-serif';
            }
        """)

def Input_style (input,c,s):
    if(c==1):  #c de contraseña si es 1 es un input de contraseña  por ende se oculta la contraseña
        input.setEchoMode(QLineEdit.Password)
    input.setFixedWidth(300)
    input.setFixedHeight(31) 
    if(s==1):#s es de signup si es 1 tiene otro estilo
        input.setStyleSheet("""
            QLineEdit {
                background:#8700FC;
                font-size: 15px;
                border: 2px solid white;
                border-radius: 10px;
            }
        """)
    else:
        input.setStyleSheet("""
            QLineEdit {
                background:transparent;
                font-size: 15px;
                border: none;
                border-bottom: 1px solid #fff;
                border-left: 1px solid #fff;
                color : white;
                outline: none;
            }
        """)

def Button_config (buton):
    buton.setFixedWidth(150)
    buton.setFixedHeight(50)
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

def Button_config2 (buton,c,s):
    if (c==1):
        buton.setObjectName("mostrar")
        buton.setIcon(QIcon('img/ojo-tachado.png'))  # Reemplaza 'ruta/al/icono.png' por la ruta real de tu imagen de ícono
    else:
        buton.setObjectName("user")
        buton.setIcon(QIcon("img/user.png"))
    buton.setIconSize(buton.size())  # Ajusta el tamaño del ícono al tamaño del botón
    buton.setFixedWidth(30)
    buton.setFixedHeight(31)
    if(s==1):
        buton.setStyleSheet("""
            QPushButton {
                background:transparent;
                height:40px;
            }
        """)
    else:
        buton.setStyleSheet("""
            QPushButton {
                height:40px;
                border-radius: 20px; 
                border-bottom: 1px solid white;
                border-right: 1px solid white;
            }
        """)  



#Contenedores individuales

def subcontenedor(input,sub_espacio_widget,button,l,t,r,b):
    sub_espacio_layout = QHBoxLayout()
    sub_espacio_layout.setContentsMargins(l,t,r,b)  # Ajustar margen izquierdo
    sub_espacio_layout.addWidget(input)
    sub_espacio_layout.addWidget(button)
    sub_espacio_widget.setLayout(sub_espacio_layout)
    sub_espacio_widget.setStyleSheet('''
        QWidget{
            background: black;
        }
    ''')

def contenedor_botones(login_button,signup_button,botones_box):
    botones = QHBoxLayout() 
    botones.addWidget(login_button) 
    botones.addWidget(signup_button)
    botones_box.setLayout(botones)



#Contendores Sign Up

def contenedor_usuario(user_container, user_label, user2_label, name_input, lastname_input):
    diseño=QVBoxLayout(user_container)
    aux=QGroupBox("")
    layout = QVBoxLayout()
    layout.addWidget(user_label)
    layout.addWidget(name_input)
    layout.addWidget(user2_label)
    layout.addWidget(lastname_input)
    aux.setLayout(layout)
    diseño.addWidget(aux)
    user_container.setLayout(diseño)
    user_container.setFrameShape(QFrame.StyledPanel)
    user_container.setStyleSheet("""
        QFrame {
            border: none;
            background-color: black;
        }
        QVBoxLayout{
            border:none;
            background-color:black;
        }
        QGroupBox{
            border:none;
            background-color:black;
        }
    """)

def contemail(email_container, email_label, email_input):
    diseño=QVBoxLayout(email_container,)
    aux=QGroupBox("")
    layout = QVBoxLayout()
    layout.setContentsMargins(0,0,0,10)
    layout.addWidget(email_label)
    layout.addWidget(email_input)
    aux.setLayout(layout)
    diseño.addWidget(aux)
    email_container.setLayout(diseño)
    email_container.setFrameShape(QFrame.StyledPanel)
    email_container.setStyleSheet("""
        QFrame {
            border:none;
            background-color: black;
        }
        QVBoxLayout{
            border:none;
            background-color:black;
        }
        QGroupBox{
            border:none;
            background-color:black;
            padding-left:10px;
        }
    """)

def contepassword(password_container, password_label,p, password_input,password_inputc,button,buttonc):
    diseño=QVBoxLayout(password_container)

    aux=QGroupBox("")
    layout = QVBoxLayout()
    layout.addWidget(password_label)

    sub_espacio_widget = QWidget()
    subcontenedor(password_input,sub_espacio_widget,button,0,0,5,0)
    layout.addWidget(sub_espacio_widget)
    
    layout.addWidget(p)

    sub_espacio_widget2 = QWidget()
    subcontenedor(password_inputc,sub_espacio_widget2,buttonc,0,0,5,0)
    layout.addWidget(sub_espacio_widget2)
    
    aux.setLayout(layout)
    diseño.addWidget(aux)
    password_container.setLayout(diseño)
    password_container.setFrameShape(QFrame.StyledPanel)
    password_container.setStyleSheet("""
        QFrame {
            border: none;
            background-color: black;
        }
        QVBoxLayout{
            border:none;
            background-color:black;
        }
        QGroupBox{
            border:none;
            background-color:black;
        }
    """)

def contetotal(container, user_container, email_container, password_container,botones):
    layout = QVBoxLayout()
    layout.setContentsMargins(0,0,0,20)

    # Agregar los QFrames al layout principal
    layout.addWidget(user_container)
    layout.addWidget(email_container)
    layout.addWidget(password_container)
    layout.addWidget(botones)

    # Configurar el contenedor
    container.setContentsMargins(0, 0, 0, 30)
    container.setLayout(layout)
    container.setMaximumHeight(600)
    container.setStyleSheet("""
        QFrame {
            border:none;
            background-color:black;
        }
        QVBoxLayout{
            border:none;
            background-color:black;
        }
    """)

def toggle_visibility(password_input,button):
    if password_input.echoMode() == QLineEdit.Password:
        password_input.setEchoMode(QLineEdit.Normal)
        button.setIcon(QIcon('img/ojo.png'))  # Cambiar el icono a uno que muestre la contraseña
    else:
        password_input.setEchoMode(QLineEdit.Password)
        button.setIcon(QIcon('img/ojo-tachado.png')) 


