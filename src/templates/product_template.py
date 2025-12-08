from typing import Dict, Any
from .base import Template

class ProductPageTemplate(Template):
    """Template for detailed product description page"""
    
    @property
    def name(self):
        return "product_page"
    
    @property
    def description(self):
        return "Complete product description page with specifications"
    
    def render(self, data: Dict[str, Any]) -> Dict[str, Any]:
        print(f"🔧 [{self.name.upper()} Template] Rendering Product Page...")
        
        required = ["product_info", "content_blocks"]
        if not self.validate_data(data, required):
            return {"error": "Missing required data for Product template"}
        
        product = data["product_info"]
        blocks = data["content_blocks"]
        
        # Build product page
        product_page = {
            "header": {
                "title": product["name"],
                "tagline": f"Advanced {product.get('concentration', '')} Serum",
                "short_description": f"A premium serum designed for {', '.join(product.get('skin_type', []))} skin"
            },
            "overview": {
                "description": self._generate_description(product, blocks),
                "key_benefits": blocks.get("benefits", {}).get("primary_benefits", []),
                "ideal_for": product.get("skin_type", [])
            },
            "specifications": {
                "concentration": product.get("concentration", ""),
                "key_ingredients": [
                    {
                        "name": ing["name"],
                        "benefit": ing.get("benefit", ""),
                        "purpose": ing.get("purpose", "")
                    }
                    for ing in blocks.get("ingredients", {}).get("ingredients", [])
                ],
                "texture": "Lightweight, fast-absorbing",
                "fragrance": "Unscented",
                "size": "30ml"
            },
            "usage": {
                "instructions": blocks.get("usage", {}).get("steps", []),
                "frequency": blocks.get("usage", {}).get("frequency", "Daily"),
                "best_time": blocks.get("usage", {}).get("best_time", "Morning")
            },
            "safety": {
                "warnings": blocks.get("safety", {}).get("warnings", []),
                "recommendations": blocks.get("safety", {}).get("recommendations", []),
                "patch_test": blocks.get("safety", {}).get("patch_test", True)
            },
            "pricing": {
                "price": blocks.get("price", {}).get("display_price", ""),
                "value": blocks.get("price", {}).get("value_rating", ""),
                "category": blocks.get("price", {}).get("price_category", "")
            },
            "metadata": {
                "sku": f"SKU-{product['name'].replace(' ', '-').upper()}",
                "category": "Face Serums",
                "rating": "4.5/5",
                "reviews_count": "150+"
            }
        }
        
        print(f"✅ [{self.name.upper()} Template] Product page generated")
        return self.add_metadata(product_page)
    
    def _generate_description(self, product: Dict, blocks: Dict[str, Any]) -> str:
        """Generate product description"""
        ingredients = blocks.get("ingredients", {})
        benefits = blocks.get("benefits", {})
        
        return f"{product['name']} is a {product.get('concentration', '')} serum " \
               f"featuring {ingredients.get('total_actives', 0)} key active ingredients. " \
               f"Formulated for {', '.join(product.get('skin_type', []))} skin types, " \
               f"it delivers {', '.join(benefits.get('primary_benefits', ['multiple benefits']))}. " \
               f"Perfect for daily use in your morning skincare routine."