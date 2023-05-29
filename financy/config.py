import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    fields = ['openai_api_key', 'azure_form_key', 'azure_form_endpoint']

    def __init__(self):
        for field in self.fields:
            env_value = os.getenv(field.upper())
            if env_value is None:
                raise ValueError(f'{field} environment variable is not set')
            
            setattr(self, field, env_value)