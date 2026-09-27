from datetime import datetime

class Venta:
    def __init__(self, usuario_id, producto_id, id=None, fecha=None):
        self.id = id or f"V-{int(datetime.now().timestamp())}"
        self.usuario_id = usuario_id
        self.producto_id = producto_id
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "producto_id": self.producto_id,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            usuario_id=data.get("usuario_id"),
            producto_id=data.get("producto_id"),
            fecha=data.get("fecha")
        )