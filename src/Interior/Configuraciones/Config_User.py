import sys
from PyQt5.QtWidgets import QFrame,QSizePolicy,QLineEdit,QPushButton,QGroupBox,QGridLayout, QHBoxLayout, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QFrame,QSpacerItem




def Button_config (buton):
    buton.setFixedWidth(24)
    buton.setFixedHeight(34)
    buton.setIconSize(buton.size()) 
    buton.setStyleSheet("""
            QPushButton {
                background-color :transparent;
                font-size: 18px;
            }
        """)


def SubCont(a,b,cont):
    layout=QHBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    layout.addWidget(b)
    layout.addWidget(a)
    cont.setLayout(layout)
    cont.setStyleSheet("""
        QGroupBox{
            border: none;
        }
    """)


def Etiq(todos,fav,icon,iconf,conte):
    layout=QVBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    aux=QGroupBox("")
    SubCont(todos, icon, aux)
    aux.setFixedWidth(180)
    layout.addWidget(aux)
    aux2=QGroupBox("")
    SubCont(fav,iconf,aux2)
    aux2.setFixedWidth(96)
    layout.addWidget(aux2)
    conte.setLayout(layout)
    conte.setFixedHeight(106)
    conte.setStyleSheet("""
        QLabel{
            color: white;
            font-size: 14px;
            font-family:'Arial';
        }
        QLabel:hover {
            color:#001385;
        }
    """)


def carpetas(mostrar,carpeta,Crear,L,cont):
    layout=QVBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    aux=QGroupBox()
    Layout2=QHBoxLayout()
    Layout2.setContentsMargins(0,0,0,0)
    Layout2.addWidget(mostrar)
    Layout2.addWidget(carpeta)
    Layout2.addWidget(Crear)
    aux.setLayout(Layout2)
    aux.setFixedHeight(106)
    layout.addWidget(aux)
    layout.addWidget(L)
    cont.setLayout(layout)
    cont.setStyleSheet("""
        QLabel{
            color: white;
            font-size: 14px;
            font-family:'Arial';
        }
    """)


def Main(opciones,carpetas,cont):
    layout=QVBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    layout.addWidget(opciones)
    layout.addWidget(carpetas)
    cont.setLayout(layout)


def List_cont(fi,elm,icon,cont):
    layout=QHBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    layout.addWidget(fi)
    layout.addWidget(elm)
    layout.addWidget(icon)
    cont.setLayout(layout)
    cont.setFixedHeight(50)