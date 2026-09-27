# Restaurante App - Sistema Modular de Gestión de Ventas (Semana 15)

## 📌 Propósito del Proyecto
Este proyecto corresponde a la evolución modular del sistema `restaurante_app` para la asignatura de Programación Orientada a Objetos[cite: 8]. Su objetivo principal es demostrar la comprensión e implementación de los **fundamentos básicos del manejo de eventos** utilizando la librería `tkinter` de Python, aplicando una separación clara de responsabilidades entre la interfaz gráfica (UI), la capa de servicios y la persistencia de datos en archivos JSON[cite: 8].

---

## 🏗️ Arquitectura y Estructura del Sistema
El proyecto mantiene una arquitectura en capas, garantizando que la lógica de negocio y la lectura/escritura de archivos no se encuentren concentradas dentro de la interfaz gráfica[cite: 8]:

```text
restaurante_app15/
│
├── assets/                  # Recursos visuales obligatorios (íconos y logotipo)
│   ├── icon.png
│   └── logo.png
│
├── datos/                   # Persistencia de datos en formato JSON
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/                 # Entidades del dominio del restaurante
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/               # Lógica de negocio y persistencia
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/                      # Vistas y componentes de la interfaz de usuario
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py                  # Punto de entrada de la aplicación
└── README.md                # Documentación del proyecto
```

---

## 🔄 Flujo de Control y Manejo de Eventos

El registro de una venta sigue el flujo de eventos solicitado en la arquitectura[cite: 13]:

1. **Acción del Usuario:** El usuario selecciona un cliente en el `Combobox` de usuarios y un plato/bebida en el `Combobox` de productos[cite: 13].
2. **Disparo del Evento (`command=`):** Al hacer clic en el botón **"Registrar Venta"**, se activa la asociación mediante `command=self.callback_registrar_venta` (asociado a la función callback sin ejecutarla explícitamente con paréntesis)[cite: 13].
3. **Callback:** La función `callback_registrar_venta()` recolecta las selecciones de la vista[cite: 13].
4. **Delegación al Servicio:** El callback delega la validación y el procesamiento a `RestauranteServicio.registrar_venta()`[cite: 13].
5. **Persistencia:** `RestauranteServicio` utiliza `ArchivoServicio` para actualizar y conservar el nuevo registro dentro de `datos/ventas.json`[cite: 13].
6. **Respuesta Visual:** El servicio retorna el resultado de la operación[cite: 13]. La interfaz muestra un mensaje de confirmación (`messagebox`) y refresca inmediatamente la tabla `Treeview` de ventas[cite: 13].

---

## 🚀 Instrucciones de Ejecución

### Requisitos Previos
* Tener instalado Python 3.10 o superior[cite: 8].
* Contar con las imágenes `icon.png` y `logo.png` guardadas dentro de la carpeta `assets/`[cite: 8].

### Pasos para Ejecutar
1. Abre una terminal dentro de la carpeta raíz del proyecto (`restaurante_app15/`)[cite: 8].
2. Ejecuta el comando[cite: 8]:
   ```bash
   python main.py
   ```
3. Ingresa las credenciales de inicio de sesión de prueba[cite: 8]:
   * **Usuario:** `admin`[cite: 8]
   * **Clave:** `1234`[cite: 8]