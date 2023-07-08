class MinhaClasse:
    
    variavel_de_classe = "Olá"
    
    def __init__(self, atributo_publico: str) -> None:
        self.atributo_publico = atributo_publico
        self.__atributo_privado = False
        
    def metodo_publico(self) -> None:
        pass
    
    def __metodo_privado(self) -> int:
        pass
    
    @staticmethod
    def metodo_estatico() -> None:
        pass