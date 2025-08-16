# E-commerce Web Scraper

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive web scraping application for e-commerce websites with data visualization and analysis capabilities. This tool allows you to extract product information from various e-commerce sites, store the data in a local database, and generate insightful visualizations.

## 🚀 Features

- 🕷️ **Web Scraping**: Extract product data from e-commerce websites using intelligent CSS selectors
- 📊 **Data Visualization**: Generate interactive charts and graphs from scraped data
- 🔍 **Search & Filter**: Full-text search through scraped products with SQLite FTS5
- 📁 **Data Export**: Export data to Excel format for further analysis
- 💾 **Database Storage**: SQLite database for persistent storage with automatic schema creation
- 🎨 **Modern UI**: Bootstrap-based responsive web interface
- 🛡️ **Rate Limiting**: Built-in delays to respect server resources
- 🔧 **Customizable**: Easy to modify CSS selectors for specific websites

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package installer - usually comes with Python)
- **Git** (for cloning the repository)

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 2GB (4GB recommended)
- **Storage**: At least 100MB free space
- **Internet Connection**: Required for web scraping and package installation

## 🛠️ Installation

### Option 1: Quick Setup (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/web-scraping-ecom-app.git
   cd web-scraping-ecom-app
   ```

2. **Run the automated setup:**
   ```bash
   python setup.py
   ```

3. **Start the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/web-scraping-ecom-app.git
   cd web-scraping-ecom-app
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create necessary directories:**
   ```bash
   mkdir exports
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

### Option 3: Alternative Startup Scripts

- **Windows users**: Double-click `run.bat`
- **Cross-platform**: `python start_app.py`

## 📖 Usage Guide

### 1. Starting a Scraping Session

1. **Navigate to the home page** at `http://localhost:5000`
2. **Enter the target URL**: Paste the URL of an e-commerce product listing page
3. **Set category** (optional): Add a category name for better organization
4. **Configure pages**: Set the number of pages to scrape (start with 1 for testing)
5. **Click "Start Scraping"** and wait for the process to complete

### 2. Viewing and Managing Results

- **Results Page**: View all scraped products in a card-based layout
- **Search**: Use the search bar to find specific products by name or description
- **Filter**: Filter results by category if you've organized your data
- **Product Details**: Each product card shows title, price, rating, and source website

### 3. Data Visualization

Navigate to the "Visualizations" page to see:
- **Price Comparison**: Bar charts comparing average prices across different websites
- **Rating Analysis**: Visual comparison of product ratings by source
- **Price Distribution**: Histogram showing the distribution of product prices
- **Price vs Rating**: Scatter plot revealing correlations between price and ratings
- **Price Trends**: Time-series analysis of price changes over time

### 4. Exporting Data

- Click **"Export to Excel"** to download your scraped data
- Files are automatically saved in the `exports/` directory
- Each export includes timestamps for easy organization

## ⚙️ Configuration and Customization

### Customizing CSS Selectors

For better results with specific websites, modify the selectors in `scraper.py`:

```python
# Example customization for a specific e-commerce site
selectors_to_try = [
    '.product-item',           # Your custom selector
    '.listing-card',           # Alternative selector
    '.search-result-item'      # Fallback selector
]
```

### Rate Limiting

Adjust scraping delays in `scraper.py`:

```python
# Modify the delay between requests (in seconds)
time.sleep(random.uniform(1, 3))  # Random delay between 1-3 seconds
```

## 🏗️ Project Structure

```
web-scraping-ecom-app/
├── 📄 app.py                    # Main Flask application
├── 🕷️ scraper.py               # Web scraping logic and CSS selectors
├── 🗄️ database.py              # SQLite database operations
├── 📊 visualizer.py             # Data visualization with matplotlib/seaborn
├── ⚙️ setup.py                 # Automated setup script
├── 📋 requirements.txt         # Python dependencies
├── 🎨 templates/               # Jinja2 HTML templates
│   ├── index.html              # Main scraping interface
│   ├── results.html            # Product results display
│   └── visualizations.html     # Charts and graphs
├── 🎯 static/                  # Static web assets
│   ├── css/style.css           # Custom styling
│   ├── js/main.js              # JavaScript functionality
│   └── images/                 # Generated visualization images
├── 📁 exports/                 # Excel export files (auto-created)
├── 🧪 test_app.py              # Application testing suite
└── 📚 README.md                # This documentation
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. **Import Errors**
```bash
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Install dependencies with `pip install -r requirements.txt`

#### 2. **Template Not Found**
```bash
TemplateNotFound: index.html
```
**Solution**: Ensure HTML files are in the `templates/` directory

#### 3. **Static Files Not Loading**
**Solution**: Verify CSS/JS files are in the `static/` directory structure

#### 4. **No Products Found**
**Possible causes**:
- Website uses different CSS selectors
- Anti-bot protection is active
- Network connectivity issues

**Solutions**:
- Customize CSS selectors in `scraper.py`
- Test with a simple e-commerce site first
- Check your internet connection

#### 5. **Database Errors**
```bash
sqlite3.OperationalError: database is locked
```
**Solution**: Close any other instances of the application

#### 6. **Visualization Errors**
**Solution**: Ensure matplotlib backend is properly configured:
```python
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
```

### Performance Optimization

- **Memory Usage**: For large datasets, consider processing in batches
- **Scraping Speed**: Adjust delays in `scraper.py` based on target website's capacity
- **Database Performance**: Regular cleanup of old data can improve query speed

## 🛡️ Legal and Ethical Considerations

### ⚠️ Important Disclaimers

- **Respect robots.txt**: Always check `website.com/robots.txt` before scraping
- **Rate Limiting**: Don't overload servers - use appropriate delays
- **Terms of Service**: Review and comply with website terms of service
- **Copyright**: Respect intellectual property rights
- **Personal Data**: Be mindful of privacy laws (GDPR, CCPA, etc.)

### Best Practices

1. **Start Small**: Test with 1-2 pages before scaling up
2. **Use APIs When Available**: Official APIs are always preferred over scraping
3. **Monitor Impact**: Ensure your scraping doesn't affect website performance
4. **Stay Updated**: Websites change - update selectors as needed

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 2.3.3+ | Web framework |
| BeautifulSoup4 | 4.12.2+ | HTML parsing |
| Requests | 2.31.0+ | HTTP requests |
| Pandas | 2.0.3+ | Data manipulation |
| Matplotlib | 3.7.2+ | Data visualization |
| Seaborn | 0.12.2+ | Statistical visualization |
| OpenPyXL | 3.1.2+ | Excel file handling |
| Werkzeug | 2.3.7+ | WSGI utilities |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) web framework
- UI components from [Bootstrap](https://getbootstrap.com/)
- Data visualization powered by [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)
- Web scraping with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Create a new issue with detailed information about your problem and reach out to me at the E-Mail provided below
   <br>
   G-Mail : mohammedhamza7428@gmail.com

---

**⚠️ Disclaimer**: This tool is for educational and research purposes only. Users are responsible for ensuring their use complies with applicable laws and website terms of service.
