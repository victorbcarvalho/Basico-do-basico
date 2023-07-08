class MinhaClasse:
    
    def __init__(self, atributo) -> None:
        self.meu_atributo = "Olá, Mundo!"
        self.meu_atributo2 = atributo
        
    def meu_metodo(self) -> None:
        print(self.meu_atributo)
        print(self.meu_atributo2)
        
    def meu_metodo2(self, num, mult) -> int:
        return num * mult

objeto = MinhaClasse("Olá, mundo! Como vai?")
objeto.meu_metodo()
objeto.meu_atributo