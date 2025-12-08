from typing import Dict, Any
from .faq_template import FAQTemplate
from .product_template import ProductPageTemplate
from .comparison_template import ComparisonTemplate

class TemplateManager:
    """
    Manages all templates and renders pages.
    """
    
    def __init__(self):
        self.templates = self._register_templates()
    
    def process(self, data):
        """
        Process method for DAG compatibility.
        Automatically detects which template to render based on available data.
        """
        # Check what data we have to determine which template to render
        if "questions" in data and "content_blocks" in data:
            # FAQ template
            return self.render_template("faq", data)
        elif "product_info" in data and "content_blocks" in data:
            # Product page template
            if "questions" not in data:
                return self.render_template("product_page", data)
            else:
                # Could be either, default to product page
                return self.render_template("product_page", data)
        elif "product_a" in data:
            # Comparison template
            return self.render_template("comparison_page", data)
        else:
            # Default: render all
            return self.render_all_templates(data)

    def _register_templates(self) -> Dict[str, Any]:
        """Register all available templates"""
        return {
            "faq": FAQTemplate(),
            "product_page": ProductPageTemplate(),
            "comparison_page": ComparisonTemplate()
        }
    
    def render_template(self, template_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Render a template with provided data.
        
        Args:
            template_name: Name of template to render
            data: Dictionary containing all required data
            
        Returns:
            Rendered content as dictionary
        """
        if template_name not in self.templates:
            print(f"❌ Template '{template_name}' not found")
            return {"error": f"Template '{template_name}' not found"}
        
        template = self.templates[template_name]
        
        try:
            # Different print based on which template
            if template_name == "faq_template":
                print("🎨 Rendering FAQ template...")
            elif template_name == "product_template":
                print("🎨 Rendering Product Page template...")
            elif template_name == "comparison_template":
                print("🎨 Rendering Comparison template...")
            else:
                print(f"🎨 Rendering {template.name} template...")
            
            result = template.render(data)
            return result
        except Exception as e:
            print(f"❌ Failed to render {template.name}: {e}")
            return {"error": str(e)}
    
    def render_all_templates(self, data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """
        Render all templates with the same data.
        
        Args:
            data: Dictionary containing data for all templates
            
        Returns:
            Dictionary with template_name: rendered_content
        """
        print("🎨 Rendering all templates...")
        results = {}
        
        for template_name, template in self.templates.items():
            print(f"  Processing {template_name}...")
            result = template.render(data)
            results[template_name] = result
        
        print(f"✅ Rendered {len(results)} templates")
        return results
    
    def get_template_info(self) -> Dict[str, Any]:
        """Get information about all available templates"""
        return {
            template_name: {
                "name": template.name,
                "description": template.description,
                "required_fields": self._get_required_fields(template_name)
            }
            for template_name, template in self.templates.items()
        }
    
    def _get_required_fields(self, template_name: str) -> list:
        """Get required fields for a template"""
        field_map = {
            "faq": ["product_info", "questions", "content_blocks"],
            "product_page": ["product_info", "content_blocks"],
            "comparison_page": ["product_a", "content_blocks"]
        }
        return field_map.get(template_name, [])