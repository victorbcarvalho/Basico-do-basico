class Pessoa:
    
    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        
    # def print_cpf(self):
    #     print(self.__cpf)
    
    def correr(self) -> None:
        print("Estou correndo")
        
    def beber(self, bebida: str) -> None:
        if bebida == "Cerveja":
            self.__apresentar_documento()
        print("Bebendo...")
                
    def __apresentar_documento(self) -> None:
        print(self.__cpf)
        
ronaldo = Pessoa("Ronaldo", 34, "234.fhj.453-45")
print(ronaldo.nome)
print(ronaldo.idade)
#print(ronaldo.__cpf)
#ronaldo.print_cpf()
ronaldo.beber("Cerveja")
ronaldo.beber("Coca-cola")