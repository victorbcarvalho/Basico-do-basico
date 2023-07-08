class Mae:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = "Carvalho"
    
    def comer(self) -> None:
        print("Estou comendo.")
    
    def estudar(self) -> None:
        print("Estudar estudando.")


class Filha(Mae):
    
    def __init__(self, endereco) -> None:
        super().__init__(endereco)

    def brincar(self) -> None:
        print("Estou brincando.")

class Neta(Filha):
    
    def __init__(self, endereco) -> None:
        super().__init__(endereco)
    

    
Claudineia = Mae("Rua das Loucuras")
Claudinuza = Filha("Rua das Loucuras")
Claudinaria = Neta("Rua da Normalidade")

Claudineia.endereco
Claudinuza.endereco
Claudinaria.endereco

Claudinaria.brincar()
Claudinaria.estudar()

Claudinuza.comer()