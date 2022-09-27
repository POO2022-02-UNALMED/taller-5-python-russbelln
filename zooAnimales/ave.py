from animal import Animal
from gestion.Zona import Zona
from gestion.Zoologico import Zoologico

class Ave(Animal):
    aguilas = 0
    halcones = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
        
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "volar"
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas +=1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones +=1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso") 
    
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado =listado
        
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
        
    