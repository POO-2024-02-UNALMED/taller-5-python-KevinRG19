from zooAnimales.animal import Animal

class Mamifero(Animal):

    _listado = []
    caballos = 0
    leones = 0
    
    def __init__(self, nombre = '', edad = 0, habitat = '', genero = '', pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero._listado)
    
    def getPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas
    
    @classmethod
    def crearCaballo(cls, nombre = '', edad = 0, genero = ''):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, 'pradera', genero, True, 4)
    
    @classmethod
    def crearLeon(cls, nombre = '', edad = 0, genero = ''):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, 'selva', genero, True, 4)
    
        


    