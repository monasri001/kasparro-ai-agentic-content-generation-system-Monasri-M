import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.parser_agent import ParserAgent
from src.agents.question_generator_agent import QuestionGeneratorAgent

def test_question_generator():
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
    
    question_gen = QuestionGeneratorAgent()
    questions = question_gen.process(product)
    
    assert len(questions) == 15
    assert all(q.category for q in questions)
    
    categories = set(q.category for q in questions)
    assert len(categories) == 5
    
    print(f"✅ Generated {len(questions)} questions")
    print(f"✅ Categories: {categories}")
    
    print("\n📋 Sample Questions:")
    for i, q in enumerate(questions[:3], 1):
        print(f"  {i}. [{q.category}] {q.question}")
    
    return True

if __name__ == "__main__":
    test_question_generator()