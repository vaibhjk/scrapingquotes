from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    # URL of the static website
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrape quotes and authors
    quotes_data = []
    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        quotes_data.append({"text": text, "author": author})

    # HTML Template
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        
    </head>
    <body>
        <h1>Scraped Quotes</h1>
        <ul>
            {% for item in quotes_data %}
                <li>
                    <strong>"{{ item.text }}"</strong> - {{ item.author }}
                </li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    return render_template_string(html_template, quotes_data=quotes_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
