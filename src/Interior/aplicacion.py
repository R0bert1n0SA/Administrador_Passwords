
import sys
from PyQt5.QtWidgets import QHBoxLayout,QApplication,QStackedWidget, QWidget, QVBoxLayout, QLineEdit, QPushButton,QDialog, QFrame
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QFont,QIcon,QPixmap
from Configuraciones.config_app import *
from almcenamiento import Almacenamiento
from generador_contraseña import *
from Usuario_almacenado import *
from creacion_Elemento import Creacion


class Interfaz(QMainWindow):
    Muestra=pyqtSignal()
    def __init__(self): #Constructor de Clase
        super().__init__()
        self.InicializarUi()
        self.ConfigUI()
        self.User = Organizacion_datos()


    def InicializarUi(self): 
        self.setWindowTitle("SecurityBox") #Le Asigno Titulo a la Ventana
        icono = QIcon("img/Logo.png")
        self.setWindowIcon(icono)
        self.setGeometry(100, 100, 800, 400)
        self.showMaximized()
        self.setMinimumSize(800, 200)  # Establecer tamaño mínimo
        self.setMaximumSize(1600, 1200)  # Establecer tamaño máximo             # Mostrar la ventana a pantalla completa              
        self.setStyleSheet("""
            QWidget {
                background-color: gray;
            }
            QFrame{
                border:none;
            }
            QGroupBox{
                border:none;           
                border-right: 1px solid black;
            }
        """)#Doy estilo a Elemntos al inicio


    def ConfigUI(self):
        Principal = QFrame() #Qframe para contener el contenido principal de la ventana
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)# Establecer márgenes a cero
        Principal.setLayout(self.layout)
        self.setCentralWidget(Principal) #Elemento visual  Principal de la clase

        self.seccion_barra_de_búsqueda()
        self.seccion_cont()


    def seccion_barra_de_búsqueda(self): 
    #Diseña la seccion de la barra de busqueda
        search_bar = QLineEdit(self) 
        search_bar.setPlaceholderText("Buscar...")
        Input_style(search_bar, 0,1) #Configura Estilo
        
        sectionBar = QFrame()
        sectionBar_layout = QHBoxLayout()
        sectionBar_layout.addWidget(search_bar)
        sectionBar.setLayout(sectionBar_layout)
        sectionBar.setFixedHeight(50)
        sectionBar.setStyleSheet("""
            QFrame {
                background-color: gray;
            }
        """)
        self.layout.addWidget(sectionBar)#Lo Agrego al Layout Principal


    def seccion_cont(self):
    #Contenedor  de todas las Secciones
        self.section_cont = QGroupBox()
        self.section_cont_layout = QHBoxLayout()
        self.section_cont_layout.setSpacing(0)
        self.section_cont_layout.setContentsMargins(0, 0, 0, 0)  # Establecer márgenes a cero
        self.section_cont.setLayout(self.section_cont_layout)
        self.section_cont.setStyleSheet("""
            QFrame {
                background-color: gray;
            }
        """)
        self.seccionA()
        self.seccionB()
        self.seccionC()
        self.layout.addWidget(self.section_cont)#Lo Agrego al Layout Principal


    def seccionA(self):
    #Contenedor Seccion A Contiene Intefaz de Usuario   
        sectiona = QGroupBox()
        sectiona_layout = QVBoxLayout()
        sectiona_layout.setContentsMargins(0,0,0,0)
        self.User= Organizacion_datos()
        sectiona_layout.addWidget(self.User,0,Qt.AlignTop)
        sectiona.setLayout(sectiona_layout)
        sectiona.setFixedWidth(278)
        self.section_cont_layout.addWidget(sectiona)


    def seccionB(self):
    #Contenedor Seccion B Contiene Almacenamiento de Contraseñas      
        almacenamiento_window = Almacenamiento()
        sectionB = QGroupBox()
        sectionB_layout = QVBoxLayout()
        sectionB_layout.setContentsMargins(0,0,0,0)
        sectionB_layout.addWidget(almacenamiento_window,1,Qt.AlignTop)
        sectionB.setLayout(sectionB_layout)
        sectionB.setFixedWidth(308)
        self.section_cont_layout.addWidget(sectionB)

        almacenamiento_window.signal.connect(lambda: self.mostrar_creacion(self.sectionc))


    def seccionC(self):
    #Contenedor Seccion C Contiene Creador de Nueva Contraseña a Guardar       
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap('img/Logo.png'))   # Escala la imagen para que quepa en el QLabel
    
        self.creacion = Creacion()
        
        self.sectionc = QStackedWidget()
        self.sectionc.setContentsMargins(60,0,60,0)
        self.creacion.hide()
        self.sectionc.addWidget(self.image_label)
        self.sectionc.addWidget(self.creacion)
        self.section_cont_layout.addWidget(self.sectionc)
        self.sectionc.setCurrentWidget(self.image_label)
        self.creacion.gene.connect(self.mostrar_generador)
        self.creacion.closse.connect(self.on_creacion_closed)  # Conectar la señal de cierre de creación
        # Conectar la señal actualizar de User a la función actualizar_combo_box de Almacenamiento
        self.User.aniadir.connect(self.creacion.aniadir)
        self.User.borrar.connect(self.creacion.eliminar)
        self.User.actualizar_nombre.connect(self.creacion.edit)


    def mostrar_creacion(self,section):
    # Mostrar la ventana Creacion en QStackedWidget
        self.creacion.show()
        section.setCurrentWidget(self.creacion)


    def on_creacion_closed(self):
        # Cuando la ventana de creación se cierra, mostrar nuevamente la imagen
        self.sectionc.setCurrentWidget(self.image_label)
        self.image_label.show()


    def mostrar_generador(self):
    # Crea Ventana Indipendiente con el Generador de Contraseñas
        Generator=Generador()
        GeneradorC = QDialog()
        GeneradorC.setWindowTitle("Generador")
        Elem = QHBoxLayout()
        Elem.setContentsMargins(0,0,0,0)
        Elem.addWidget(Generator,1)
        GeneradorC.setLayout(Elem)
        GeneradorC.exec()


    def Enviar(self):
        self.Muestra.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Interfaz()
    sys.exit(app.exec_())

