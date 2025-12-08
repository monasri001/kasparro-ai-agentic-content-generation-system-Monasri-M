import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents.parser_agent import ParserAgent
from src.agents.question_generator_agent import QuestionGeneratorAgent
from src.agents.template_agents import FAQTemplateAgent, ProductTemplateAgent, ComparisonTemplateAgent
from src.logic_blocks.manager import ContentBlockManager
from src.orchestration.dag import DAGOrchestrator

def test_full_workflow():
    print("🧪 Testing Complete Workflow...")
    
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
    
    # Create all agents
    parser = ParserAgent()
    question_gen = QuestionGeneratorAgent()
    content_manager = ContentBlockManager()
    faq_agent = FAQTemplateAgent()
    product_agent = ProductTemplateAgent()
    comparison_agent = ComparisonTemplateAgent()
    
    # Build DAG
    orchestrator = DAGOrchestrator()
    
    orchestrator.add_node("parser", parser)
    orchestrator.add_node("question_generator", question_gen, ["parser"])
    orchestrator.add_node("content_blocks", content_manager, ["parser"])
    orchestrator.add_node("faq_template", faq_agent, ["question_generator", "content_blocks"])
    orchestrator.add_node("product_template", product_agent, ["content_blocks"])
    orchestrator.add_node("comparison_template", comparison_agent, ["content_blocks"])
    
    # Execute
    results = orchestrator.execute({"initial_data": raw_data})
    
    # Check results
    assert "faq" in results
    assert "product_page" in results
    assert "comparison_page" in results
    
    print(f"\n✅ Generated {len(results)-1} pages")
    print(f"✅ FAQ questions: {results['faq']['content']['total_questions']}")
    
    return True

if __name__ == "__main__":
    test_full_workflow()