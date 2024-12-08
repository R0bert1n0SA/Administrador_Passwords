
import sys
import random
from PyQt5.QtWidgets import QSlider,QScrollArea,QStackedLayout, QApplication, QTextEdit, QCheckBox, QGroupBox, QLabel, QWidget, QVBoxLayout, QPushButton, QFrame, QHBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon,QIntValidator
from Interior.Configuraciones.config_generador import *
import nltk
from nltk.corpus import words
TOP_CONTRA=12
LOW_CONTRA=4
top_frase=20
Low_frase=3

class Generador(QWidget):
    def __init__(self):
        super().__init__()
        self.Inicializar()
        self.ConfiguracionUI()     


#FUNCIONES
    def Inicializar(self):
        self.setWindowTitle("SecurityBox")
        self.setFixedSize(330, 700)
        self.setStyleSheet("""
            QWidget {
                background-color: gray;
            }
            QLabel {
                font-size: 20px;
                padding: 5px;
            }
            QSlider {
                background-color: cyan;
                height: 10px;
                margin: 0px;
            }
            QSlider::groove {
                background-color: gray;
                color: white;
            }
            QSlider::handle {
                background-color: darkviolet;
                width: 10px;
                margin: 0px;
                border-radius: 4px;
            }
        """)


    def ConfiguracionUI(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 0)
        #Nombre
        self.nombre = QLabel()
        self.nombre.setText("GENERADOR")
        Name_style(self.nombre)
        self.Pantalla_Visual()

        self.Selector_tipo_Contraseña()
        self.Contenedor_deInterfases()
        self.Contrasena_Interfaz()
        self.Frase_Interfaz()


    def  Contenedor_deInterfases(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        section0 = QFrame()
        section0_layout = QVBoxLayout()
        section0_layout.setContentsMargins(0, 0, 0, 0)

        section0_layout.addWidget(self.nombre,-4,Qt.AlignTop)
        section0_layout.addWidget(self.contracont,3,Qt.AlignTop)
        #Defino un Apilador  
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.setCurrentIndex(0)
        #el primer widget q se agrega es el primero q se visualiza
        
        #Subcontenedor
        auxc=QGroupBox()
        auxl=QVBoxLayout()
        auxl.addWidget(self.cajaopciones,3,Qt.AlignTop)
        auxl.addLayout(self.stacked_layout)
        auxc.setLayout(auxl)
        auxc.setFixedHeight(300)
        scroll_area.setWidget(auxc)#asigno como Zona de desplazamiento 

        section0_layout.addWidget(scroll_area,10,Qt.AlignTop)
        

        section0.setLayout(section0_layout)
        section0.setStyleSheet("""
            QFrame {
                background-color: gray;
            }
        """)
        self.layout.addWidget(section0,40,Qt.AlignTop)
#-------------------------------------------------------------

    def Pantalla_Visual(self):
        # cuadro contraseña
        self.contra = QTextEdit()
        generador_cuadrocontra(self.contra)
    # botones del cuadro
        copy_button = QPushButton("")
        copy_button.setIcon(QIcon('img/copy.png'))#Le asigno un icono
        Button_config2(copy_button, 30, 30, 'i')      
        self.generate_button = QPushButton("")
        self.generate_button.setIcon(QIcon('img/work-process.png'))#Le asigno un icono
        Button_config2(self.generate_button, 30, 30, 'i')
        self.contracont = QGroupBox()
        contpas(self.contra, copy_button, self.generate_button, self.contracont)
        copy_button.clicked.connect(self.copy_password)


    def  Contrasena_Interfaz(self):
    #Casilla Numeros y sus Botones
        elemn = QLabel("Cantidad de Numeros")
        eleme = QLabel("Cantidad de Simbolos")

        self.numeros = QLineEdit(str("4"))
        self.numeros.setFixedWidth(20)
        self.especiales = QLineEdit(str("4"))
        self.especiales.setFixedWidth(20)

        increment = QPushButton("▲")
        increment2 = QPushButton("▲")
        decrement = QPushButton("▼")
        decrement2 = QPushButton("▼")
        Button_config(increment,15,15)
        Button_config(decrement,15,15)
        Button_config(increment2,15,15)
        Button_config(decrement2,15,15)

        cont = QGroupBox()#Contenedor de Numeros + Contenedor Simbolos
        num = QGroupBox("")#Contenedor Numeros
        esp = QGroupBox(" ")#Contenedor Simbolos
        contenedor_cant(self.numeros, elemn, increment, decrement, num)
        contenedor_cant(self.especiales, eleme, increment2, decrement2, esp)
        container(num,esp,cont)
        
        self.barra = QSlider(Qt.Horizontal)# Crear Barra
        self.barra.setMinimum(12)  # Valor mínimo del rango
        self.barra.setMaximum(128)  # Valor máximo del rango
        self.barra.setSingleStep(1)  # Incremento/decremento del valor al mover la barra
        self.barra.setFixedWidth(130)
        self.valor_label = QLabel("12")
        self.longitud = QLabel("Longitud")
        barracont = QGroupBox()
        barra(self.longitud, self.valor_label, self.barra, barracont, cont)
        self.barra.valueChanged.connect(self.actualizar_valor)
        self.stacked_layout.addWidget(barracont)  # Agregar barracont al layout apilado

        increment.clicked.connect(lambda: self.increment(self.numeros,self.especiales,TOP_CONTRA))
        increment2.clicked.connect(lambda: self.increment(self.especiales,self.numeros,TOP_CONTRA))
        decrement.clicked.connect(lambda: self.decrement(self.numeros,LOW_CONTRA))
        decrement2.clicked.connect(lambda: self.decrement(self.especiales,LOW_CONTRA))
#-------------------------------------------------------------

    def Frase_Interfaz(self):
        # Número de palabras
        palabras = QLabel('Número de palabras:')
        Separador= QLabel('Separador De Palabras')
        self.contador= QLineEdit(str('3'))
        incrementC = QPushButton("▲")
        decrementC = QPushButton("▼")
        Button_config(incrementC,15,15)
        Button_config(decrementC,15,15)
        subc= QGroupBox("")
        palabras_cont(palabras,self.contador,incrementC, decrementC,subc)


        
        self.Separador_input = QLineEdit()
        self.Separador_input.setMaxLength(1)
        sep=QGroupBox()
        contsep(Separador,self.Separador_input,sep)


        # Inicio en mayúscula
        self.Mayus = QCheckBox('Iniciar con mayúscula')
        # Incluir números
        self.Numbers = QCheckBox('Incluir números')
        checkB=QGroupBox()
        Fra=QGroupBox()
        cajaopcion2(self.Mayus,self.Numbers,checkB)
        cuadro_frase(subc,sep,checkB,Fra)
        incrementC.clicked.connect(lambda: self.incrementF(self.contador,top_frase))
        decrementC.clicked.connect(lambda: self.decrement(self.contador,Low_frase))
        self.stacked_layout.addWidget(Fra)  # Agregar Fra al layout apilado
        
#-------------------------------------------------------------

    def Selector_tipo_Contraseña(self):
        #Caja de opciones Principal
        enunciado = QLabel("Tipo de Contraseña")
        op1 = QLabel("Contraseña")
        op2 = QLabel("Frase")
        normal = QCheckBox("")
        frase = QCheckBox("")
        self.cajaopciones = QGroupBox("")
        config_checkbox(normal)
        config_checkbox(frase)
        cajaopcion(enunciado, op1, op2, normal, frase, self.cajaopciones)
        #Inicializo en Contraseña
        normal.setChecked(True)
        #Verifico Estado Marcado Contraseña o Frase
        normal.stateChanged.connect(lambda: self.check_option(normal, frase))
        frase.stateChanged.connect(lambda: self.check_option(frase, normal))
        #Verifico Cual Debo Mostrar
        normal.clicked.connect(lambda estado: self.stacked_layout.setCurrentIndex(0 if estado else 1))
        frase.clicked.connect(lambda estado: self.stacked_layout.setCurrentIndex(1 if estado else 0))
        self.generate_button.clicked.connect(lambda : self.mostrar_contrasena(frase,self.contador,self.numeros, self.especiales,self.Separador_input,self.Numbers,self.Mayus))
#-------------------------------------------------------------

    def actualizar_valor(self, valor):
        self.valor_label.setText(str(valor))


    def mostrar_contrasena(self,frase,contador,numeros, especiales,Separador_input,Numbers,Mayus):
        checked = frase.isChecked()
        if(checked):
            count=int(contador.text())
            separator = Separador_input.text()

            nltk.download('words')
            
            word_list = words.words()
            chosen_words = random.sample(word_list, count)


            password = separator.join(chosen_words)
            if Mayus.isChecked():
                password = password.title()
        else:
            minus = "abcdefghijklmnopqrstuvwxyz"
            mayus = minus.upper()
            Numeros = "1234567890"
            longuitud = self.barra.value()
            simbolos = "$,.-_:;{}[]{}´¨*'+<>\^`~¿?@!#%&/()=°|"            
            nume = int(numeros.text())
            espe = int(especiales.text())

            total_chars = longuitud  - nume - espe

            caracteres_disponibles = minus + mayus 
            if len(caracteres_disponibles) < longuitud:
                # Repetir los caracteres disponibles para alcanzar la longitud deseada
                repeticiones = longuitud // len(caracteres_disponibles) + 1
                caracteres_disponibles = caracteres_disponibles * repeticiones

            Numeros = Numeros * ((nume // len(Numeros)) + 1)
            Numeros = Numeros[:nume]
            muestra = random.sample(caracteres_disponibles, total_chars)
            muestra += random.sample(Numeros, nume)
            muestra += random.sample(simbolos, espe)
            random.shuffle(muestra)
            password = "".join(muestra)

        self.contra.setPlainText(password)
        document_height = int(self.contra.document().documentLayout().documentSize().height() + 30)
        self.contra.setMinimumHeight(document_height)
        self.contra.setMaximumHeight(document_height)
        self.contracont.setMinimumHeight(document_height)
        self.contracont.setMaximumHeight(document_height)


    def copy_password(self):
        password = self.contra.toPlainText()
        QApplication.clipboard().setText(password)


    def check_option(self, current, other):
        normal_checked = current.isChecked()
        phrase_checked = other.isChecked()
        if normal_checked:
            other.setChecked(False)
        elif phrase_checked:
            current.setChecked(False)


    def increment(self, n, ref, TC):
        value = int(n.text())
        ref_value = int(ref.text())
        longitud = self.barra.value()

        if longitud > 24:
        # Resto de los casos
            if value < TC:
                value += 1
                n.setText(str(value))
        elif(longitud <= 24):
        # Caso especial: 'longitud' es menor o igual a 24
            if(ref_value <=5) and (value < 5):
                if value < TC:
                    value += 1
                    n.setText(str(value))


    def incrementF(self,n,TC):
        value = int(n.text())
        if(value < TC):
            value += 1
            n.setText(str(value))


    def decrement(self, n,lc):
        value = int(n.text())
        if(value > lc):
            value -= 1
            n.setText(str(value))
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Generador()
    main_window.show()
    sys.exit(app.exec_())








'''

from werkzeug.security import generate_password_hash

        general(contracont,generate_button)

def encriptar_contrasena():
    encryptP=generate_password_hash(generar_contrasena())
    return encryptP

def mostrar_contrasenas():
    contrasena_entry.config(text=generar_contrasena())
    contrasena_encriptada_entry.config(text=encriptar_contrasena())




# Crear widgets
mostrar_btn = tk.Button(ventana, text="Generar", command=mostrar_contrasenas)
mostrar_btn.pack()
contrasena_label = tk.Label(ventana, text="Contraseña generada:")
contrasena_entry = tk.Label(ventana,text="")


contrasena_encriptada_label = tk.Label(ventana, text="Contraseña encriptada:")
contrasena_encriptada_entry = tk.Label(ventana, text="")

# Posicionar los widgets en la ventana
contrasena_label.pack()
contrasena_entry.pack()

contrasena_encriptada_label.pack()
contrasena_encriptada_entry.pack()

# Ejecutar la aplicación
ventana.mainloop()


















































'''


