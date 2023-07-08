from interfaces.formas import FormasInterfaces

class TerrenoQuadrado(FormasInterfaces):
    
    def __init__(self, lado: int):
        self.lado = lado
        
    def get_perimetro(self) -> int:
        perimetro = self.lado * 4
        return perimetro
    
    def get_area(self) -> int:
        area = self.lado * self.lado
        return area