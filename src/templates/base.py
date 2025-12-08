from abc import ABC, abstractmethod
from typing import Dict, Any
import json
from datetime import datetime

class Template(ABC):
    """Base class for all templates"""
    
    @abstractmethod
    def render(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Render template with data"""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Template name"""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Template description"""
        pass
    
    def validate_data(self, data: Dict[str, Any], required_fields: list) -> bool:
        """Check if data has required fields"""
        missing = [field for field in required_fields if field not in data]
        if missing:
            print(f"⚠️  Missing fields for {self.name}: {missing}")
            return False
        return True
    
    def add_metadata(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Add metadata to rendered content"""
        return {
            "page_type": self.name,
            "generated_at": datetime.now().isoformat(),
            "template_version": "1.0",
            "content": content
        }