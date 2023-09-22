import openai
import os

# Enter your API here
API_KEY = os.getenv("OPENAI_API")


class ChatBot:
    def __init__(self):
        openai.api_key = API_KEY

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


