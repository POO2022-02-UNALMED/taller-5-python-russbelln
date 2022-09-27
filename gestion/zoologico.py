

class Zoologico():
    def __init__(self, nombre, ubicacion, zonas=[]):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self):
        t = 0
        q = 0
        while q < len(self._zonas):
            t += self._zonas[q].cantidadAnimales()
            q += 1
        return t
            
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
        
    def getZona(self):
        return self._zonas
    def setZona(self, zonas):
        self._zonas=zonas
        
        