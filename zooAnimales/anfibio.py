from zooAnimales.animal import Animal

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
    
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio._listado)

    @classmethod
    def crearRana(cls, nombre = '', edad = 0, genero = ''):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, 'selva', genero, 'rojo', True)
    
    @classmethod
    def crearSalamandra(cls, nombre = '', edad = 0, genero = ''):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, 'selva', genero, 'negro y amarillo', False)