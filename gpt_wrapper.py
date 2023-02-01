import os
import openai

def send_completion_request(prompt, model_choice="text-davinci-003",
                            model_temperature=0.7, max_tokens=250):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    response = openai.Completion.create(
        model=model_choice,
        prompt=prompt,
        temperature=model_temperature,
        max_tokens=max_tokens
    )
    return response['choices'][0]['text']

