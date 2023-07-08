class Casa:
    
    def __init__(self) -> None:
        self.__endereco = "Rua dos Limoeiros"
    
    def acender_luzes(self) -> None:
        print("Estou Acendendo as Luzes")
    
    def apresentar_local(self, local: any) -> None:
        return self.__endereco
