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

def Contenedor_Titulo(Contenedor_titulo,titulo):
    Layout=QHBoxLayout()
    Layout.setContentsMargins(0,0,0,0)
    Layout.addWidget(titulo,Qt.AlignTop)
    Contenedor_titulo.setLayout(Layout)
    Contenedor_titulo.setFixedHeight(200)


def Contenedor_Central(group_box,container):
    container.setObjectName("container")
    container.setFrameShape(QFrame.StyledPanel)
    container.setStyleSheet("""
        QFrame#container {
            background-color:black;
            padding: 20px;
        }
    """)
    container_layout = QVBoxLayout(container)
    container_layout.addWidget(group_box)
    container_layout.setSpacing(1)
    container.setLayout(container_layout)
    container.setFixedWidth(500)
    container.setFixedHeight(400)


def subcontenedor(input,sub_espacio_widget,button):
    sub_espacio_layout = QHBoxLayout()
    sub_espacio_layout.setContentsMargins(40,0,50,0)
    sub_espacio_layout.addWidget(input)
    sub_espacio_layout.addWidget(button)
    sub_espacio_widget.setLayout(sub_espacio_layout)
    sub_espacio_widget.setStyleSheet('''
        QWidget{
            background: black;
        }
    ''')


def contenedor_email(email_label, email_input, email_icon, email_group_box):
    elementos_vertical = QVBoxLayout()
    elementos_vertical.setContentsMargins(0,0,0,0)
    elementos_vertical.addWidget(email_label)
    widget_contenedor = QWidget()
    subcontenedor(email_input,widget_contenedor,email_icon)
    elementos_vertical.addWidget(widget_contenedor)
    email_group_box.setLayout(elementos_vertical)

    email_group_box.setStyleSheet('''
        QGroupBox {
            border: none;
            background-color: black;
        }
        QLineEdit {
            border: none;
            background-color: transparent;
        }
        QLabel {
            padding-left:33px;
        }

    ''')


def contenedor_Total(email_group_box,password_group_box,group_box,login_button,signup_button):
    caja = QVBoxLayout()
    caja.addWidget(email_group_box)
    caja.addWidget(password_group_box)
    group_box.setStyleSheet("""
        QGroupBox {
            border: none;
            background-color:black;
            margin-bottom: -10px;
        }
    """)
    botones_box = QGroupBox("")
    contenedor_botones(login_button,signup_button,botones_box)
    caja.addWidget(botones_box)
    group_box.setLayout(caja)


def contenedor_botones(login_button,signup_button,botones_box):
    botones = QHBoxLayout() 
    botones.addWidget(login_button) 
    botones.addWidget(signup_button)
    botones_box.setLayout(botones)