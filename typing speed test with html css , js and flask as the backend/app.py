from flask import Flask, render_template, make_response
import random

app = Flask(__name__)

# Sample text for typing test
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "Practice makes perfect.",
    "Life is what happens while you're busy making other plans."
]

@app.route('/')
def index():
    # Create response object
    response = make_response(render_template('index.html', text=random.choice(sample_texts)))
    
    # Set headers to prevent caching
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
