from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.on_login_success = on_login_success
        self.pack(fill="both", expand=True)

        # Contenedor central
        frame_login = ttk.LabelFrame(self, text=" Acceso al Sistema ", padding=20)
        frame_login.pack(expand=True, padx=20, pady=20)

        tk.Label(frame_login, text="Usuario:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_user = tk.Entry(frame_login)
        self.entry_user.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_login, text="Clave:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_pass = tk.Entry(frame_login, show="*")
        self.entry_pass.grid(row=1, column=1, padx=5, pady=5)

        btn_ingresar = tk.Button(
            frame_login, 
            text="Iniciar Sesión", 
            command=self.validar_credenciales, 
            bg="#2196F3", 
            fg="white", 
            font=("Arial", 10, "bold")
        )
        btn_ingresar.grid(row=2, column=0, columnspan=2, pady=15)

    def validar_credenciales(self):
        usuario = self.entry_user.get().strip()
        clave = self.entry_pass.get().strip()

        if usuario == "admin" and clave == "1234":
            self.on_login_success()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.\nUse: admin / 1234")