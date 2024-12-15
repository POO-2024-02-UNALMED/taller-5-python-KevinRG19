from zooAnimales.animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', colorPlumas = ''):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def movimiento(self):
        return "volar"
    
    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    def cantidadAves(self):
        return len(Ave._listado)
    
    @classmethod
    def crearHalcon(cls, nombre = '', edad = 0, genero = ''):
        Ave.halcones += 1
        Ave(nombre, edad, 'montanas', genero, 'cafe glorioso')

    @classmethod
    def crearAguila(cls, nombre = '', edad = 0, genero = ''):
        Ave.aguilas += 1
        Ave(nombre, edad, 'montanas', genero, 'blanco y amarillo')