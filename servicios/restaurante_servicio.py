from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self):
        self.ruta_productos = "datos/productos.json"
        self.ruta_usuarios = "datos/usuarios.json"
        self.ruta_ventas = "datos/ventas.json"

    def obtener_usuarios(self):
        datos = ArchivoServicio.cargar_json(self.ruta_usuarios)
        return [Usuario.from_dict(u) for u in datos]

    def obtener_productos(self):
        datos = ArchivoServicio.cargar_json(self.ruta_productos)
        return [Producto.from_dict(p) for p in datos]

    def obtener_ventas(self):
        datos = ArchivoServicio.cargar_json(self.ruta_ventas)
        return [Venta.from_dict(v) for v in datos]

    def registrar_venta(self, usuario_id, producto_id):
        if not usuario_id or not producto_id:
            return False, "Debe seleccionar un usuario y un producto válidos."

        # Validaciones de existencia dentro del servicio
        usuarios = [u.id for u in self.obtener_usuarios()]
        productos = [p.id for p in self.obtener_productos()]

        if usuario_id not in usuarios:
            return False, f"El usuario {usuario_id} no existe."
        if producto_id not in productos:
            return False, f"El producto {producto_id} no existe."

        ventas = self.obtener_ventas()
        nueva_venta = Venta(usuario_id, producto_id)
        ventas.append(nueva_venta)

        datos_guardar = [v.to_dict() for v in ventas]
        ArchivoServicio.guardar_json(self.ruta_ventas, datos_guardar)

        return True, f"¡Venta {nueva_venta.id} registrada exitosamente!"