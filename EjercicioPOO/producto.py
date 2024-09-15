from Especificacion1 import Especificacion1
from Especificacion2 import Especificacion2
from alimento import alimento

class producto(Especificacion1, Especificacion2, alimento):
    codigo = 0
    def __init__(self):
        pass
    def getcodigo(self):
        return self.codigo
    def setcodigo(self, codigo):
        self.codigo = codigo