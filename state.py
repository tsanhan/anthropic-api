
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5-20251001"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)
    
def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, max_tokens, system_prompt=None):
    # Make a request
    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages
    }
    if system_prompt:
        params["system"] = system_prompt    
    
    response = client.messages.create(**params)
    return response.content[0].text
