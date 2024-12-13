# Web to Markdown Converter

A Python tool that scrapes web pages and converts their content to well-formatted markdown using OpenAI's GPT model.

## Features

- Web scraping with proper user agent handling
- Content cleaning and preprocessing
- Markdown conversion using OpenAI's GPT model
- Support for large content through chunking
- Command-line interface
- Configurable output (file or stdout)

## Installation

1. Clone the repository
2. Create the conda environment:
```bash
conda env create -f environment.yml
```
3. Activate the environment:
```bash
conda activate web_to_markdown
```
4. Copy `.env.example` to `.env` and add your OpenAI API key:
```bash
cp .env.example .env
# Edit .env and add your API key
```

## Usage

Basic usage:
```bash
python main.py https://example.com
```

Save output to file:
```bash
python main.py https://example.com -o output.md
```

## Project Structure

- `main.py`: Entry point and command-line interface
- `scraper.py`: Web scraping functionality
- `converter.py`: Markdown conversion using OpenAI's GPT
- `environment.yml`: Conda environment configuration
- `.env`: Configuration for API keys (not included in repo)

## Requirements

- Python 3.10+
- OpenAI API key
- Dependencies listed in `environment.yml`

## Error Handling

The tool includes comprehensive error handling and logging for:
- Web scraping issues
- API failures
- File operations
- Invalid URLs

## License

MIT
