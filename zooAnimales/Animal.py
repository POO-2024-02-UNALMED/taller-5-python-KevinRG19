from .Mamifero import Mamifero
from .Ave import Ave
from .Reptil import Reptil
from .Pez import Pez
from .Anfibio import Anfibio

class Animal:
    _totalAnimales = 0
    
    def __init__(self,nombre = '', edad = 0, habitat = '', genero = ''):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
        Animal._totalAnimales += 1

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_habitat(self):
        return self._habitat

    def set_habitat(self, habitat):
        self._habitat = habitat

    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    def get_zona(self):
        return self._zona

    def set_zona(self, zona):
        self._zona = zona

    @classmethod
    def totalPorTipo(cls):
        return (f'Mamiferos : {len(Mamifero._listado)}\nAves : {len(Ave._listado)}\nReptiles : {len(Reptil._listado)}\nPeces : {len(Pez._listado)}\nAnfibios : {len(Anfibio._listado)}')
    
    
    def __str__(self):
        if self._zona == []:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}")
        else:
            return(f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el zoo {self._zona._zoo._nombre}")

    def movimiento(self):
        return "desplazarse"
    
