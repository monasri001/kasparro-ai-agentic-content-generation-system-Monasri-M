from typing import List
from ..models.product import ProductData, FAQItem

class QuestionGeneratorAgent:
    def __init__(self):
        self.agent_name = "QuestionGeneratorAgent"
        self.description = "Generates user questions from product data"
        
        self.question_templates = {
            "Informational": [
                "What is {name}?",
                "What are the main ingredients in {name}?",
                "What is the concentration of active ingredients in {name}?",
                "Who should use {name}?",
                "What skin types is {name} suitable for?"
            ],
            "Safety": [
                "Are there any side effects of using {name}?",
                "Is {name} safe for sensitive skin?",
                "Can {name} cause irritation?",
                "What precautions should I take with {name}?",
                "Has {name} been tested for safety?"
            ],
            "Usage": [
                "How do I use {name}?",
                "When should I apply {name}?",
                "How much {name} should I use per application?",
                "Can I use {name} with other skincare products?",
                "How often should I use {name}?"
            ],
            "Purchase": [
                "How much does {name} cost?",
                "Where can I buy {name}?",
                "Is {name} worth the price?",
                "Does {name} offer good value for money?",
                "Are there any discounts available for {name}?"
            ],
            "Comparison": [
                "How does {name} compare to other vitamin C serums?",
                "What makes {name} different from competitors?",
                "Is {name} better than other brightening serums?",
                "What are good alternatives to {name}?",
                "Why should I choose {name} over similar products?"
            ]
        }
    
    def process(self, product: ProductData) -> List[FAQItem]:
        print(f"🔧 [{self.agent_name}] Generating questions...")
        
        questions = []
        question_id = 1
        
        for category, templates in self.question_templates.items():
            for template in templates[:3]:
                formatted_question = template.format(
                    name=product.name,
                    concentration=product.concentration,
                    skin_types=", ".join(product.skin_type)
                )
                
                source_fields = self._get_source_fields(category, product)
                
                faq_item = FAQItem(
                    id=question_id,
                    category=category,
                    question=formatted_question,
                    answer="",
                    source_data=source_fields
                )
                
                questions.append(faq_item)
                question_id += 1
        
        print(f"✅ [{self.agent_name}] Generated {len(questions)} questions")
        return questions
    
    def _get_source_fields(self, category: str, product: ProductData) -> List[str]:
        field_mapping = {
            "Informational": ["name", "concentration", "key_ingredients", "skin_type"],
            "Safety": ["side_effects", "skin_type"],
            "Usage": ["how_to_use"],
            "Purchase": ["price"],
            "Comparison": ["name", "benefits", "price", "key_ingredients"]
        }
        return field_mapping.get(category, [])
    
    def get_status(self) -> dict:
        return {
            "agent": self.agent_name,
            "status": "ready",
            "description": self.description,
            "categories": list(self.question_templates.keys())
        }