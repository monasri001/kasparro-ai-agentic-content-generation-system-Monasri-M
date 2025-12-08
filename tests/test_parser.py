import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.parser_agent import ParserAgent

def test_parser_agent():
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
    
    assert product.name == "GlowBoost Vitamin C Serum"
    assert product.concentration == "10% Vitamin C"
    assert product.skin_type == ["Oily", "Combination"]
    assert product.key_ingredients == ["Vitamin C", "Hyaluronic Acid"]
    assert product.benefits == ["Brightening", "Fades dark spots"]
    assert "699" in product.price
    
    print("✅ ParserAgent test passed!")
    
if __name__ == "__main__":
    test_parser_agent()