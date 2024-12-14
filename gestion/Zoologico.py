from .zona import Zona

class Zoologico:
    
    def __init__(self, nombre = '', ubicacion = '', zonas = None):
        self._nombre = nombre
        self._ubicacion = ubicacion 
        self._zonas = []

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getUbicacion(self):
        return self._ubicacion
    
    def setZonas(self, zonas):
        self._zonas = zonas

    def getZonas(self):
        return self._zonas
    
    def cantidadTotalAnimales(self):
        cantidad = 0
        for i in range(self._zonas):
            if isinstance(i, Zona):
                cantidad += len(i._animales)
        return cantidad

    def agregarZonas(self, Zona):
        self._zonas.append(Zona)
        Zona._zoo = self


        
                
        


