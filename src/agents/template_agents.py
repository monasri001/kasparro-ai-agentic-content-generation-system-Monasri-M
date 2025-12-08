from src.templates.manager import TemplateManager

class FAQTemplateAgent:
    def __init__(self):
        self.agent_name = "FAQTemplateAgent"
    
    def process(self, data):
        manager = TemplateManager()
        return manager.render_template("faq", data)

class ProductTemplateAgent:
    def __init__(self):
        self.agent_name = "ProductTemplateAgent"
    
    def process(self, data):
        manager = TemplateManager()
        return manager.render_template("product_page", data)

class ComparisonTemplateAgent:
    def __init__(self):
        self.agent_name = "ComparisonTemplateAgent"
    
    def process(self, data):
        manager = TemplateManager()
        return manager.render_template("comparison_page", data)