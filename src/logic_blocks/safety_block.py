from typing import Dict, Any
from .base import ContentLogicBlock
from ..models.product import ProductData

class SafetyWarningBlock(ContentLogicBlock):
    """
    Formats safety information and warnings.
    """
    
    @property
    def name(self):
        return "safety-warning-block"
    
    def apply(self, product: ProductData) -> Dict[str, Any]:
        side_effects = product.side_effects
        skin_types = product.skin_type
        
        warnings = []
        recommendations = []
        
        if "tingling" in side_effects.lower():
            warnings.append("Mild tingling may occur initially")
            recommendations.append("Start with patch test")
        
        if "sensitive" in side_effects.lower():
            warnings.append("Extra caution for sensitive skin")
            recommendations.append("Use every other day at first")
        
        # Add based on skin type
        if "Oily" in skin_types:
            recommendations.append("Suitable for oily skin - non-comedogenic")
        
        if "Combination" in skin_types:
            recommendations.append("Balances both oily and dry areas")
        
        return {
            "side_effects": side_effects,
            "warnings": warnings,
            "recommendations": recommendations,
            "patch_test": True,
            "discontinue_if": "Severe irritation occurs",
            "consult_doctor": "If you have very sensitive skin or conditions"
        }