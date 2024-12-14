from .animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', colorEscamas = '', largoCola = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def movimiento(self):
        return "reptar"
    
    def cantidadReptiles(self):
        return len(Reptil._listado)
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setLargoCola(self, largo):
        self._largoCola = largo
    
    def getLargoCola(self):
        return self._largoCola
    
    @classmethod
    def crearIguana(cls, nombre = '', edad = 0, genero = ''):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, 'humedad', genero, 'verde', 3)
    
    @classmethod
    def crearSerpiente(cls, nombre = '', edad = 0, genero = ''):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, 'jungla', genero, 'blanco', 1)