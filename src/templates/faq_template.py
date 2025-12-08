from typing import Dict, Any
from datetime import datetime
from .base import Template

class FAQTemplate(Template):
    """Template for FAQ page with categorized questions"""
    
    @property
    def name(self):
        return "faq"
    
    @property
    def description(self):
        return "Frequently Asked Questions page with categorized Q&A"
    
    def render(self, data: Dict[str, Any]) -> Dict[str, Any]:
        print(f"🔧 [{self.name.upper()} Template] Rendering FAQ page...")
        
        # Validate required data
        required = ["product_info", "questions", "content_blocks"]
        if not self.validate_data(data, required):
            return {"error": "Missing required data for FAQ template"}
        
        product = data["product_info"]
        questions = data["questions"]
        blocks = data["content_blocks"]
        
        # Group questions by category
        categories = {}
        for q in questions:
            category = q["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append({
                "id": q["id"],
                "question": q["question"],
                "answer": self._generate_answer(q, blocks)
            })
        
        # Build FAQ page structure
        faq_page = {
            "title": f"FAQ - {product['name']}",
            "product": {
                "name": product["name"],
                "price": product["price"],
                "category": "Skincare Serum"
            },
            "summary": f"Common questions about {product['name']}, a {product.get('concentration', '')} serum.",
            "categories": [
                {
                    "name": category,
                    "count": len(questions),
                    "questions": questions_list
                }
                for category, questions_list in categories.items()
            ],
            "total_questions": len(questions),
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }
        
        print(f"✅ [{self.name.upper()} Template] Generated FAQ with {len(questions)} questions")
        return self.add_metadata(faq_page)
    
    def _generate_answer(self, question: Dict, blocks: Dict[str, Any]) -> str:
        """Generate answer based on question category and content blocks"""
        category = question["category"]
        
        if category == "Informational":
            return f"{question['question'].replace('What is', 'This is')}. " \
                   f"It contains {blocks.get('ingredients', {}).get('total_actives', 0)} active ingredients."
        
        elif category == "Safety":
            safety = blocks.get("safety", {})
            return f"{safety.get('side_effects', 'Generally safe for most skin types.')} " \
                   f"Recommendations: {', '.join(safety.get('recommendations', []))}"
        
        elif category == "Usage":
            usage = blocks.get("usage", {})
            return f"{usage.get('main_instruction', '')}. " \
                   f"Best used: {usage.get('best_time', 'Daily')}. " \
                   f"Key tip: {usage.get('key_tip', '')}"
        
        elif category == "Purchase":
            price = blocks.get("price", {})
            return f"Price: {price.get('display_price', '')}. " \
                   f"Category: {price.get('price_category', '')}. " \
                   f"Value: {price.get('value_rating', '')}"
        
        elif category == "Comparison":
            return f"This product offers unique benefits including " \
                   f"{', '.join(blocks.get('benefits', {}).get('primary_benefits', ['multiple benefits']))}. " \
                   f"Compare with similar products for your specific needs."
        
        return "Information available from product specifications."