import sys
import os
from PyQt5.QtWidgets import  QSpacerItem,QListWidget,QListWidgetItem, QSizePolicy, QVBoxLayout, QFrame, QListView, QLabel, QLineEdit, QPushButton, QHBoxLayout, QWidget, QInputDialog, QMessageBox,QAbstractItemView
from PyQt5.QtCore import Qt,QTimer,QSize
from PyQt5.QtGui import QCursor, QIcon,QIntValidator,QFont,QStandardItemModel, QStandardItem

def Button_config (buton,a,b):
    buton.setFixedWidth(a)
    buton.setFixedHeight(b)
    buton.setIconSize(buton.size()) 
    buton.setStyleSheet("""
            QPushButton {
                border:1px solid gray;
                background:#39373B  ;
            }
            QPushButton:hover {
                border:2px solid black;
                background:#282629   ;
            }            
        """)

def Button_config2 (buton):
    buton.setFixedWidth(20)
    buton.setFixedHeight(20)
    buton.setIconSize(buton.size()) 
    buton.setStyleSheet("""
            QPushButton {
                border:none;
                background:transparent  ;
            }          
        """)    

def contenedor(parametro1,parametro2,cont):
    layout=QVBoxLayout()
    layout.setContentsMargins(5,5,5,0)
    layout.addWidget(parametro2,0,Qt.AlignTop)
    layout.addWidget(parametro1,0,Qt.AlignTop)
    cont.setLayout(layout)
    cont.setFixedHeight(50)
    cont.setStyleSheet('''
        QGroupBox{
            border:none;
            background:#59565B;
        }
        QLabel{
            background:#59565B;            
        }
    ''')

def contenedorcontra(parametro1,verificador,ojo,generador,cont):
    layout=QHBoxLayout()
    layout.addWidget(parametro1)
    layout.addWidget(verificador)
    layout.addWidget(ojo)
    layout.addWidget(generador)
    cont.setLayout(layout)
    cont.setFixedHeight(50)



def contenedorfavo(parametro1,parametro2,cont):
    layout=QHBoxLayout()
    layout.addWidget(parametro1,9,Qt.AlignLeft)
    layout.addWidget(parametro2,Qt.AlignRight)
    cont.setLayout(layout)
    cont.setFixedHeight(50)



def contenedorcarpetasfav(parametro1,parametro2,cont):
    layout=QVBoxLayout()
    layout.addWidget(parametro1)
    layout.addWidget(parametro2)
    cont.setLayout(layout)
    cont.setFixedHeight(130)
    cont.setStyleSheet('''
        QGroupBox{
            background:#59565B;
        }
        QLabel{
            background:#59565B;            
        }
    ''')

def contenedorGeneral(parametro1,parametro2,parametro3,cont):
    layout=QVBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    layout.addWidget(parametro1)
    layout.addWidget(parametro2)
    layout.addWidget(parametro3)
    cont.setLayout(layout)
    cont.setFixedHeight(200)
    cont.setStyleSheet('''
        QGroupBox{
            background:#59565B;
        }
        QLabel{
            background:#59565B;            
        }
    ''')



def contenedorPie(parametro1, parametro2, cont):
    layout = QHBoxLayout()
    # Agregar el primer parámetro (centrado a la izquierda)
    layout.addWidget(parametro1, alignment=Qt.AlignLeft | Qt.AlignVCenter)
    # Agregar un spacer flexible para separar los widgets
    spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    layout.addItem(spacer)
    # Agregar el segundo parámetro (centrado a la derecha)
    layout.addWidget(parametro2, alignment=Qt.AlignRight | Qt.AlignVCenter)

    cont.setLayout(layout)
    cont.setFixedHeight(60)
    cont.setFixedWidth(452)
