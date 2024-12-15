import zooAnimales

class Animal:
    _totalAnimales = 0
    
    def __init__(self,nombre = '', edad = 0, habitat = '', genero = ''):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
        Animal._totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    @classmethod
    def totalPorTipo(cls):
        return (f'Mamiferos : {zooAnimales.mamifero.Mamifero.cantidadMamiferos()}\nAves : {zooAnimales.ave.Ave.cantidadAves()}\nReptiles : {zooAnimales.reptil.Reptil.cantidadReptiles()}\nPeces : {zooAnimales.pez.Pez.cantidadPeces()}\nAnfibios : {zooAnimales.anfibio.Anfibio.cantidadAnfibios()}')
    
    
    def __str__(self):
        if self._zona == []:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}")
        else:
            return(f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el zoo {self._zona._zoo._nombre}")

    def movimiento(self):
        return "desplazarse"
    
