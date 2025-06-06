import json
import os
import array
import google.generativeai as genai
from dotenv import load_dotenv
from apps.base.log import logger
from common.utils import load_yaml, load_json

load_dotenv()

# Load application configuration
cfg = load_yaml("config/application.yaml")
pre_messages = load_json("config/pre_message.json")

# Gemini configuration
gemini_api_key = os.environ.get("GEMINI_API_KEY") or cfg.get("open_ai", {}).get("api_key")
gemini_model = os.environ.get("GEMINI_MODEL") or cfg.get("open_ai", {}).get("model", "gemini-2.0-flash")

# Configure Gemini
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)

async def get_openai_stream_generator(request_messages: array):
    """Gemini streaming response"""
    try:
        if not gemini_api_key:
            yield f"data: {json.dumps({'message': 'Gemini API key not configured', 'code': 500, 'data': ''}, ensure_ascii=False)}\n\n"
            return

        # Tạo combined prompt từ messages
        system_content = ""
        user_content = ""
        
        # Lấy system message từ pre_messages
        for msg in pre_messages:
            if msg.get('role') == 'system':
                system_content = msg.get('content', '')
                break
        
        # Lấy user message cuối cùng
        for msg in reversed(request_messages):
            if msg.get('role') == 'user':
                user_content = msg.get('content', '')
                break
        
        combined_prompt = f"{system_content}\n\n{user_content}"
        
        model = genai.GenerativeModel(gemini_model)
        response = model.generate_content(
            combined_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=2048,
            ),
            stream=True
        )
        print(response)
        for chunk in response:
            if chunk.text:
                data = json.dumps({'message': '', 'code': 0, 'data': chunk.text}, ensure_ascii=False)
                yield f"data: {data}\n\n"
                
    except Exception as e:
        logger.error(f"Error in Gemini API call: {str(e)}")
        error_data = json.dumps({'message': f'Gemini Error: {str(e)}', 'code': 500, 'data': ''}, ensure_ascii=False)
        yield f"data: {error_data}\n\n"

async def get_openai_generator(request_messages: array):
    """Gemini non-streaming response"""
    try:
        if not gemini_api_key:
            return "Gemini API key not configured"

        # Tạo combined prompt từ messages
        system_content = ""
        user_content = ""
        
        # Lấy system message từ pre_messages
        for msg in pre_messages:
            if msg.get('role') == 'system':
                system_content = msg.get('content', '')
                break
        
        # Lấy user message cuối cùng
        for msg in reversed(request_messages):
            if msg.get('role') == 'user':
                user_content = msg.get('content', '')
                break
        
        combined_prompt = f"{system_content}\n\n{user_content}"
        
        model = genai.GenerativeModel(gemini_model)
        response = model.generate_content(
            combined_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=8192,
            )
        )
        
        return response.text
        
    except Exception as e:
        logger.error(f"Error in Gemini API call: {str(e)}")
        return f"Gemini Error: {str(e)}"

async def get_pre_messages():
    return pre_messages