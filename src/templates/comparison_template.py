from typing import Dict, Any
from datetime import datetime
from .base import Template

class ComparisonTemplate(Template):
    """Template for product comparison page"""
    
    @property
    def name(self):
        return "comparison_page"
    
    @property
    def description(self):
        return "Product comparison page (Product A vs Product B)"
    
    def render(self, data: Dict[str, Any]) -> Dict[str, Any]:
        print(f"🔧 [{self.name.upper()} Template] Rendering Comparison Page...")
        
        required = ["product_a", "content_blocks"]
        if not self.validate_data(data, required):
            return {"error": "Missing required data for Comparison template"}
        
        product_a = data["product_a"]
        blocks = data["content_blocks"]
        
        # Create fictional Product B for comparison
        product_b = self._create_fictional_product(product_a)
        
        # Build comparison
        comparison_page = {
            "title": f"Comparison: {product_a['name']} vs {product_b['name']}",
            "summary": f"Comparing two popular vitamin C serums for different needs",
            "products": [
                self._format_product(product_a, blocks, "A"),
                self._format_product(product_b, {}, "B")
            ],
            "key_differences": [
                {
                    "aspect": "Price",
                    "product_a": blocks.get("price", {}).get("display_price", ""),
                    "product_b": product_b["price"],
                    "winner": "B" if self._extract_price(product_b["price"]) < self._extract_price(blocks.get("price", {}).get("display_price", "₹0")) else "A"
                },
                {
                    "aspect": "Key Ingredients",
                    "product_a": f"{len(blocks.get('ingredients', {}).get('ingredients', []))} actives",
                    "product_b": f"{len(product_b['ingredients'])} key ingredients",
                    "winner": "A" if len(blocks.get('ingredients', {}).get('ingredients', [])) > len(product_b['ingredients']) else "B"
                },
                {
                    "aspect": "Best For",
                    "product_a": ", ".join(product_a.get("skin_type", [])),
                    "product_b": "All skin types, especially sensitive",
                    "winner": "Depends on skin type"
                }
            ],
            "recommendation": self._generate_recommendation(product_a, product_b, blocks),
            "disclaimer": "Product B is fictional for demonstration. Always patch test new products."
        }
        
        print(f"✅ [{self.name.upper()} Template] Comparison with fictional product generated")
        return self.add_metadata(comparison_page)
    
    def _create_fictional_product(self, product_a: Dict) -> Dict[str, Any]:
        """Create a fictional product for comparison"""
        return {
            "name": "DermaGlow Vitamin E Serum",
            "ingredients": ["Vitamin E", "Niacinamide", "Green Tea Extract"],
            "benefits": ["Hydration", "Reduces Redness", "Antioxidant Protection"],
            "price": "₹899",
            "concentration": "5% Vitamin E",
            "skin_type": ["All", "Sensitive", "Dry"],
            "key_feature": "Gentle formula for sensitive skin"
        }
    
    def _format_product(self, product: Dict, blocks: Dict[str, Any], label: str) -> Dict[str, Any]:
        """Format product for comparison table"""
        if label == "A":
            # Real product with content blocks
            return {
                "name": product["name"],
                "label": "Our Product",
                "price": blocks.get("price", {}).get("display_price", ""),
                "key_ingredients": [ing["name"] for ing in blocks.get("ingredients", {}).get("ingredients", [])],
                "benefits": blocks.get("benefits", {}).get("primary_benefits", []),
                "best_for": product.get("skin_type", []),
                "concentration": product.get("concentration", ""),
                "value_rating": blocks.get("price", {}).get("value_rating", ""),
                "pros": ["Higher Vitamin C concentration", "Multiple brightening benefits", "Competitive pricing"],
                "cons": ["May cause tingling for very sensitive skin", "Specific to oily/combination skin"]
            }
        else:
            # Fictional product
            return {
                "name": product["name"],
                "label": "Alternative",
                "price": product["price"],
                "key_ingredients": product["ingredients"],
                "benefits": product["benefits"],
                "best_for": product["skin_type"],
                "concentration": product["concentration"],
                "value_rating": "Premium",
                "pros": ["Gentle formula", "Suitable for all skin types", "Additional antioxidant Vitamin E"],
                "cons": ["Higher price point", "Lower active concentration"]
            }
    
    def _extract_price(self, price_str: str) -> int:
        """Extract numeric price from string"""
        try:
            return int(''.join(filter(str.isdigit, price_str)))
        except:
            return 0
    
    def _generate_recommendation(self, product_a: Dict, product_b: Dict, blocks: Dict[str, Any]) -> str:
        """Generate recommendation based on comparison"""
        price_a = self._extract_price(blocks.get("price", {}).get("display_price", "₹0"))
        price_b = self._extract_price(product_b["price"])
        
        if price_a < price_b:
            return f"For budget-conscious buyers looking for effective Vitamin C, {product_a['name']} offers better value."
        else:
            return f"For sensitive skin or those wanting Vitamin E benefits, {product_b['name']} might be preferable despite higher cost."