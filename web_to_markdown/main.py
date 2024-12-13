import asyncio
import argparse
import logging
from scraper import WebScraper
from converter import MarkdownConverter

async def main():
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert web pages to markdown format')
    parser.add_argument('url', help='URL of the webpage to convert')
    parser.add_argument('--output', '-o', help='Output file path (optional)')
    args = parser.parse_args()

    try:
        # Initialize components
        scraper = WebScraper()
        converter = MarkdownConverter()

        # Scrape the webpage
        logger.info(f"Scraping content from {args.url}")
        content = scraper.scrape(args.url)

        # Convert to markdown
        logger.info("Converting content to markdown")
        markdown_content = await converter.convert_to_markdown(content)

        # Handle output
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            logger.info(f"Markdown content saved to {args.output}")
        else:
            print(markdown_content)

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())
