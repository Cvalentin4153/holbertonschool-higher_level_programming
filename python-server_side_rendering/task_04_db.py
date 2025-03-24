#!/usr/bin/env python3
"""
Task 4: Flask application with JSON, CSV, and SQLite database support.
"""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def load_json_products():
    """Load products from JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_csv_products():
    """Load products from CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price to float and id to int
                row['price'] = float(row['price'])
                row['id'] = int(row['id'])
                products.append(row)
    except (FileNotFoundError, csv.Error):
        pass
    return products

def load_sql_products():
    """Load products from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': float(row[3])
            })
        
        conn.close()
    except sqlite3.Error:
        pass
    return products

def filter_product_by_id(products, product_id):
    """Filter products by ID."""
    try:
        product_id = int(product_id)
        for product in products:
            if product['id'] == product_id:
                return [product]
        return []
    except ValueError:
        return []

@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite database."""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Load products based on source
    if source == 'json':
        products = load_json_products()
    elif source == 'csv':
        products = load_csv_products()
    elif source == 'sql':
        products = load_sql_products()
    else:
        return render_template('product_display.html', 
                             error="Wrong source. Please use 'json', 'csv', or 'sql'.")
    
    # Filter by ID if provided
    if product_id:
        products = filter_product_by_id(products, product_id)
        if not products:
            return render_template('product_display.html', 
                                 error="Product not found")
    
    return render_template('product_display.html', 
                         products=products, 
                         source=source)

if __name__ == '__main__':
    app.run(debug=True, port=5000) 