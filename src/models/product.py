from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class ProductData(BaseModel):
    name: str = Field(..., description="Product name")
    concentration: str = Field(..., description="Concentration percentage")
    skin_type: List[str] = Field(..., description="List of suitable skin types")
    key_ingredients: List[str] = Field(..., description="List of main ingredients")
    benefits: List[str] = Field(..., description="List of benefits")
    how_to_use: str = Field(..., description="Usage instructions")
    side_effects: str = Field(..., description="Potential side effects")
    price: str = Field(..., description="Price with currency")
    
    timestamp: datetime = Field(default_factory=datetime.now)
    
    class Config:
        frozen = True

class FAQItem(BaseModel):
    id: int
    category: str
    question: str
    answer: str
    source_data: List[str]
    
class ProductPage(BaseModel):
    title: str
    description: str
    specifications: dict
    benefits: List[str]
    usage: str
    safety_info: str
    price: str
    
class ComparisonProduct(BaseModel):
    name: str
    ingredients: List[str]
    benefits: List[str]
    price: str
    key_feature: str