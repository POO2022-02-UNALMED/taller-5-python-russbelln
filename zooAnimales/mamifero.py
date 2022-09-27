from animal import Animal
from gestion.zona import Zona
from gestion.zoologico import Zoologico

class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
        
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos +=1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    
    def crearLeon(cls, nombre, edad, genero):
        cls.leones +=1
        return Mamifero(nombre, edad, "oceano", genero, True, 4) 
    
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado =listado
        
    def getPelaje(self):
        return self._pelaje
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
        
    def getPatas(self):
        return self._cantidadAletas
    def setPatas(self, patas):
        self._patas = patas