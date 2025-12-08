from typing import Dict, Any
from ..models.product import ProductData

class ParserAgent:
    def __init__(self):
        self.agent_name = "ParserAgent"
        self.description = "Parses and validates raw product data"
        
    def process(self, raw_data: Dict[str, Any]) -> ProductData:
        print(f"🔧 [{self.agent_name}] Processing raw data...")
        
        cleaned_data = self._clean_raw_data(raw_data)
        product = ProductData(**cleaned_data)
        
        print(f"✅ [{self.agent_name}] Successfully parsed product: {product.name}")
        return product
    
    def _clean_raw_data(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        cleaned = {}
        
        field_mapping = {
            "Product Name": "name",
            "Concentration": "concentration", 
            "Skin Type": "skin_type",
            "Key Ingredients": "key_ingredients",
            "Benefits": "benefits",
            "How to Use": "how_to_use",
            "Side Effects": "side_effects",
            "Price": "price"
        }
        
        for raw_field, model_field in field_mapping.items():
            if raw_field in raw:
                value = raw[raw_field]
                
                if raw_field in ["Skin Type", "Key Ingredients", "Benefits"]:
                    if isinstance(value, str):
                        cleaned[model_field] = [item.strip() for item in value.split(",")]
                    else:
                        cleaned[model_field] = value
                else:
                    cleaned[model_field] = value
        
        return cleaned
    
    def get_status(self) -> Dict[str, Any]:
        return {
            "agent": self.agent_name,
            "status": "ready",
            "description": self.description
        }