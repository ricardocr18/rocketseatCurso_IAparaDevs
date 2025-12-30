"""
Gerador de imagens usando DALL-E 3.
"""

import os
import requests
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
output_dir = Path("outputs/thumbnails/images")
output_dir.mkdir(parents=True, exist_ok=True)


def generate_image(prompt: str) -> dict:
    """
    Gera uma thumbnail usando DALL-E 3.
    
    Args:
        prompt: Descrição da imagem
    
    Returns:
        Dict com url e local_path
    """
    try:
        enhanced_prompt = f"""Professional YouTube gaming thumbnail, 16:9 aspect ratio, 
        {prompt}, high contrast, bold text, vibrant colors, eye-catching, clickable"""
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=enhanced_prompt,
            size="1792x1024",
            quality="hd",
            style="vivid",
            n=1
        )
        
        image_url = response.data[0].url
        
        # Salvar localmente
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"thumbnail_{timestamp}.png"
        filepath = output_dir / filename
        
        img_response = requests.get(image_url, timeout=30)
        img_response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            f.write(img_response.content)
        
        print(f"✅ Thumbnail salva: {filepath}")
        
        return {
            'url': image_url,
            'local_path': str(filepath),
            'prompt': prompt
        }
    
    except Exception as e:
        print(f"⚠️ Erro ao gerar imagem: {e}")
        return {
            'url': None,
            'local_path': None,
            'error': str(e)
        }


class ImageGeneratorTool:
    """Wrapper para geração de imagens"""
    def __init__(self):
        pass
    
    def generate(self, prompt: str) -> dict:
        return generate_image(prompt)