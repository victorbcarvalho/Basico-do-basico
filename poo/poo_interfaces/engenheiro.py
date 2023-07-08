from typing import Type 
from interfaces.formas import FormasInterfaces

class Engenheiro:
    
    def __init__(self, name: str) -> None:
        self.nome = name
    
    def medir_perimetro(self, terreno: Type[FormasInterfaces]) -> int:
        perimetro = terreno.get_perimetro()
        return perimetro
    
    def medir_area(self, terreno: Type[FormasInterfaces]) -> int:
        area = terreno.get_area()
        return area
    