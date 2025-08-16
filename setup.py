#!/usr/bin/env python3
"""
Setup script for E-commerce Web Scraper
This script helps set up the environment and install dependencies
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages from requirements.txt"""
    print("Installing required packages...")

    # Check Python version and choose appropriate requirements file
    if sys.version_info >= (3, 13):
        print("⚠️  Python 3.13 detected - using compatible package versions...")
        requirements_file = "requirements-python313.txt"
    else:
        requirements_file = "requirements.txt"

    try:
        # First try to install with the chosen requirements file
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        print("\n🔧 Trying alternative installation method...")

        # Try installing packages individually with fallbacks
        packages = [
            "flask>=2.0.0",
            "beautifulsoup4>=4.10.0",
            "requests>=2.25.0",
            "openpyxl>=3.0.0"
        ]

        # Try to install data science packages
        data_packages = ["pandas", "matplotlib", "seaborn"]

        success = True
        for package in packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                success = False

        # Try data science packages with fallbacks
        for package in data_packages:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"⚠️  Failed to install {package} - visualization features may be limited")

        return success

def create_directories():
    """Create necessary directories"""
    directories = [
        "static/images",
        "exports"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        return False
    print(f"✅ Python version {sys.version_info.major}.{sys.version_info.minor} is compatible")
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up E-commerce Web Scraper...")
    print("=" * 50)

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Create directories
    create_directories()

    # Install requirements
    if not install_requirements():
        print("\n❌ Setup failed! Please check the error messages above.")
        print("\n🔧 Troubleshooting tips:")
        print("1. Make sure you have an active internet connection")
        print("2. Try running: pip install --upgrade pip")
        print("3. If on Windows, you may need Visual C++ Build Tools")
        print("4. Try installing packages individually: pip install flask beautifulsoup4 requests")
        sys.exit(1)

    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n🚀 Next steps:")
    print("1. Run the application:")
    print("   python app.py")
    print("\n2. Open your browser and go to:")
    print("   http://localhost:5000")
    print("\n3. Start scraping e-commerce websites!")
    print("\n📚 For help and documentation, see README.md")

if __name__ == "__main__":
    main()
