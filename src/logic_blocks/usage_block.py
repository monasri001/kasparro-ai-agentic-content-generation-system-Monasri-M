from typing import Dict, Any
from .base import ContentLogicBlock
from ..models.product import ProductData

class UsageExtractorBlock(ContentLogicBlock):
    """
    Formats usage instructions into structured steps.
    """
    
    @property
    def name(self):
        return "extract-usage-block"
    
    def apply(self, product: ProductData) -> Dict[str, Any]:
        usage_text = product.how_to_use
        
        # Extract steps from usage text
        steps = []
        if "drops" in usage_text.lower():
            steps.append("Take 2-3 drops of serum")
        
        if "morning" in usage_text.lower():
            steps.append("Use in the morning routine")
        
        if "sunscreen" in usage_text.lower():
            steps.append("Apply before sunscreen for protection")
        
        # Add default steps if none found
        if not steps:
            steps = ["Apply to clean face", "Use daily for best results"]
        
        return {
            "main_instruction": usage_text,
            "steps": steps,
            "frequency": "Daily",
            "best_time": "Morning",
            "key_tip": "Apply to damp skin for better absorption"
        }