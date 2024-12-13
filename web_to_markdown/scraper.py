import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional
import logging

class WebScraper:
    def __init__(self, headers: Optional[Dict] = None):
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def scrape(self, url: str) -> str:
        """
        Scrape content from a given URL.
        
        Args:
            url (str): The URL to scrape
            
        Returns:
            str: The extracted text content
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Extract text and clean it
            text = soup.get_text(separator='\n', strip=True)
            
            # Remove empty lines and excessive whitespace
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            cleaned_text = '\n'.join(lines)
            
            return cleaned_text
            
        except requests.RequestException as e:
            self.logger.error(f"Error scraping {url}: {str(e)}")
            raise
