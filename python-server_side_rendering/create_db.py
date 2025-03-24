#!/usr/bin/env python3
"""
Script to create and populate the SQLite database.
"""

import sqlite3

def create_database():
    """Create and populate the SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99),
            (3, 'Headphones', 'Electronics', 99.99),
            (4, 'Desk Chair', 'Furniture', 199.99)
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database() 