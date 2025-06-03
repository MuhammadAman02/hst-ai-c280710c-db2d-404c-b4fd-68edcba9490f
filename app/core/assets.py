"""Professional visual asset management system for the Hello World landing page"""
import requests
from typing import List, Dict, Optional
import random
import sys
import codecs

# Force UTF-8 encoding for reliability
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

class ProfessionalAssetManager:
    """Manages professional visual assets for applications"""
    
    IMAGE_CATEGORIES = {
        "portfolio": ["technology", "workspace", "coding", "professional", "innovation"],
        "dashboard": ["analytics", "charts", "business", "data", "insights"],
        "ecommerce": ["products", "shopping", "retail", "commerce", "marketplace"],
        "saas": ["cloud", "software", "business", "enterprise", "productivity"],
        "finance": ["finance", "banking", "investment", "money", "economics"],
        "healthcare": ["health", "medical", "wellness", "care", "science"],
        "education": ["education", "learning", "school", "knowledge", "training"]
    }
    
    @staticmethod
    def get_project_images(project_type: str, count: int = 6) -> List[str]:
        """Fetch contextually relevant professional images"""
        categories = ProfessionalAssetManager.IMAGE_CATEGORIES.get(
            project_type.lower(), ["business", "technology"]
        )
        
        images = []
        for i in range(count):
            category = categories[i % len(categories)]
            # Generate unique URLs to avoid caching issues
            seed = random.randint(1000, 9999)
            img_url = f"https://source.unsplash.com/800x600/?{category}&sig={seed}"
            images.append(img_url)
        
        if not images:
            # Fallback to a generic, high-quality placeholder if Unsplash fails
            images = [f"https://picsum.photos/800/600?random={i}" for i in range(1, count+1)]
        
        return images
    
    @staticmethod
    def get_hero_image(project_type: str) -> str:
        """Get high-quality hero image for main sections"""
        categories = ProfessionalAssetManager.IMAGE_CATEGORIES.get(
            project_type.lower(), ["business"]
        )
        primary_category = categories[0]
        seed = random.randint(10000, 99999)
        return f"https://source.unsplash.com/1200x600/?{primary_category}&sig={seed}"

    @staticmethod
    def get_placeholder_svg(width: int, height: int, text: str = "Placeholder") -> str:
        """Generates a simple SVG placeholder."""
        return f"""<svg width='{width}' height='{height}' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width} {height}'>\n  <rect fill='#cccccc' width='{width}' height='{height}'/>\n  <text x='50%' y='50%' dominant-baseline='middle' text-anchor='middle' font-family='sans-serif' font-size='24' fill='#333333'>{text}</text>\n</svg>"""