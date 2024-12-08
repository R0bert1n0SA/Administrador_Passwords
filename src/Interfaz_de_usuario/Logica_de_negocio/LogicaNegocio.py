from PyQt5.QtCore import Qt,pyqtSignal,QObject
from Interfaz_de_usuario.pantalla_principal.Log_UI import *
from Interfaz_de_usuario.pantalla_principal.SignUp_UI import *
from Interfaz_de_usuario.Interior_App.InteriorAPP_UI import *
from Interfaz_de_usuario.pantalla_principal.RecuperarContra import *

class LogicaNegocio (QObject):
    def __init__(self):
        super().__init__()
        self.Users  =["admin"]
        self.Pasword=["password"]
        self.Acceso                = Log_UI()
        self.Registrar             = SignUp_UI()
        self.Interior              = Interior_app()
        self.RecuperarCount        = Recuperar() 
        self.Acceso.Ingreso.connect(self.Verificar)


#Log in Controller
    def Verificar(self):
        if (self.Acceso.Ingresar() != None):
            user=self.Acceso.Ingresar()[0]
            passw=self.Acceso.Ingresar()[1]
            if(user in self.Users)and(passw in self.Pasword):
                self.mostrar_aplicacion(self.Acceso,self.Interior)
            else:
                self.Acceso.Mensaje()


#sign up controlller
#