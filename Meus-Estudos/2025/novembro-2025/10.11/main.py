from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

while True:
    a = input("\033[32mUser: \033[0m")
    response = client.responses.create(
    model="gpt-5-nano",
    input= a,
    store=True,
    )
    if a in ['break', 'quit', 'stop', 'bye']:
        break

    print(f'\033[36m{response.output_text}\033[0m')
