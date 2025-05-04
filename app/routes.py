from flask import render_template, request
from app import app
from app.ai import analyze_sentiment

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
    return render_template('index.html', sentiment=sentiment)
