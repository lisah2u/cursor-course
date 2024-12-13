import os
from flask import Flask, render_template, request, send_file, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import asyncio
from scraper import WebScraper
from converter import MarkdownConverter
import tempfile
from asgiref.sync import async_to_sync

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

class URLForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Convert to Markdown')

async def process_url(url: str) -> str:
    # Initialize components
    scraper = WebScraper()
    converter = MarkdownConverter()

    # Scrape the webpage
    content = scraper.scrape(url)

    # Convert to markdown
    markdown_content = await converter.convert_to_markdown(content)
    return markdown_content

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        try:
            # Process the URL and get markdown content
            markdown_content = async_to_sync(process_url)(form.url.data)

            # Create a temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
                temp_file.write(markdown_content)
                temp_path = temp_file.name

            # Send the file to the user
            return send_file(
                temp_path,
                as_attachment=True,
                download_name='converted.md',
                mimetype='text/markdown'
            )

        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            return render_template('index.html', form=form)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
