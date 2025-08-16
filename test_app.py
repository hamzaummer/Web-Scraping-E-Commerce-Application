#!/usr/bin/env python3
"""
Test script to verify the application components work correctly
"""

import sys
import traceback

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import flask
        print("✅ Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        import requests
        print("✅ Requests imported successfully")
    except ImportError as e:
        print(f"❌ Requests import failed: {e}")
        return False
    
    try:
        import bs4
        print("✅ BeautifulSoup4 imported successfully")
    except ImportError as e:
        print(f"❌ BeautifulSoup4 import failed: {e}")
        return False
    
    try:
        import pandas
        print("✅ Pandas imported successfully")
    except ImportError as e:
        print(f"❌ Pandas import failed: {e}")
        return False
    
    try:
        import matplotlib
        print("✅ Matplotlib imported successfully")
    except ImportError as e:
        print(f"❌ Matplotlib import failed: {e}")
        return False
    
    try:
        import seaborn
        print("✅ Seaborn imported successfully")
    except ImportError as e:
        print(f"❌ Seaborn import failed: {e}")
        return False
    
    return True

def test_app_components():
    """Test if application components can be initialized"""
    print("\nTesting application components...")
    
    try:
        from scraper import EcommerceScraper
        scraper = EcommerceScraper()
        print("✅ Scraper initialized successfully")
    except Exception as e:
        print(f"❌ Scraper initialization failed: {e}")
        return False
    
    try:
        from database import Database
        db = Database()
        print("✅ Database initialized successfully")
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return False
    
    try:
        from visualizer import Visualizer
        viz = Visualizer()
        print("✅ Visualizer initialized successfully")
    except Exception as e:
        print(f"❌ Visualizer initialization failed: {e}")
        return False
    
    try:
        from app import app
        print("✅ Flask app initialized successfully")
    except Exception as e:
        print(f"❌ Flask app initialization failed: {e}")
        return False
    
    return True

def test_database():
    """Test basic database operations"""
    print("\nTesting database operations...")
    
    try:
        from database import Database
        db = Database()
        
        # Test connection
        db.connect()
        db.disconnect()
        print("✅ Database connection test passed")
        
        # Test sample data insertion
        sample_products = [{
            'title': 'Test Product',
            'price': 29.99,
            'rating': 4.5,
            'description': 'Test description',
            'url': 'http://example.com',
            'image_url': 'http://example.com/image.jpg',
            'timestamp': 1234567890
        }]
        
        db.save_products(sample_products, 'test-site', 'test-category')
        print("✅ Database save test passed")
        
        # Test retrieval
        products = db.get_products(limit=1)
        if products:
            print("✅ Database retrieval test passed")
        else:
            print("⚠️ Database retrieval returned no results")
        
        return True
        
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("🧪 Running Application Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test components
    if not test_app_components():
        all_passed = False
    
    # Test database
    if not test_database():
        all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! The application should work correctly.")
        print("\nTo start the application, run:")
        print("  python app.py")
    else:
        print("❌ Some tests failed. Please check the error messages above.")
        print("Make sure you've run: python setup.py")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
