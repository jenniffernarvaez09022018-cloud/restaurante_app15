class Usuario:
    def __init__(self, id, nombre, rol="Cliente"):
        self.id = id
        self.nombre = nombre
        self.rol = rol

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "rol": self.rol
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            nombre=data.get("nombre"),
            rol=data.get("rol", "Cliente")
        )