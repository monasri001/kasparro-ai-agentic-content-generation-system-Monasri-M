from typing import Dict, Any, List
from .base import ContentLogicBlock
from .benefits_block import BenefitsGeneratorBlock
from .usage_block import UsageExtractorBlock
from .ingredient_block import IngredientAnalyzerBlock
from .safety_block import SafetyWarningBlock
from .price_block import PriceFormatterBlock
from ..models.product import ProductData

class ContentBlockManager:
    """
    Manages all content logic blocks.
    Can apply multiple blocks to product data.
    """
    
    def __init__(self):
        self.blocks = self._register_blocks()

    # Add this method to ContentBlockManager class:
    def process(self, product):
        """Alias for apply_blocks for DAG compatibility"""
        return self.apply_blocks(product)
    
    def _register_blocks(self) -> Dict[str, ContentLogicBlock]:
        """Register all available blocks"""
        return {
            "benefits": BenefitsGeneratorBlock(),
            "usage": UsageExtractorBlock(),
            "ingredients": IngredientAnalyzerBlock(),
            "safety": SafetyWarningBlock(),
            "price": PriceFormatterBlock()
        }
    
    def apply_blocks(self, product: ProductData, block_names: List[str] = None) -> Dict[str, Any]:
        """
        Apply specified blocks to product data.
        If no blocks specified, apply all.
        """
        print("🔧 [ContentBlockManager] Applying logic blocks...")
        
        results = {}
        
        if block_names is None:
            block_names = list(self.blocks.keys())
        
        for block_name in block_names:
            if block_name in self.blocks:
                block = self.blocks[block_name]
                try:
                    results[block_name] = block.apply(product)
                    print(f"   ✅ Applied: {block.name}")
                except Exception as e:
                    print(f"   ❌ Failed: {block.name} - {e}")
                    results[block_name] = {"error": str(e)}
        
        print(f"✅ [ContentBlockManager] Applied {len(results)} blocks")
        return results
    
    def get_available_blocks(self) -> List[Dict[str, str]]:
        """List all available blocks"""
        return [
            {"name": block.name, "description": block.__doc__ or "No description"}
            for block in self.blocks.values()
        ]