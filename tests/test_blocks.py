import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.parser_agent import ParserAgent
from src.logic_blocks.manager import ContentBlockManager

def test_content_blocks():
    print("🧪 Testing Content Logic Blocks...")
    
    # Parse product data first
    raw_data = {
        "Product Name": "GlowBoost Vitamin C Serum",
        "Concentration": "10% Vitamin C", 
        "Skin Type": "Oily, Combination",
        "Key Ingredients": "Vitamin C, Hyaluronic Acid",
        "Benefits": "Brightening, Fades dark spots",
        "How to Use": "Apply 2–3 drops in the morning before sunscreen",
        "Side Effects": "Mild tingling for sensitive skin",
        "Price": "₹699"
    }
    
    parser = ParserAgent()
    product = parser.process(raw_data)
    
    # Test block manager
    manager = ContentBlockManager()
    
    print("\n📋 Available blocks:")
    for block in manager.get_available_blocks():
        print(f"  • {block['name']}: {block['description'][:60]}...")
    
    # Apply all blocks
    print("\n🔧 Applying all blocks...")
    results = manager.apply_blocks(product)
    
    # Check results
    assert "benefits" in results
    assert "usage" in results
    assert "ingredients" in results
    assert "safety" in results
    assert "price" in results
    
    print("\n✅ Block results summary:")
    for block_name, result in results.items():
        print(f"  📦 {block_name}: {len(result)} fields generated")
    
    # Show sample output
    print("\n🎯 Sample output from Benefits block:")
    print(f"  Primary benefits: {results['benefits'].get('primary_benefits', [])}")
    
    print("\n🎯 Sample output from Price block:")
    print(f"  Price category: {results['price'].get('price_category', '')}")
    
    print("\n✅ All content blocks working correctly!")
    return True

if __name__ == "__main__":
    test_content_blocks()