import json
from datetime import datetime
from typing import Any, Dict

class JSONOutputFormatter:
    """Utility for formatting and saving JSON outputs"""
    
    @staticmethod
    def save_json(data: Dict[str, Any], filepath: str, indent: int = 2):
        """
        Save data as formatted JSON file.
        
        Args:
            data: Dictionary to save
            filepath: Output file path
            indent: JSON indentation
        """
        # Ensure directory exists
        import os
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Convert datetime objects to strings
        def datetime_serializer(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Type {type(obj)} not serializable")
        
        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, default=datetime_serializer, ensure_ascii=False)
        
        print(f"💾 Saved JSON to: {filepath}")
    
    @staticmethod
    def validate_json(filepath: str) -> bool:
        """
        Validate JSON file is properly formatted.
        
        Args:
            filepath: Path to JSON file
            
        Returns:
            True if valid JSON
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                json.load(f)
            return True
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON in {filepath}: {e}")
            return False
    
    @staticmethod
    def add_metadata(data: Dict[str, Any], page_type: str) -> Dict[str, Any]:
        """
        Add standard metadata to output.
        
        Args:
            data: Content data
            page_type: Type of page (faq, product_page, etc.)
            
        Returns:
            Data with metadata added
        """
        return {
            "system": "Kasparro Agentic Content Generation",
            "page_type": page_type,
            "generated_at": datetime.now().isoformat(),
            "version": "1.0",
            "content": data
        }