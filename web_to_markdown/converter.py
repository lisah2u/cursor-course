import os
from typing import Optional
from openai import AsyncOpenAI
from dotenv import load_dotenv
import logging

class MarkdownConverter:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        
        self.client = AsyncOpenAI(api_key=api_key)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    async def convert_to_markdown(self, content: str, max_length: Optional[int] = 4000) -> str:
        """
        Convert text content to markdown format using OpenAI's GPT model.
        
        Args:
            content (str): The text content to convert
            max_length (int, optional): Maximum chunk size for processing
            
        Returns:
            str: The markdown formatted text
        """
        try:
            # Split content into chunks if it exceeds max_length
            chunks = [content[i:i + max_length] for i in range(0, len(content), max_length)]
            markdown_chunks = []

            for chunk in chunks:
                response = await self.client.chat.completions.create(
                    model="gpt-4o-mini",  # You can adjust the model as needed
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that converts text content into well-formatted markdown. Maintain the original structure and meaning while improving readability."},
                        {"role": "user", "content": f"Convert this text to markdown format:\n\n{chunk}"}
                    ],
                    temperature=0.3,
                    max_tokens=2000
                )
                
                markdown_chunks.append(response.choices[0].message.content)

            return '\n'.join(markdown_chunks)

        except Exception as e:
            self.logger.error(f"Error converting to markdown: {str(e)}")
            raise
