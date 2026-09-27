import os
import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Frame):
    def __init__(self, parent, restaurante_servicio):
        super().__init__(parent)
        self.servicio = restaurante_servicio
        self.pack(fill="both", expand=True)

        # Cargar Logo desde assets/ si existe y no está vacío
        try:
            ruta_logo = os.path.join("assets", "logo.png")
            if os.path.exists(ruta_logo) and os.path.getsize(ruta_logo) > 0:
                self.logo_img = tk.PhotoImage(file=ruta_logo)
                tk.Label(self, image=self.logo_img).pack(pady=5)
            else:
                tk.Label(self, text="🍽️ RESTAURANTE APP", font=("Arial", 16, "bold")).pack(pady=10)
        except Exception:
            tk.Label(self, text="🍽️ RESTAURANTE APP", font=("Arial", 16, "bold")).pack(pady=10)

        # Sistema de Pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_usuarios = ttk.Frame(self.notebook)
        self.tab_productos = ttk.Frame(self.notebook)
        self.tab_ventas = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_usuarios, text=" Usuarios ")
        self.notebook.add(self.tab_productos, text=" Productos ")
        self.notebook.add(self.tab_ventas, text=" Ventas ")

        self.crear_seccion_usuarios()
        self.crear_seccion_productos()
        self.crear_seccion_ventas()

    def crear_seccion_usuarios(self):
        tabla_u = ttk.Treeview(self.tab_usuarios, columns=("ID", "Nombre", "Rol"), show="headings")
        tabla_u.heading("ID", text="ID")
        tabla_u.heading("Nombre", text="Nombre")
        tabla_u.heading("Rol", text="Rol")
        tabla_u.pack(fill="both", expand=True, padx=10, pady=10)

        for u in self.servicio.obtener_usuarios():
            tabla_u.insert("", "end", values=(u.id, u.nombre, u.rol))

    def crear_seccion_productos(self):
        tabla_p = ttk.Treeview(self.tab_productos, columns=("ID", "Nombre", "Precio"), show="headings")
        tabla_p.heading("ID", text="ID")
        tabla_p.heading("Nombre", text="Nombre")
        tabla_p.heading("Precio", text="Precio ($)")
        tabla_p.pack(fill="both", expand=True, padx=10, pady=10)

        for p in self.servicio.obtener_productos():
            tabla_p.insert("", "end", values=(p.id, p.nombre, f"${p.precio:.2f}"))

    def crear_seccion_ventas(self):
        frame_form = ttk.LabelFrame(self.tab_ventas, text=" Registrar Nueva Venta ", padding=10)
        frame_form.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_form, text="Usuario:").grid(row=0, column=0, padx=5, pady=5)
        self.combo_usuarios = ttk.Combobox(frame_form, state="readonly", width=25)
        self.combo_usuarios.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Producto:").grid(row=0, column=2, padx=5, pady=5)
        self.combo_productos = ttk.Combobox(frame_form, state="readonly", width=25)
        self.combo_productos.grid(row=0, column=3, padx=5, pady=5)

        # Uso correcto de command= asociando el callback sin paréntesis
        btn_registrar = ttk.Button(
            frame_form,
            text="Registrar Venta",
            command=self.callback_registrar_venta
        )
        btn_registrar.grid(row=0, column=4, padx=10, pady=5)

        # Tabla de Ventas (Treeview)
        self.tabla_ventas = ttk.Treeview(
            self.tab_ventas,
            columns=("ID", "Usuario", "Producto", "Fecha"),
            show="headings"
        )
        self.tabla_ventas.heading("ID", text="ID Venta")
        self.tabla_ventas.heading("Usuario", text="ID Usuario")
        self.tabla_ventas.heading("Producto", text="ID Producto")
        self.tabla_ventas.heading("Fecha", text="Fecha de Registro")

        self.tabla_ventas.column("ID", width=120)
        self.tabla_ventas.column("Usuario", width=100)
        self.tabla_ventas.column("Producto", width=100)
        self.tabla_ventas.column("Fecha", width=180)

        self.tabla_ventas.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_comboboxes()
        self.actualizar_tabla_ventas()

    def cargar_comboboxes(self):
        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        self.combo_usuarios["values"] = [f"{u.id} - {u.nombre}" for u in usuarios]
        self.combo_productos["values"] = [f"{p.id} - {p.nombre} (${p.precio:.2f})" for p in productos]

    def callback_registrar_venta(self):
        """Callback: Obtiene datos de la UI y delega la operación al servicio"""
        usuario_sel = self.combo_usuarios.get()
        producto_sel = self.combo_productos.get()

        u_id = usuario_sel.split(" - ")[0] if usuario_sel else ""
        p_id = producto_sel.split(" - ")[0] if producto_sel else ""

        # Delegación al servicio
        exito, mensaje = self.servicio.registrar_venta(u_id, p_id)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_tabla_ventas()
        else:
            messagebox.showwarning("Atención", mensaje)

    def actualizar_tabla_ventas(self):
        """Refresca el Treeview trayendo los datos guardados mediante el servicio"""
        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        ventas = self.servicio.obtener_ventas()
        for v in ventas:
            self.tabla_ventas.insert("", "end", values=(v.id, v.usuario_id, v.producto_id, v.fecha))