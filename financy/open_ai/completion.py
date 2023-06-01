import openai
from financy.config import Config

def completion(prompt: str):
    c = Config()
    openai.api_key = c.openai_api_key

    data = openai.Model.list()["data"]
    model_id = None
    for model in data:
        if "FiNancy" in model["id"]:
            model_id = model["id"]
            break

    response = openai.Completion.create(model=model_id, prompt=prompt, max_tokens=1)
    print(response)

    return response.choices[0].text