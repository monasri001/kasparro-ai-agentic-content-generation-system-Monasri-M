from typing import Dict, Any
from .base import ContentLogicBlock
from ..models.product import ProductData

class IngredientAnalyzerBlock(ContentLogicBlock):
    """
    Analyzes and explains key ingredients.
    """
    
    INGREDIENT_DESCRIPTIONS = {
        "Vitamin C": {
            "benefit": "Powerful antioxidant that brightens skin",
            "purpose": "Fights free radicals, boosts collagen",
            "key_feature": "10% concentration for optimal efficacy"
        },
        "Hyaluronic Acid": {
            "benefit": "Intense hydration without heaviness",
            "purpose": "Locks in moisture, plumps skin",
            "key_feature": "Holds 1000x its weight in water"
        }
    }
    
    @property
    def name(self):
        return "analyze-ingredients-block"
    
    def apply(self, product: ProductData) -> Dict[str, Any]:
        ingredient_details = []
        
        for ingredient in product.key_ingredients:
            if ingredient in self.INGREDIENT_DESCRIPTIONS:
                details = self.INGREDIENT_DESCRIPTIONS[ingredient].copy()
                details["name"] = ingredient
                ingredient_details.append(details)
            else:
                ingredient_details.append({
                    "name": ingredient,
                    "benefit": "Provides skincare benefits",
                    "purpose": "Key active ingredient",
                    "key_feature": "Essential component"
                })
        
        return {
            "ingredients": ingredient_details,
            "total_actives": len(ingredient_details),
            "key_ingredient": ingredient_details[0]["name"] if ingredient_details else "",
            "concentration": product.concentration
        }