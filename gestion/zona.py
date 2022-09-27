from zooAnimales.anfibio import Anfibio
from zooAnimales.pez import Pez
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.reptil import Reptil
from zoologico import Zoologico

class Zona():
    def __init__(self, nombre, zoo, animales = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = animales
        
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        animal.setZona(self)
        
    def cantidadAnimales(self):
        return len(self._animales)
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getZoo(self):
        return self._zoo
    def setZoo(self, zoo):
        self._zoo = zoo
        
    def getAnimales(self):
        return self._animales
    def setAnimales(self, animales):
        self._animales = animales
        
    