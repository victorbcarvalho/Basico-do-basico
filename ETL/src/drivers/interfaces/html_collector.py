from typing import Dict, List
from abc import ABC, abstractmethod

class HtmlCollectorInterface(ABC):
    
    @abstractmethod
    def collect_essential_information(self, html: str) -> List[Dict[str,str]]:
        pass