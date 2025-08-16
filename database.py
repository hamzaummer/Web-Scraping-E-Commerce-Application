import sqlite3
import pandas as pd
import os
import json

class Database:
    def __init__(self, db_path='ecommerce_data.db'):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.initialize_db()
    
    def connect(self):
        """Connect to the SQLite database"""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.conn
    
    def disconnect(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
    
    def initialize_db(self):
        """Create the database tables if they don't exist"""
        self.connect()
        
        # Create products table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price REAL,
            rating REAL,
            description TEXT,
            url TEXT,
            image_url TEXT,
            source_site TEXT,
            category TEXT,
            additional_data TEXT,
            timestamp REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create a search index
        self.cursor.execute('''
        CREATE VIRTUAL TABLE IF NOT EXISTS product_search 
        USING fts5(title, description, category)
        ''')
        
        self.conn.commit()
        self.disconnect()
    
    def save_products(self, products, source_site, category=''):
        """Save multiple products to the database"""
        self.connect()
        
        for product in products:
            # Convert any additional data to JSON string
            additional_data = {}
            for key, value in product.items():
                if key not in ['title', 'price', 'rating', 'description', 'url', 'image_url', 'timestamp']:
                    additional_data[key] = value
            
            additional_data_json = json.dumps(additional_data)
            
            # Insert into products table
            self.cursor.execute('''
            INSERT INTO products 
            (title, price, rating, description, url, image_url, source_site, category, additional_data, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                product.get('title', ''),
                product.get('price'),
                product.get('rating'),
                product.get('description', ''),
                product.get('url', ''),
                product.get('image_url', ''),
                source_site,
                category,
                additional_data_json,
                product.get('timestamp', 0)
            ))
            
            # Get the ID of the inserted product
            product_id = self.cursor.lastrowid
            
            # Insert into search index
            self.cursor.execute('''
            INSERT INTO product_search (rowid, title, description, category)
            VALUES (?, ?, ?, ?)
            ''', (
                product_id,
                product.get('title', ''),
                product.get('description', ''),
                category
            ))
        
        self.conn.commit()
        self.disconnect()
    
    def search_products(self, query, limit=20):
        """Search for products using FTS5"""
        self.connect()
        
        self.cursor.execute('''
        SELECT p.* FROM products p
        JOIN product_search ps ON p.id = ps.rowid
        WHERE product_search MATCH ?
        ORDER BY p.rating DESC, p.price ASC
        LIMIT ?
        ''', (query, limit))
        
        results = self.cursor.fetchall()
        
        # Convert to list of dictionaries
        columns = [desc[0] for desc in self.cursor.description]
        products = [dict(zip(columns, row)) for row in results]
        
        self.disconnect()
        return products
    
    def get_products(self, category=None, limit=100, order_by='timestamp DESC'):
        """Get products with optional filtering"""
        self.connect()
        
        query = 'SELECT * FROM products'
        params = []
        
        if category:
            query += ' WHERE category = ?'
            params.append(category)
        
        query += f' ORDER BY {order_by} LIMIT ?'
        params.append(limit)
        
        self.cursor.execute(query, params)
        results = self.cursor.fetchall()
        
        # Convert to list of dictionaries
        columns = [desc[0] for desc in self.cursor.description]
        products = [dict(zip(columns, row)) for row in results]
        
        self.disconnect()
        return products
    
    def export_to_excel(self, filename=None, category=None):
        """Export product data to Excel"""
        import os
        from datetime import datetime

        # Create exports directory if it doesn't exist
        os.makedirs('exports', exist_ok=True)

        # Generate filename if not provided
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            category_suffix = f"_{category}" if category else ""
            filename = f'exports/product_data{category_suffix}_{timestamp}.xlsx'
        elif not filename.startswith('exports/'):
            filename = f'exports/{filename}'

        self.connect()

        query = 'SELECT * FROM products'
        params = []

        if category:
            query += ' WHERE category = ?'
            params.append(category)

        df = pd.read_sql_query(query, self.conn, params=params)

        if df.empty:
            self.disconnect()
            raise ValueError("No data to export")

        # Convert timestamp to datetime
        df['date'] = pd.to_datetime(df['timestamp'], unit='s')

        # Reorder columns for better readability
        column_order = ['title', 'price', 'rating', 'description', 'source_site',
                       'category', 'url', 'image_url', 'date', 'created_at']
        df = df[[col for col in column_order if col in df.columns]]

        # Save to Excel
        df.to_excel(filename, index=False, engine='openpyxl')

        self.disconnect()
        return filename
    
    def get_price_stats(self, category=None):
        """Get price statistics for visualization"""
        self.connect()
        
        query = '''
        SELECT 
            source_site,
            COUNT(*) as count,
            AVG(price) as avg_price,
            MIN(price) as min_price,
            MAX(price) as max_price
        FROM products
        '''
        
        params = []
        if category:
            query += ' WHERE category = ?'
            params.append(category)
        
        query += ' GROUP BY source_site'
        
        df = pd.read_sql_query(query, self.conn, params=params)
        
        self.disconnect()
        return df
    
    def get_rating_stats(self, category=None):
        """Get rating statistics for visualization"""
        self.connect()
        
        query = '''
        SELECT 
            source_site,
            COUNT(*) as count,
            AVG(rating) as avg_rating
        FROM products
        WHERE rating IS NOT NULL
        '''
        
        params = []
        if category:
            query += ' AND category = ?'
            params.append(category)
        
        query += ' GROUP BY source_site'
        
        df = pd.read_sql_query(query, self.conn, params=params)
        
        self.disconnect()
        return df