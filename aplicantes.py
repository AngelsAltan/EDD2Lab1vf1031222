import json
class aplicantes_:
    def __init__(self, nombre, dpi, fechaNacimiento, direccion):
        self.nombre = nombre
        self.dpi = dpi
        self.fechaNacimiento = fechaNacimiento
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre}, dpi: {self.dpi}, fechaNacimiento: {self.fechaNacimiento}, direccion: {self.direccion}"

    @classmethod
    def from_json(cls, json_str):
        f = json.loads(json_str)
        return cls(f["name"], f["dpi"], f["datebirth"], f["address"])