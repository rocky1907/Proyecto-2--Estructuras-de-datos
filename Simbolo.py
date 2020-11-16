class Simbolo:
    def __init__(self, nombre, tipo=None):
        self.nombre=nombre
        self.tipo=tipo

    def get_nombre(self):
        return self.nombre

    def get_tipo (self):
        return self.tipo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_tipo (self, tipo):
        self.tipo = tipo


