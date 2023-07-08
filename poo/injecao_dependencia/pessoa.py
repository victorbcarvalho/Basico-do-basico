from casa import Casa
from typing import Type

class Pessoa:
    
    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__local = local
        self.__nome = nome
    
    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()
    
    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)

casa_de_amigo = Casa()
ana = Pessoa("Ana", casa_de_amigo)

ana.entrar_no_local()
ana.apresentar_local()