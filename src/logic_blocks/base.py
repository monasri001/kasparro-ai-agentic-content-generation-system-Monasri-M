from abc import ABC, abstractmethod
from typing import Dict, Any
from ..models.product import ProductData

class ContentLogicBlock(ABC):
    """Base class for all content logic blocks"""
    
    @abstractmethod
    def apply(self, product: ProductData) -> Dict[str, Any]:
        """Transform product data into content"""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Unique name for the block"""
        pass
    
    def get_info(self) -> Dict[str, Any]:
        """Get block information"""
        return {
            "name": self.name,
            "description": self.__doc__ or "No description"
        }