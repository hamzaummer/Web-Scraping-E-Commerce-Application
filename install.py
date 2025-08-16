#!/usr/bin/env python3
"""
Simple installation script for E-commerce Web Scraper
This script tries multiple installation approaches for maximum compatibility
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and return success status"""
    print(f"🔧 {description}...")
    try:
        subprocess.check_call(command, shell=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        return False

def install_basic_packages():
    """Install basic packages that should work on any Python version"""
    basic_packages = [
        "flask",
        "beautifulsoup4", 
        "requests",
        "openpyxl"
    ]
    
    print("📦 Installing basic packages...")
    success = True
    
    for package in basic_packages:
        if not run_command(f"{sys.executable} -m pip install {package}", f"Installing {package}"):
            success = False
    
    return success

def install_data_packages():
    """Try to install data science packages with fallbacks"""
    data_packages = ["pandas", "matplotlib", "seaborn"]
    
    print("📊 Installing data science packages...")
    
    for package in data_packages:
        # Try normal installation first
        if run_command(f"{sys.executable} -m pip install {package}", f"Installing {package}"):
            continue
        
        # Try with --no-build-isolation for problematic packages
        if run_command(f"{sys.executable} -m pip install --no-build-isolation {package}", f"Installing {package} (no build isolation)"):
            continue
        
        # Try installing pre-release versions
        if run_command(f"{sys.executable} -m pip install --pre {package}", f"Installing {package} (pre-release)"):
            continue
        
        print(f"⚠️  Could not install {package} - visualization features may be limited")

def main():
    """Main installation function"""
    print("🚀 Installing E-commerce Web Scraper Dependencies")
    print("=" * 60)
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    print(f"🐍 Python version: {python_version}")
    
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        return False
    
    # Upgrade pip first
    run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrading pip")
    
    # Install basic packages
    if not install_basic_packages():
        print("❌ Failed to install basic packages. Please check your internet connection.")
        return False
    
    # Try to install data science packages
    install_data_packages()
    
    # Create necessary directories
    os.makedirs("static/images", exist_ok=True)
    os.makedirs("exports", exist_ok=True)
    print("✅ Created necessary directories")
    
    print("\n" + "=" * 60)
    print("🎉 Installation completed!")
    print("\nTo test the installation, run:")
    print("  python test_app.py")
    print("\nTo start the application, run:")
    print("  python app.py")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Installation failed. Please check the error messages above.")
        sys.exit(1)
