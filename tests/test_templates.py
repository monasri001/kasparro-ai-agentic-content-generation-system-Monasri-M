import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.parser_agent import ParserAgent
from src.agents.question_generator_agent import QuestionGeneratorAgent
from src.logic_blocks.manager import ContentBlockManager
from src.templates.manager import TemplateManager

def test_template_engine():
    print("🧪 Testing Template Engine...")
    
    # 1. Parse product data
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
    
    # 2. Generate questions
    question_gen = QuestionGeneratorAgent()
    questions = question_gen.process(product)
    
    # 3. Apply content blocks
    block_manager = ContentBlockManager()
    content_blocks = block_manager.apply_blocks(product)
    
    # 4. Prepare data for templates
    template_data = {
        "product_info": {
            "name": product.name,
            "concentration": product.concentration,
            "skin_type": product.skin_type,
            "price": product.price
        },
        "questions": [q.model_dump() for q in questions],
        "content_blocks": content_blocks,
        "product_a": {
            "name": product.name,
            "concentration": product.concentration,
            "skin_type": product.skin_type,
            "price": product.price
        }
    }
    
    # 5. Test Template Manager
    template_manager = TemplateManager()
    
    print("\n📋 Available templates:")
    for name, info in template_manager.get_template_info().items():
        print(f"  • {name}: {info['description']}")
        print(f"    Required: {info['required_fields']}")
    
    # 6. Test individual templates
    print("\n🔧 Testing FAQ Template...")
    faq_result = template_manager.render_template("faq", template_data)
    assert "content" in faq_result
    assert faq_result["page_type"] == "faq"
    print(f"   ✅ FAQ has {faq_result['content'].get('total_questions', 0)} questions")
    
    print("\n🔧 Testing Product Page Template...")
    product_result = template_manager.render_template("product_page", template_data)
    assert "content" in product_result
    assert product_result["page_type"] == "product_page"
    print(f"   ✅ Product page generated with specifications")
    
    print("\n🔧 Testing Comparison Template...")
    comparison_result = template_manager.render_template("comparison_page", template_data)
    assert "content" in comparison_result
    assert comparison_result["page_type"] == "comparison_page"
    print(f"   ✅ Comparison with fictional product generated")
    
    # 7. Test rendering all templates at once
    print("\n🎨 Rendering all templates at once...")
    all_results = template_manager.render_all_templates(template_data)
    
    assert len(all_results) == 3
    assert "faq" in all_results
    assert "product_page" in all_results
    assert "comparison_page" in all_results
    
    print(f"\n✅ All templates rendered successfully!")
    print(f"   Generated: {', '.join(all_results.keys())}")
    
    # Show sample output structure
    print("\n📄 Sample FAQ structure:")
    faq_content = all_results["faq"]["content"]
    print(f"   Title: {faq_content.get('title', '')}")
    print(f"   Categories: {len(faq_content.get('categories', []))}")
    
    return all_results

if __name__ == "__main__":
    results = test_template_engine()
    
    # Save sample output to file
    import json
    with open("output/sample_faq.json", "w", encoding="utf-8") as f:
        json.dump(results["faq"], f, indent=2, ensure_ascii=False)
    print("\n💾 Sample FAQ saved to output/sample_faq.json")