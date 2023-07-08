class MinhaClasse:
    
    estatico = "Victor" 
    
    def __init__(self, estado):
        self.estado = estado
        
    def print_estatico(self):
        print(self.estatico)
    
    @classmethod
    def mudar_estatico(cls):
        cls.estatico = "Bastos"

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)
obj1.mudar_estatico()
obj2.print_estatico()
