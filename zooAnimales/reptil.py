from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes= 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
        
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero=None):
        Reptil.iguanas +=1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero=None):
        Reptil.serpientes +=1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1) 
    
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado =listado
        
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getLargoCola(self):
        return self._largoCola
    def setVenenoso(self, largoCola):
        self._largoCola = largoCola
    