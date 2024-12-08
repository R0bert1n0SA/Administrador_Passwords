from PyQt5.QtWidgets import QAction,QMenuBar ,QMenu, QWidget, QVBoxLayout
def Menu():
    # Crear una instancia de QMenuBar
        menu_bar =QMenuBar()
        menu_bar.setStyleSheet('''
            QMenuBar{
                background-color: blue;
                color: white;
            }
        ''')

        # Crear un menú "Archivo"
        archivo = menu_bar.addMenu("Archivo")
        editar = menu_bar.addMenu("Editar")
        ver = menu_bar.addMenu("Ver")
        cuenta = menu_bar.addMenu("Cuenta")
        ventana=menu_bar.addMenu("Ventana")
        ayuda=menu_bar.addMenu("Ayuda")
        return menu_bar