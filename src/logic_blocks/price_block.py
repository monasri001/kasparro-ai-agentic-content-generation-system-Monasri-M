from typing import Dict, Any
from .base import ContentLogicBlock
from ..models.product import ProductData

class PriceFormatterBlock(ContentLogicBlock):
    """
    Formats price information and value analysis.
    """
    
    @property
    def name(self):
        return "format-price-block"
    
    def apply(self, product: ProductData) -> Dict[str, Any]:
        price_text = product.price
        
        # Extract numeric value
        price_value = 0
        for char in price_text:
            if char.isdigit():
                price_value = price_value * 10 + int(char)
        
        # Determine price category
        if price_value < 500:
            price_category = "Budget"
            value_rating = "Good value"
        elif price_value < 1000:
            price_category = "Mid-range"
            value_rating = "Premium quality"
        else:
            price_category = "Luxury"
            value_rating = "High-end"
        
        return {
            "display_price": price_text,
            "numeric_value": price_value,
            "currency": "INR",
            "price_category": price_category,
            "value_rating": value_rating,
            "price_per_ml": f"₹{price_value / 30:.2f}/ml (estimated)",
            "comparison_note": "Competitively priced for a Vitamin C serum"
        }