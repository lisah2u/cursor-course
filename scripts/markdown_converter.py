import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

# Initialize the OpenAI client
client = OpenAI()

# return markdown from url
def convert_to_markdown(url: str) -> str:
    return "Hello, world!"

if __name__ == "__main__":
    url = "https://www.google.com"  
    print(convert_to_markdown(url))