import json
import os
import array
import httpx
from dotenv import load_dotenv
from openai import OpenAI
from apps.base.log import logger
from common.utils.gemini_utils import get_gemini_stream_generator, get_gemini_generator
from common.utils import load_yaml, load_json

load_dotenv()

provider = os.environ.get("AI_PROVIDER") or cfg.get("open_ai", {}).get("provider", "openai")

# Load application configuration
cfg = load_yaml("config/application.yaml")

pre_messages = load_json("config/pre_message.json")

# Timeout for API requests
timeout = os.environ.get("OPENAI_API_TIMEOUT") or cfg.get("open_ai").get("timeout")
# API_KEY
api_key = os.environ.get("OPENAI_API_KEY") or cfg.get("open_ai").get("api_key")
# System content
sys_content = os.environ.get("OPENAI_API_SYS_CONTENT") or cfg.get("open_ai").get("sys_content")
# Travel content
travel_content = os.environ.get("OPENAI_API_TRAVEL_CONTENT") or cfg.get("open_ai").get("travel_content")
# Model to use
model = os.environ.get("OPENAI_API_MODEL") or cfg.get("open_ai").get("model")
# Proxy
proxy = os.environ.get("OPENAI_API_PROXY") or cfg.get("open_ai").get("proxy") or None
# HTTP client with proxy if specified
http_client = httpx.Client(proxy=proxy) if proxy else httpx.Client()

client = OpenAI(
    timeout=timeout,
    api_key=api_key,
    http_client=http_client,
)

async def get_openai_stream_generator(request_messages: array):
    if provider == "gemini":
        async for chunk in get_gemini_stream_generator(request_messages):
            yield chunk
        return
    message_list = []
    message_list.extend(pre_messages)
    message_list.extend(request_messages)

    # Lọc các tin nhắn hợp lệ
    new_message_list = [item for item in message_list if
                       item.get('role') == 'user' or item.get('role') == 'system' or item.get('role') == 'assistant']

    try:
        # Sử dụng định dạng mới cho input
        content = ""
        for msg in new_message_list:
            if msg.get('role') == 'user':
                content = msg.get('content')

        # Tìm tin nhắn system
        system_content = ""
        for msg in new_message_list:
            if msg.get('role') == 'system':
                system_content = msg.get('content')
                break
        
        stream = client.responses.create(
            model=model or "gpt-3.5-turbo",
            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": system_content
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": content
                        }
                    ]
                }
            ],
            text={
                "format": {
                    "type": "text"
                }
            },
            temperature=0.7,
            max_output_tokens=2048,
            stream=True
        )

        for event in stream:
            if hasattr(event, 'choices') and len(event.choices) > 0:
                delta = event.choices[0].delta
                if hasattr(delta, 'content') and delta.content:
                    answer = delta.content
                    yield json.dumps({'message': '', 'code': 0, 'data': answer}, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error in OpenAI API call: {str(e)}")
        yield json.dumps({'message': f'Error: {str(e)}', 'code': 500, 'data': ''}, ensure_ascii=False)

async def get_openai_generator(request_messages: array):
    if provider == "gemini":
        return await get_gemini_generator(request_messages)
    message_list = []
    message_list.extend(pre_messages)
    message_list.extend(request_messages)

    # Lọc các tin nhắn hợp lệ
    new_message_list = [item for item in message_list if
                        item.get('role') == 'user' or item.get('role') == 'system' or item.get('role') == 'assistant']

    try:
        # Sử dụng định dạng mới cho input
        content = ""
        for msg in new_message_list:
            if msg.get('role') == 'user':
                content = msg.get('content')

        # Tìm tin nhắn system
        system_content = ""
        for msg in new_message_list:
            if msg.get('role') == 'system':
                system_content = msg.get('content')
                break
        
        response = client.responses.create(
            model=model or "gpt-3.5-turbo",
            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": system_content
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": content
                        }
                    ]
                }
            ],
            text={
                "format": {
                    "type": "text"
                }
            },
            temperature=0.7,
            max_output_tokens=2048
        )
        
        result = ""
        if hasattr(response, 'outputs') and len(response.outputs) > 0:
            result = response.outputs[0].text
            
        logger.info(result)
        return result
    except Exception as e:
        logger.error(f"Error in OpenAI API call: {str(e)}")
        return f"Error: {str(e)}"

async def get_pre_messages():
    return pre_messages