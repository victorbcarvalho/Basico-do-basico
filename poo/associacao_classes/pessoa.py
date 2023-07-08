from interruptor import Interruptor
from typing import Type

class Pessoa:
    
    def acender_luz(self, interruptor: Type[Interruptor]) -> None:
        interruptor.acender()
    
    def apagar_luz(self, interruptor: Type[Interruptor]) -> None:
        interruptor.apagar()
        
    def dormir(self) -> None:
        print("Foi dormir")
        
victor = Pessoa()
interruptror_quarto = Interruptor("quarto")

interruptror_quarto.acender()
victor.acender_luz(interruptror_quarto)