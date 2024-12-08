import sys
from PyQt5.QtWidgets import QFrame,QSizePolicy,QLineEdit,QPushButton,QGroupBox,QGridLayout, QHBoxLayout, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QFrame,QSpacerItem
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QFont,QTextOption, QTextCursor, QTextCharFormat, QTextDocument,QColor
from PyQt5.QtGui import QFont,QIcon,QPixmap


def Name_style(campo):
    campo.setFixedHeight(30)
    campo.setStyleSheet("""
        QLabel {
            color: white;
            font-size: 12px;
            font-family: 'sans-serif';
        }
    """)


def Button_config(buton,a,b):
    buton.setFixedWidth(a)
    buton.setFixedHeight(b)


def Button_config2(buton, a, b, tipo):
    buton.setIconSize(buton.size())  # Ajusta el tamaño del ícono al tamaño del botón
    buton.setFixedWidth(a)
    buton.setFixedHeight(b)
    if tipo == 'e':
        buton.setStyleSheet("""
            QPushButton {
                background: blue;
                border-radius: 5px;
                height: 40px;
                border: 1px solid gray;
            }
            QPushButton:hover {
                background: red;
                border: 1px solid black;
            }
        """)
    if tipo == 'i':
        buton.setStyleSheet("""
            QPushButton {
                border-radius: 5px;
                height: 40px;
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

def generador_cuadrocontra(contra):
    contra.setReadOnly(True)
    contra.setFixedWidth(173)
    contra.setFixedHeight(60)  # Altura inicial fija
    contra.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    contra.setStyleSheet('''
        QTextEdit{
            font-size: 20px;
            padding-top: 12px;
            margin: 0px;
            margin-bottom: 4px;
        }
    ''')
    maximum_width = 200  # Anchura máxima deseada
    contra.setMaximumWidth(maximum_width)
    contra.setWordWrapMode(QTextOption.WrapAnywhere)

def container (num,esp,cont):
    contL = QVBoxLayout()
    contL.addWidget(num)
    contL.setContentsMargins(0, 0, 0, 0)
    contL.addWidget(esp)
    cont.setLayout(contL)
    cont.setFixedHeight(100)
    cont.setFixedWidth(270)
    cont.setStyleSheet('''
        QFrame{
            background:#2C2C2C;
        }
    ''')











def contenedor_general(buton, cont, contg, list_widget):
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignBottom)  # Alinear al inicio
    layout.setContentsMargins(0, 0, 0, 0)
    contenedor_boton(buton, cont)
    layout.addWidget(list_widget)
    layout.addWidget(cont)
    contg.setLayout(layout)


def contenedor_boton(buton, cont):
    Layout = QHBoxLayout()
    Layout.setContentsMargins(0, 0, 0, 0)
    Layout.addWidget(buton)
    cont.setLayout(Layout)
    cont.setFixedWidth(300)
    cont.setFixedHeight(60)


def contpas(password, copy_button, generate_button, contracont):
    layout = QHBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setAlignment(Qt.AlignTop)
    layout.addWidget(password)

    buton = QFrame()
    button_layout = QHBoxLayout()
    button_layout.addWidget(copy_button)
    button_layout.addWidget(generate_button)
    buton.setLayout(button_layout)
    buton.setFixedWidth(100)

    document_height = int(password.document().documentLayout().documentSize().height() + 40)

    layout.addWidget(buton,0,Qt.AlignRight)
    contracont.setLayout(layout)
    contracont.setMinimumHeight(document_height)
    contracont.setMaximumHeight(document_height)
    contracont.setStyleSheet('''
        QGroupBox{
            border: 2px solid blue;
        }
        QTextEdit{
            border: none;
        }
    ''')


def barra(longitud, valor, slider, barracont, cont):
    grilla = QVBoxLayout()
    grilla.setContentsMargins(0, 0, 0, 66)

    aux = QFrame()
    auxL = QHBoxLayout()
    auxL.setContentsMargins(0, 0, 5, 0)
    auxL.addWidget(longitud,-90)
    auxL.addWidget(valor,80)
    auxL.addWidget(slider)
    aux.setLayout(auxL)
    aux.setFixedHeight(50)

    grilla.addWidget(aux)
    grilla.addWidget(cont)
    barracont.setLayout(grilla)
    barracont.setFixedHeight(155)
    barracont.setFixedWidth(270)
    barracont.setStyleSheet('''
        QLabel{
            font-size:16px;
            font-family: 'Arial';
        }    
        QGroupBox{
            border:none;               
        }
        QFrame{
            border:none;
            background:#2C2C2C;
            color:white;
        }                                                    
    ''')

def cajaopcion(enunciado, ql1, ql2, op1, op2, cuadro):
    Layout = QVBoxLayout()
    Layout.addWidget(enunciado)

    aux = QGroupBox()
    aux2 = QGroupBox()
    auxl = QHBoxLayout()
    auxl.setContentsMargins(0, 0, 0, 0)
    auxl.setAlignment(Qt.AlignLeft)
    auxl.addWidget(op1)
    auxl.addWidget(ql1)
    aux.setLayout(auxl)

    auxl2 = QHBoxLayout()
    auxl2.setContentsMargins(0, 0, 0, 0)
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
    layout.setContentsMargins(0, 0, 10, 0)
    layout.addWidget(elemn)
    layout.addWidget(name)
    layout.addWidget(increment)
    layout.addWidget(decrement)

    cont.setLayout(layout)
    cont.setFixedHeight(52)
    cont.setFixedWidth(270)
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


def botones(incrementC, decrementC, boto):
    bLayout=QVBoxLayout()
    bLayout.addWidget(incrementC)
    bLayout.addWidget(decrementC)
    boto.setLayout(bLayout)
    boto.setFixedHeight(40)
    boto.setFixedWidth(27)


def palabras_cont(palabras,contador,incrementC, decrementC,p):
    Layout=QHBoxLayout()
    Layout.setContentsMargins(0, 0, 16, 0)
    Layout.addWidget(palabras)

    aux=QGroupBox()
    auxL=QHBoxLayout()
    auxL.setContentsMargins(50, 0, 10, 0)
    auxL.addWidget(contador)
    auxL.addWidget(incrementC)
    auxL.addWidget(decrementC)
    aux.setLayout(auxL)

    Layout.addWidget(aux)
    p.setLayout(Layout)
    p.setFixedHeight(40)
    p.setFixedWidth(270)
    p.setStyleSheet('''
        QGroupBox {
            border:none;
            background-color:#2C2C2C;
        }
        QLabel{
            font-size: 12px;
            color:white;
            background-color:#2C2C2C;       
        }
        QLineEdit {
            font-size: 15px;
            border: none;
            color:white;
            background-color:#2C2C2C;
        }
    ''')


def cajaopcion2(op1, op2, cuadro):
    Layout = QVBoxLayout()

    Layout.addWidget(op1)
    Layout.addWidget(op2)

    cuadro.setLayout(Layout)
    cuadro.setFixedWidth(270)
    cuadro.setFixedHeight(80)
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

def contsep (separador,inp, sep):
    Layout = QHBoxLayout()
    Layout.addWidget(separador)
    Layout.addWidget(inp)
    sep.setLayout(Layout)
    sep.setFixedWidth(270)
    sep.setFixedHeight(43)
    sep.setStyleSheet('''
        QGroupBox{
            border:none;
            border-bottom: 1px solid black;
            background:#2C2C2C;
        }
        QLabel{
            background:#2C2C2C;
            font-size:12px;
            font-family:'Arial';
            color:white;
            border:none;
        }             
    ''')

def cuadro_frase(cont2,sep,checkB,fra):
    Layout=QVBoxLayout()
    Layout.setContentsMargins(0,0,0,45)
    Layout.addWidget (cont2)
    Layout.addWidget(sep)
    Layout.addWidget(checkB)
    fra.setLayout(Layout)
    fra.setStyleSheet('''
        QGroupBox{
            border:none;
            background:gray;
        }           
    ''')

