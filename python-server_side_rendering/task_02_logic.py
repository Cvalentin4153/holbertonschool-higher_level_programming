#!/usr/bin/env python3
"""
Task 2: Flask application with dynamic content using Jinja templates.
"""

import json
from flask import Flask, render_template

app = Flask(__name__)

def load_items():
    """Load items from the JSON file."""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            return data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/items')
def items():
    """Render the items page with dynamic content."""
    items_list = load_items()
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 