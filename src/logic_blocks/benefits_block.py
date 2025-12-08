from typing import Dict, Any
from .base import ContentLogicBlock
from ..models.product import ProductData

class BenefitsGeneratorBlock(ContentLogicBlock):
    """
    Transforms benefits data into marketing copy.
    Example: "Brightening" → "Enhances skin radiance and glow"
    """
    
    @property
    def name(self):
        return "generate-benefits-block"
    
    def apply(self, product: ProductData) -> Dict[str, Any]:
        enhanced_benefits = []
        
        for benefit in product.benefits:
            if benefit == "Brightening":
                enhanced_benefits.append("Enhances skin radiance and glow")
                enhanced_benefits.append("Reduces dullness for luminous skin")
            elif benefit == "Fades dark spots":
                enhanced_benefits.append("Reduces appearance of hyperpigmentation")
                enhanced_benefits.append("Helps fade dark spots over time")
            else:
                enhanced_benefits.append(benefit)
        
        return {
            "primary_benefits": enhanced_benefits[:2],
            "secondary_benefits": enhanced_benefits[2:],
            "total_benefits": len(enhanced_benefits),
            "key_benefit": enhanced_benefits[0] if enhanced_benefits else ""
        }