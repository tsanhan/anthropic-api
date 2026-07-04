import os
from anthropic import Anthropic
from dotenv import load_dotenv



class AnthropicClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in .env file")
        self.client = Anthropic(api_key=api_key )
    
    def get_client(self):
        return self.client
