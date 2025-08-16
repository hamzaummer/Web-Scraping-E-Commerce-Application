#!/usr/bin/env python3
"""
Deployment verification script for Web Scraping Ecom App
This script verifies that the application can be run from a fresh clone
"""

import os
import sys
import subprocess
import importlib.util

def check_file_structure():
    """Verify that all required files are present"""
    print("📁 Checking file structure...")
    
    required_files = [
        'app.py',
        'scraper.py', 
        'database.py',
        'visualizer.py',
        'requirements.txt',
        'README.md',
        'LICENSE',
        'setup.py'
    ]
    
    required_dirs = [
        'templates',
        'static',
        'static/css',
        'static/js'
    ]
    
    missing_files = []
    missing_dirs = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ {file}")
    
    for directory in required_dirs:
        if not os.path.exists(directory):
            missing_dirs.append(directory)
        else:
            print(f"✅ {directory}/")
    
    if missing_files or missing_dirs:
        print("\n❌ Missing files/directories:")
        for item in missing_files + missing_dirs:
            print(f"   - {item}")
        return False
    
    print("✅ All required files and directories present")
    return True

def check_python_version():
    """Check if Python version is compatible"""
    print("\n🐍 Checking Python version...")
    
    if sys.version_info < (3, 7):
        print(f"❌ Python {sys.version_info.major}.{sys.version_info.minor} is too old")
        print("   Requires Python 3.7 or higher")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True

def check_imports():
    """Test if core modules can be imported"""
    print("\n📦 Testing core module imports...")
    
    modules = [
        ('app', 'Flask application'),
        ('scraper', 'Web scraper'),
        ('database', 'Database handler'),
        ('visualizer', 'Data visualizer')
    ]
    
    for module_name, description in modules:
        try:
            spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"✅ {description}")
        except Exception as e:
            print(f"❌ {description}: {e}")
            return False
    
    return True

def check_dependencies():
    """Check if required packages can be imported"""
    print("\n📚 Checking dependencies...")
    
    dependencies = [
        ('flask', 'Flask'),
        ('bs4', 'BeautifulSoup4'),
        ('requests', 'Requests'),
        ('pandas', 'Pandas'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('openpyxl', 'OpenPyXL')
    ]
    
    missing = []
    
    for module_name, display_name in dependencies:
        try:
            __import__(module_name)
            print(f"✅ {display_name}")
        except ImportError:
            print(f"❌ {display_name}")
            missing.append(display_name)
    
    if missing:
        print(f"\n⚠️  Missing dependencies: {', '.join(missing)}")
        print("   Run: python setup.py")
        print("   Or: pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main verification function"""
    print("🔍 Web Scraping Ecom App - Deployment Verification")
    print("=" * 60)
    
    checks = [
        ("File Structure", check_file_structure),
        ("Python Version", check_python_version),
        ("Core Modules", check_imports),
        ("Dependencies", check_dependencies)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("🎉 All verification checks passed!")
        print("\n✅ The application is ready to run:")
        print("   python app.py")
        print("\n🌐 Then open: http://localhost:5000")
    else:
        print("❌ Some verification checks failed.")
        print("\n🔧 Please fix the issues above before running the application.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
