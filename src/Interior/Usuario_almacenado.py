import sys
import os
from PyQt5.QtWidgets import  QApplication,QListWidget,QListWidgetItem, QDialog,QMainWindow, QVBoxLayout, QFrame, QListView, QLabel, QLineEdit, QPushButton, QHBoxLayout, QWidget, QInputDialog, QMessageBox,QAbstractItemView
from PyQt5.QtCore import Qt,QTimer,QSize,pyqtSignal
from PyQt5.QtGui import QCursor, QIcon,QIntValidator,QFont,QStandardItemModel, QStandardItem
from Interior.Configuraciones.Config_User import *
'''

        # Simular datos de contraseñas almacenadas
        self.passwords = {
            "Cuenta 1": {"username": "usuario1", "password": "contraseña1"},
            "Cuenta 2": {"username": "usuario2", "password": "contraseña2"}
        }
'''
class Organizacion_datos(QWidget):
    aniadir=pyqtSignal(str)
    actualizar_nombre=pyqtSignal(int,str)
    borrar=pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.InicializarUi()
        self.ConfigUI()

        # Sección de favoritos (puedes agregar una lista aquí)
        # ...

#Funciones 
    #Funciones de Ajustes

    def InicializarUi(self):
    # Configurar la ventana principal
        self.setFixedSize(253,680)
        self.setStyleSheet("""
            QWidget {
                background-color: gray;
            }
            QGroupBox{
                border:none;
            }
        """)


    def ConfigUI(self):
        self.layout = QVBoxLayout(self)
        self.Principal()
        self.TimerCursor()


    def TimerCursor(self):
        '''
        Creamos un temporizador (QTimer) llamado self.timer.Este temporizador se utiliza para verificar la posición 
        del cursor periódicamente.Esta función se ejecutará cada vez que el temporizador alcance su tiempo de espera 
        (100 ms en este caso).
        '''
        temporizador = QTimer(self)
        temporizador.timeout.connect(self.check_cursor_position)
        temporizador.start(100)


    #Funciones de Configuracion
    def Seccion_Superior(self):
        self.selected_label = None  #variable  de instancia usada como flag para saber el icono activo
        self.ant=int(-1)            #variable de uso tipo flag para llevar un registro de qué QLabel estaba  
#                                   seleccionado "Todos los Elementos" 1 "Favoritos" 2
        self.text=None              #variable Encargada de almacenar nombre modificado y 
#                                    usada para actualizar
        self.actual=None            #variable Encargada de almacenar el nombre actua
#                                    de la carpeta con cada modificacion 
        self.Todos_elem = QLabel("Todos los Elementos ")
        self.Favorit = QLabel("Favoritos")
        # Definicion de botones
        self.iconTodos=QPushButton()
        self.iconTodos.setIcon(QIcon('img/technology.png'))#Le asigno un icono
        self.iconFav=QPushButton()
        self.iconFav.setIcon(QIcon('img/Star.png'))#Le asigno un icono
        Button_config(self.iconTodos)
        Button_config(self.iconFav)
        self.Etiquetas=QFrame()
        Etiq(self.Todos_elem,self.Favorit, self.iconTodos,self.iconFav,self.Etiquetas)
        self.Todos_elem.mousePressEvent=lambda event:self.Accion(self.Todos_elem,1,self.iconTodos)
        self.Favorit.mousePressEvent=lambda event:self.Accion(self.Favorit,2,self.iconFav)


    def Carpeta_config(self):
        self.carp=[]                #Lista de referencia de los items de la QListWidget
        self.ant2=0                 #variable de uso tipo flag para saber el icono activo
        self.ultimoitem = None
        # Lista visual de carpetas
        self.list = QListWidget(self)
        self.list.setViewMode(QListWidget.ListMode)
        self.list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list.setResizeMode(QListWidget.Adjust)
        self.list.setFixedHeight(400)
        self.list.hide()

        carpeta=QLabel("Carpetas")
        mostrarcar=QPushButton()
        mostrarcar.setIcon(QIcon('img/arrow.png'))
        Crear=QPushButton()
        Crear.setIcon(QIcon('img/addition-button.png'))
        Button_config(mostrarcar)
        Button_config(Crear)
        self.carpeta=QFrame()
        carpetas(mostrarcar,carpeta,Crear,self.list,self.carpeta)

        self.carpeta.mousePressEvent=lambda event:self.cambio(mostrarcar)
        mostrarcar.mousePressEvent=lambda event:self.cambio(mostrarcar)
        Crear.clicked.connect(self.__add_folder__)
        # Conectar la señal itemSelectionChanged de la QList a la función que maneja la selección de ítem
        self.list.itemClicked.connect(self.handle_item_selection)


    def Principal(self):
        self.Seccion_Superior()
        self.Carpeta_config()
        MainFrame=QFrame()
        Main(self.Etiquetas,self.carpeta,MainFrame)
        self.layout.addWidget(MainFrame,0,Qt.AlignTop)


    #Funciones Logica
    def cambio(self,icon):
        #Funcion que alterna la lista carpetas ver o no
        if(self.ant2==0):
            icon.setIcon(QIcon('img/arrow-down.png'))
            self.ant2=1
            self.list.show()#muestro la lista
        elif(self.ant2==1):
            icon.setIcon(QIcon('img/arrow.png'))
            self.ant2=0
            self.list.hide()#oculto la lista


    def Accion(self,elem,s,icon):
        # Función que se activa cuando se presiona el QLabel
        # Desactivar el QLabel previamente seleccionado
        if self.selected_label:
            font = self.selected_label.font()
            font.setWeight(QFont.Normal)
            self.selected_label.setStyleSheet('''
            QLabel{
                color: white;
            }
            QLabel:hover {
                color:#001385;
            }
            ''')
            if(self.ant==2):
                icon.setIcon(QIcon('img/technology.png'))
            elif(self.ant==1):
                icon.setIcon(QIcon('img/Star.png'))
            self.selected_label.setFont(font)
        # Activar el QLabel seleccionado actualmente
        font = elem.font()
        font.setWeight(QFont.Bold)
        if(s==1):
            icon.setIcon(QIcon('img/technology blue.png'))
            self.ant=1
        else:
            icon.setIcon(QIcon('img/Star blue.png'))
            self.ant=2
        elem.setFont(font)
        elem.setStyleSheet('''
            QLabel{
                color:#001385
            }
        ''')
        # Almacenar el QLabel seleccionado actualmente
        self.selected_label = elem


    def check_cursor_position(self):
        '''
        Obtenemos la posición actual del cursor en la pantalla usando QCursor.pos().
        Esto nos da la posición global del cursor.
        '''
        cursor_pos = QCursor.pos()
        '''
        Usamos mapFromGlobal para verificar si la posición actual del cursor (cursor_pos) se encuentra 
        dentro de las áreas q me enterezan Favoritos o Todos los Elemntos. Esto nos permite detectar 
        si el cursor está sobre un QLabel específico
        '''
        if self.selected_label:
            # Si hay un QLabel seleccionado
            if self.selected_label == self.Todos_elem:
                # El QLabel seleccionado es "Todos Los Elementos"
                if self.Favorit.rect().contains(self.Favorit.mapFromGlobal(cursor_pos)):
                    # El cursor está sobre "Favoritos" y cambia el ícono solo si no está seleccionado
                    self.iconFav.setIcon(QIcon('img/Star blue.png'))
                else:
                    # No está seleccionado, cambia el ícono de vuelta
                    self.iconFav.setIcon(QIcon('img/Star.png'))  
            elif self.selected_label == self.Favorit:
                # El QLabel seleccionado es "Favoritos"
                if self.Todos_elem.rect().contains(self.Todos_elem.mapFromGlobal(cursor_pos)):
                    # El cursor está sobre "Todos Los Elementos" y cambia el ícono solo si no está seleccionado
                    self.iconTodos.setIcon(QIcon('img/technology blue.png'))
                else:
                    # No está seleccionado, cambia el ícono de vuelta
                    self.iconTodos.setIcon(QIcon('img/technology.png'))  
        else:
            # No hay un QLabel seleccionado, simplemente actualiza los íconos según la posición del cursor
            if self.Todos_elem.rect().contains(self.Todos_elem.mapFromGlobal(cursor_pos)):
                self.iconTodos.setIcon(QIcon('img/technology blue.png'))
            else:
                self.iconTodos.setIcon(QIcon('img/technology.png'))

            if self.Favorit.rect().contains(self.Favorit.mapFromGlobal(cursor_pos)):
                self.iconFav.setIcon(QIcon('img/Star blue.png'))
            else:
                self.iconFav.setIcon(QIcon('img/Star.png'))


    def handle_item_selection(self):
    # Obtener el ítem actualmente seleccionado en la QList
        current_item = self.list.currentItem()

    # Si no hay ítem seleccionado o el ítem seleccionado es el mismo que el anteriormente seleccionado,
    # no hacer nada
        if not current_item or current_item == self.ultimoitem:
            return

    # Si hay un ítem previamente seleccionado, ocultar el lapiz en ese ítem
        if self.ultimoitem:
            item_widget_previo = self.list.itemWidget(self.ultimoitem)
            label_previo = item_widget_previo.findChild(QLabel, "titulo")
            lapiz_previo = item_widget_previo.findChild(QPushButton)
            if lapiz_previo:
                font_previo = label_previo.font()
                font_previo.setWeight(QFont.Normal)
                label_previo.setFont(font_previo)  # Actualizar la fuente en la etiqueta
                lapiz_previo.hide()
                icon_previo = QIcon('img/folder.png')  # Ícono gris (versión normal)
                item_widget_previo.findChild(QLabel, "icono").setPixmap(icon_previo.pixmap(24, 24))
                

    # Mostrar el lapiz en el ítem seleccionado actualmente
        item_widget = self.list.itemWidget(current_item)
        label_actual = item_widget.findChild(QLabel, "titulo")
        lapiz = item_widget.findChild(QPushButton)
        if lapiz:
            font_actual = label_actual.font()
            font_actual.setWeight(QFont.Bold)
            label_actual.setFont(font_actual)
            lapiz.show()
            icon_actual = QIcon('img/folder-blue.png')  # Ícono gris (versión normal)
            item_widget.findChild(QLabel, "icono").setPixmap(icon_actual.pixmap(24, 24))

    # Actualizar el ítem seleccionado
        self.ultimoitem = current_item


    def acept(self,input):
        '''Se ejecuta cuando el usuario acepta el cuadro de diálogo de edición de carpeta.
        Almacena el texto ingresado en la variable de instancia self.text y cierra el cuadro de diálogo.
        '''
        self.text= input.text()
        self.GeneradorC.accept()


    def __add_folder__(self):
        folder_name, ok = QInputDialog.getText(self, "Agregar Carpeta", "Nombre de la carpeta:")
        item_widget = QWidget()
        layout = QHBoxLayout(item_widget)
        if ok and folder_name:
            #os.makedirs(folder_name, exist_ok=True)
            icon_label = QLabel()
            icon_label.setObjectName("icono")
            icon = QIcon('img/folder.png')
            icon_label.setPixmap(icon.pixmap(24, 24))
            icon_label.setFixedWidth(25)
            name_label=QLabel(folder_name)
            name_label.setObjectName("titulo")
            layout.addWidget(icon_label)
            layout.addWidget(name_label)
            lapiz=QPushButton()
            lapiz.setIcon(QIcon('img/pencil.png'))
            Button_config(lapiz)
            lapiz.hide()
            layout.addWidget(lapiz)

            # Agregar la carpeta a la lista
            self.carp.append(item_widget)
            new_item = QListWidgetItem(self.list)
            new_item.setSizeHint(item_widget.sizeHint())
            self.list.setItemWidget(new_item, item_widget)
            

            # Conectar el evento de selección de la carpeta
            self.list.setCurrentItem(new_item)
            new_item.setSelected(True)
            # Conectar el evento de edición de la carpeta
            lapiz.clicked.connect(lambda: self.__edit_folder__(lapiz))
        # Emitir la señal cuando se crea una nueva carpeta
            self.aniadir.emit(folder_name)
            print(folder_name)


    def __edit_folder__(self, lapiz):
        #Obtengo el Indice del Elemento a editar
        indice = self.list.currentRow()
        self.actual=self.carp[indice].findChild(QLabel, "titulo").text()
        new_folder_name= self.cuadro_de_editar()
        self.list.item(indice).setText(new_folder_name)
        self.carp[indice].findChild(QLabel, "titulo").setText(new_folder_name)
        #os.rename(old_folder_name, new_folder_name)
        self.actualizar_nombre.emit(indice,new_folder_name)
        lapiz.parentWidget().layout().itemAt(1).widget().setText(new_folder_name) 




    def eliminar_carpeta(self,name):
        '''
        Elimina una carpeta cuando se presiona el botón de eliminar asociado.
        '''
        # Obtener la posición del ítem de la QListWidget asociado al botón "Eliminar"
        print (name)

        
        print([car.findChild(QLabel, "titulo").text() for car in self.carp])

        for index,carpeta in enumerate(self.carp):
            if carpeta.findChild(QLabel, "titulo").text() == name:
                self.list.takeItem(index)
                self.carp.pop(index)
                self.ultimoitem=None

        print([car.findChild(QLabel, "titulo").text() for car in self.carp])
        # Aceptar y cerrar el cuadro de diálogo, si es aplicable    
        self.GeneradorC.accept() 
        self.borrar.emit(self.actual)  




    def cuadro_de_editar(self):
        Enunciado=QLabel("Nombre de Carpeta")
        Input=QLineEdit(self.actual)
        ok_button = QPushButton("Aceptar")
        eliminar_button = QPushButton("Eliminar")
        botones=QGroupBox()
        B_layout=QHBoxLayout()
        B_layout.addWidget(ok_button)
        B_layout.addWidget(eliminar_button)
        botones.setLayout(B_layout)
        self.GeneradorC = QDialog()
        self.GeneradorC.setWindowTitle("Editar_Nombre")
        Elem = QVBoxLayout()
        Elem.addWidget(Enunciado)
        Elem.addWidget(Input)
        Elem.addWidget(botones)
        self.GeneradorC.setLayout(Elem)
        ok_button.clicked.connect(lambda: self.acept(Input))
        eliminar_button.clicked.connect(lambda:self.eliminar_carpeta(self.actual))
        # Ejecutar el cuadro de diálogo
        result = self.GeneradorC.exec()

        # Verificar si el cuadro de diálogo fue aceptado o cancelado
        if result == QDialog.Accepted:
            return self.text  # Devolver el texto ingresado
        else:
            return None  # Si se cancela el cuadro de diálogo, devolver None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Organizacion_datos()
    window.show()
    sys.exit(app.exec_())


'''
        font = icon_label.font()
        font.setWeight(QFont.Normal)
        icon_label.setStyleSheet(
            QLabel{
                color: white;
            }
            QLabel:hover {
                color:#001385;
            }
        )
        name_label.setStyleSheet(
            QLabel{
                color: white;
            }
            QLabel:hover {
                color:#001385;
            }
        )
'''