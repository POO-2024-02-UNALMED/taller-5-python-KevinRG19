from .Animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', colorPiel = '', venenoso = False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def movimiento(self):
        return "saltar"
    
    def cantidadAnfibios(self):
        return len(Anfibio._listado)

    @classmethod
    def crearRana(cls, nombre = '', edad = 0, genero = ''):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, 'selva', genero, 'rojo', True)
    
    @classmethod
    def crearSalamandra(cls, nombre = '', edad = 0, genero = ''):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, 'selva', genero, 'negro y amarillo', False)