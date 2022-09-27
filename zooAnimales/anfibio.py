from animal import Animal


class Anfibio(Animal):
    salamandras = 0
    ranas = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso, zona=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
        
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas +=1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
    
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras +=1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False) 
    
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls, listado):
        cls._listado =listado
        
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
        
    def isVenenoso(self):
        return self._venenoso
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    
        
    
    