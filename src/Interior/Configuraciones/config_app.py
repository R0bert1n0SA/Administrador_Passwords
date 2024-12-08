
import sys
from PyQt5.QtWidgets import QFrame,QSizePolicy,QLineEdit,QPushButton,QGroupBox,QGridLayout, QHBoxLayout, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QFrame,QSpacerItem
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QFont,QTextOption, QTextCursor, QTextCharFormat, QTextDocument,QColor
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

def generador_cuadrocontra(contra):
    contra.setReadOnly(True)
    contra.setFixedWidth(173)
    contra.setFixedHeight(60)  # Altura inicial fija
    contra.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    contra.setStyleSheet('''
        QTextEdit{
            font-size: 20px;
            padding-top: 12px;
            margin:0px;
            margin-bottom:4px;                 
        }
    ''')
    maximum_width = 200  # Anchura máxima deseada
    contra.setMaximumWidth(maximum_width)
    contra.setWordWrapMode(QTextOption.WrapAnywhere)

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
                font-size: 18px;
                border-radius: 20px; 
            }
            QPushButton:hover {
                border: 2px solid white;
            }
        """)

def Button_config2 (buton,a,b,tipo):
    buton.setIconSize(buton.size())  # Ajusta el tamaño del ícono al tamaño del botón
    buton.setFixedWidth(a)
    buton.setFixedHeight(b)
    if(tipo=='e'):
        buton.setStyleSheet("""
            QPushButton {
                background:blue;
                border-radius: 5px;
                height:40px;
                border: 1px solid gray;
            }
            QPushButton:hover {
                background:red;
                border: 1px solid black;
            }
        """)    
    if(tipo=='i'):
        buton.setStyleSheet("""
            QPushButton {
                border-radius: 5px;
                height:40px;
                border: 1px solid gray;
            }
        """) 

def config_checkbox(checkbox):
    checkbox.setStyleSheet('''
        QCheckBox {
            border: none;
            background:#2C2C2C;
        }
        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            background-color:white;
            border: 2px solid black;
            border-radius: 12px ;
        }

        QCheckBox::indicator:hover {
            width: 20px;
            height: 20px;
            background-color:white;
            border: 2px solid #827F84;
            border-radius: 12px ;
        } 

        QCheckBox::indicator:checked {
            background-image: url(img/circle.png);
            background-position: center;
            background-repeat: no-repeat;
            background-color:black;
            border: 2px solid black;              
        }
        QCheckBox::indicator:checked:hover {
            background-image: url(img/circle.png);
            background-position: center;
            background-repeat: no-repeat;
            background-color:#2C2C2C;
            border: 2px solid #2C2C2C;              
        }                 
    ''')
















def contenedor_general(buton,cont, contg,list_widget):
    layout=QVBoxLayout()
    layout.setAlignment(Qt.AlignBottom)  # Alinear al inicio
    layout.setContentsMargins(0,0,0,0)
    contenedor_boton(buton,cont)
    layout.addWidget(list_widget)
    layout.addWidget(cont)
    contg.setLayout(layout)


def contenedor_boton(buton,cont):
    Layout=QHBoxLayout()
    Layout.setContentsMargins(0,0,0,0)
    Layout.addWidget(buton)
    cont.setLayout(Layout)
    cont.setFixedWidth(300)
    cont.setFixedHeight(60)

def contpas(password,copy_button,generate_button,contracont):
    layout=QHBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setAlignment(Qt.AlignTop)
    layout.addWidget(password)

    buton=QGroupBox("")
    button_layout = QHBoxLayout()
    button_layout.addWidget(copy_button)
    button_layout.addWidget(generate_button)
    buton.setLayout(button_layout)  
    buton.setFixedWidth(100)



    document_height =int(password.document().documentLayout().documentSize().height()+40)


    layout.addWidget(buton)
    contracont.setLayout(layout)
    contracont.setMinimumHeight(document_height)
    contracont.setMaximumHeight(document_height)
    contracont.setStyleSheet('''
        QFrame{
            border: 2px solid blue;
        }
        QTextEdit{
            border: none;
        }
        QGroupBox{
            border:none;
        }
    ''')


def barra(longitud,valor,slider,barracont,cont):
    grilla=QGridLayout()
    grilla.setContentsMargins(0, 0, 0, 66)
    # Agregar el slider en la primera columna
    aux=QFrame()
    auxL=QHBoxLayout()
    auxL.setContentsMargins(0, 0, 5, 0)
    auxL.addWidget(longitud)
    auxL.addWidget(valor)
    auxL.addWidget(slider)
    aux.setLayout(auxL)
    aux.setFixedHeight(50)

    grilla.addWidget(aux, 0, 0)
    grilla.addWidget(cont, 1, 0)
    barracont.setLayout(grilla)
    barracont.setFixedHeight(155)
    barracont.setFixedWidth(270)
    barracont.setStyleSheet('''
        QLabel{
            font-size:16px;
            font-family: 'Arial';
        }    
        QFrame{
            border:none;
            background:#2C2C2C;
            color:white;
        }                                                    
    ''')

def cajaopcion(enunciado,ql1,ql2,op1,op2,cuadro):
    Layout=QVBoxLayout()
    Layout.addWidget(enunciado)
    
    aux=QGroupBox()
    aux2=QGroupBox()
    auxl=QHBoxLayout()
    auxl.setContentsMargins(0,0,0,0)
    auxl.setAlignment(Qt.AlignLeft)  
    auxl.addWidget(op1)
    auxl.addWidget(ql1)
    aux.setLayout(auxl)

    auxl2=QHBoxLayout()
    auxl2.setContentsMargins(0,0,0,0)
    auxl2.setAlignment(Qt.AlignLeft)  # Alinear a la izquierda
    auxl2.addWidget(op2)
    auxl2.addWidget(ql2)
    aux2.setLayout(auxl2)

    Layout.addWidget(aux)
    Layout.addWidget(aux2)
    cuadro.setLayout(Layout)
    cuadro.setFixedWidth(270)
    cuadro.setFixedHeight(110)
    cuadro.setStyleSheet('''
        QGroupBox{
            background:#2C2C2C;
            border:none;
        }
        QLabel{
            background:2C2C2C;
            font-size:15px;
            font-family:'Arial';
            color:white;
        }
    ''')

def contenedor_cant(name, elemn, increment, decrement, cont):
    layout = QHBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(elemn)
    layout.addWidget(name)
    layout.addWidget(increment)
    layout.addWidget(decrement)

    cont.setLayout(layout)
    cont.setFixedHeight(52)
    cont.setStyleSheet('''
        QGroupBox {
            border-bottom: 2px solid black;
            border-top: 2px solid #2C2C2C;
            background:#2C2C2C;           
        } 
        QLabel {
            font-size: 15px;
            color:white;          
        } 
        QLineEdit {
            font-size: 16px;
            border: none;
            color:white;
            background:#2C2C2C;            
        }                                      
    ''')         









