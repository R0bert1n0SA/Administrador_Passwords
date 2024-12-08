import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana para que ocupe toda la pantalla
        self.showMaximized()


    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()  # Restaurar el tamaño normal
        else:
            self.showMaximized()  # Maximizar la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
