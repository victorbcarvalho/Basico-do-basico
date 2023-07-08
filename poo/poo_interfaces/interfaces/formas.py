from abc import ABC, abstractmethod   

class FormasInterfaces(ABC):
    
    @abstractmethod
    def get_perimetro(self) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def get_area(self) -> int:
        raise NotImplementedError
