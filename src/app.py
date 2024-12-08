import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout,QSizePolicy
from Principal.Log_in import *
from Principal.Interfaz_de_registro import Sign_upWindow
from Principal.BarraMenu import *
from Interior.aplicacion import Interfaz



class PasswordManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setStyleSheet("""
            QWidget {
                background-color: gray;
            }
        """)
        self.setWindowTitle("SecurityBox")
        icono = QIcon("img/Logo.png")
        self.setWindowIcon(icono)
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()
        self.setMinimumSize(800, 300)  # Establecer tamaño mínimo
        self.setMaximumSize(1600, 1200)  # Establecer tamaño máximo


        self.menu_bar = Menu()
        self.setMenuBar(self.menu_bar)

        login_window = Log_inWindow()
        signup_window = Sign_upWindow()
        principal=Interfaz()


        self.stacked_widget.addWidget(login_window)
        self.stacked_widget.addWidget(signup_window)
        self.stacked_widget.addWidget(principal)

        login_window.signup_button_clicked.connect(self.mostrar_registro)
        login_window.Login.connect(self.mostrar_aplicacion)
        signup_window.login_button_clicked.connect(self.mostrar_login)


    def mostrar_registro(self):
        self.stacked_widget.setCurrentIndex(1)


    def mostrar_login(self):
        self.stacked_widget.setCurrentIndex(0)



    def mostrar_aplicacion(self):
        self.stacked_widget.setCurrentIndex(2)





if __name__ == '__main__':
    app = QApplication([])
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec_())


