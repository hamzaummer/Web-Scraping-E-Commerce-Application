#!/usr/bin/env python3
"""
Simple run script for the E-commerce Web Scraper
"""

import os
import sys
import webbrowser
import time
from threading import Timer

def open_browser():
    """Open the browser after a short delay"""
    time.sleep(2)  # Wait for Flask to start
    webbrowser.open('http://localhost:5000')

def main():
    """Main function to run the application"""
    print("🚀 Starting E-commerce Web Scraper...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found!")
        print("Make sure you're running this from the project directory.")
        sys.exit(1)
    
    # Check if dependencies are installed
    try:
        import flask
        import requests
        import bs4
        import pandas
        import matplotlib
        import seaborn
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: python setup.py")
        sys.exit(1)
    
    print("✅ All dependencies found")
    print("🌐 Starting web server...")
    print("📱 The application will open in your browser automatically")
    print("\n🔗 URL: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Open browser after a delay
    Timer(2.0, open_browser).start()
    
    # Import and run the Flask app
    try:
        from app import app
        app.run(debug=True, use_reloader=False)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
