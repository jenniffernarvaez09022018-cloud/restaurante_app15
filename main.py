import os
import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante App - Semana 15")
        self.geometry("750x500")

        # Configurar icono del programa si existe en assets/
        ruta_icono = os.path.join("assets", "icon.png")
        if os.path.exists(ruta_icono) and os.path.getsize(ruta_icono) > 0:
            try:
                self.iconphoto(False, tk.PhotoImage(file=ruta_icono))
            except Exception:
                pass

        self.servicio = RestauranteServicio()
        self.mostrar_login()

    def mostrar_login(self):
        self.login_view = LoginView(self, on_login_success=self.mostrar_principal)

    def mostrar_principal(self):
        self.login_view.destroy()
        self.main_view = MainView(self, self.servicio)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()