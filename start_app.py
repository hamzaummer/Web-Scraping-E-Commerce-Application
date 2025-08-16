#!/usr/bin/env python3
"""
Startup script for the E-commerce Web Scraper
"""

print("🚀 Starting E-commerce Web Scraper...")
print("=" * 50)

# Import all the components
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from scraper import EcommerceScraper
from database import Database
from visualizer import Visualizer
import pandas as pd

# Create Flask app
app = Flask(__name__)
app.secret_key = 'ecommerce_scraper_secret_key'

# Initialize components
print("📦 Initializing components...")
scraper = EcommerceScraper()
database = Database()
visualizer = Visualizer()
print("✅ Components initialized")

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    category = request.form.get('category', '')
    max_pages = int(request.form.get('max_pages', 1))
    
    if not url:
        flash('Please enter a URL to scrape', 'error')
        return redirect(url_for('index'))
    
    try:
        # Extract domain for source_site
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        source_site = parsed_url.netloc
        
        # Scrape products
        products = scraper.scrape_product_listings(url, max_pages)
        
        if not products:
            flash('No products found. Try adjusting the scraper settings.', 'warning')
            return redirect(url_for('index'))
        
        # Save to database
        database.save_products(products, source_site, category)
        
        flash(f'Successfully scraped {len(products)} products', 'success')
        return redirect(url_for('results'))
        
    except Exception as e:
        flash(f'Error during scraping: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/results')
def results():
    category = request.args.get('category')
    products = database.get_products(category=category)
    return render_template('results.html', products=products, category=category)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    if not query:
        return redirect(url_for('results'))
    
    products = database.search_products(query)
    return render_template('results.html', products=products, search_query=query)

@app.route('/visualizations')
def visualizations():
    category = request.args.get('category')
    
    # Get data for visualizations
    products = database.get_products(category=category)
    price_stats = database.get_price_stats(category=category)
    rating_stats = database.get_rating_stats(category=category)
    
    # Generate visualizations
    visualizations = {}
    
    if not price_stats.empty:
        visualizations['price_comparison'] = visualizer.price_comparison(price_stats)
    
    if not rating_stats.empty:
        visualizations['rating_comparison'] = visualizer.rating_comparison(rating_stats)
    
    if products:
        df = pd.DataFrame(products)
        visualizations['price_distribution'] = visualizer.price_distribution(df)
        visualizations['price_vs_rating'] = visualizer.price_vs_rating(df)
        visualizations['price_trends'] = visualizer.price_trends(df)
    
    return render_template('visualizations.html', 
                           visualizations=visualizations, 
                           category=category)

@app.route('/export')
def export():
    category = request.args.get('category')
    try:
        filename = database.export_to_excel(category=category)
        return jsonify({'success': True, 'filename': filename})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    print("🌐 Starting Flask server...")
    print("📱 Open your browser and go to: http://127.0.0.1:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)

    # Set Flask to show output
    import os
    os.environ['FLASK_ENV'] = 'development'

    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
