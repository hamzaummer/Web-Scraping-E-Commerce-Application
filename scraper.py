import requests
import requests.exceptions
from bs4 import BeautifulSoup
import re
import time
import random

class EcommerceScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        self.session = requests.Session()
    
    def scrape_product_listings(self, url, max_pages=1):
        """Scrape multiple pages of product listings"""
        all_products = []
        
        for page in range(1, max_pages + 1):
            # Modify URL for pagination if needed
            page_url = f"{url}?page={page}" if page > 1 else url
            
            try:
                products = self._scrape_page(page_url)
                all_products.extend(products)
                
                # Be nice to the server
                time.sleep(random.uniform(1, 3))
                
            except Exception as e:
                print(f"Error scraping page {page}: {e}")
                break
        
        return all_products
    
    def _scrape_page(self, url):
        """Scrape a single page of product listings"""
        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            if response.status_code != 200:
                raise Exception(f"Failed to fetch page: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {str(e)}")

        soup = BeautifulSoup(response.content, 'html.parser')
        products = []

        # Try multiple common selectors for e-commerce sites
        selectors_to_try = [
            '.product-container', '.product', '.item', '.product-item',
            '[data-product]', 'li.product', '.product-card', '.listing-item',
            '.search-result', '.product-tile', '.grid-item', '.product-box',
            'article', '.card', '.product-wrapper'
        ]

        product_containers = []
        for selector in selectors_to_try:
            containers = soup.select(selector)
            if containers:
                product_containers = containers
                print(f"Found {len(containers)} products using selector: {selector}")
                break

        if not product_containers:
            print("Warning: No product containers found. The website structure may not be supported.")
            return []

        for container in product_containers:
            product = self._extract_product_data(container)
            if product:
                products.append(product)

        return products
    
    def _extract_product_data(self, container):
        """Extract product data from a container element"""
        try:
            # Try multiple selectors for title
            title_selectors = [
                '.product-title', '.title', 'h1', 'h2', 'h3', 'h4',
                '.name', '.product-name', '[data-title]', '.item-title'
            ]
            title_elem = None
            for selector in title_selectors:
                title_elem = container.select_one(selector)
                if title_elem:
                    break

            # Try multiple selectors for price
            price_selectors = [
                '.price', '.product-price', '.cost', '.amount', '[data-price]',
                '.price-current', '.sale-price', '.regular-price', '.money'
            ]
            price_elem = None
            for selector in price_selectors:
                price_elem = container.select_one(selector)
                if price_elem:
                    break

            # Try multiple selectors for rating
            rating_selectors = [
                '.rating', '.stars', '.star-rating', '.review-stars',
                '[data-rating]', '.score', '.rate'
            ]
            rating_elem = None
            for selector in rating_selectors:
                rating_elem = container.select_one(selector)
                if rating_elem:
                    break

            # Extract the product URL
            link_elem = container.select_one('a')
            product_url = link_elem.get('href') if link_elem else None

            # Extract image URL
            img_elem = container.select_one('img')
            image_url = img_elem.get('src') or img_elem.get('data-src') if img_elem else None

            # Clean and process the data
            title = title_elem.text.strip() if title_elem else 'Unknown Product'

            price = None
            if price_elem:
                price_text = price_elem.text.strip()
                # More robust price extraction
                price_match = re.search(r'[\d,]+\.?\d*', price_text.replace(',', ''))
                if price_match:
                    try:
                        price = float(price_match.group().replace(',', ''))
                    except ValueError:
                        pass

            rating = None
            if rating_elem:
                rating_text = rating_elem.text.strip()
                # Look for rating out of 5
                rating_match = re.search(r'(\d+(?:\.\d+)?)', rating_text)
                if rating_match:
                    try:
                        rating = float(rating_match.group())
                        # Normalize rating to 5-star scale if needed
                        if rating > 5:
                            rating = rating / 2  # Assume 10-star scale
                    except ValueError:
                        pass

            # Get description if available
            desc_selectors = [
                '.description', '.product-desc', '.summary', '.excerpt',
                '.product-summary', '[data-description]'
            ]
            description = ''
            for selector in desc_selectors:
                desc_elem = container.select_one(selector)
                if desc_elem:
                    description = desc_elem.text.strip()
                    break

            # Only return product if we have at least a title
            if title and title != 'Unknown Product':
                return {
                    'title': title,
                    'price': price,
                    'rating': rating,
                    'description': description,
                    'url': product_url,
                    'image_url': image_url,
                    'timestamp': time.time()
                }

        except Exception as e:
            print(f"Error extracting product data: {e}")
            return None
    
    def scrape_product_details(self, url):
        """Scrape detailed information from a product page"""
        response = self.session.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch product details: {response.status_code}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # These selectors will need to be customized for the target website
        title_elem = soup.select_one('h1') or soup.select_one('.product-title')
        price_elem = soup.select_one('.price') or soup.select_one('#price')
        rating_elem = soup.select_one('.rating') or soup.select_one('.stars')
        desc_elem = soup.select_one('.description') or soup.select_one('#description')
        
        # Extract specifications if available
        specs = {}
        specs_table = soup.select_one('.specifications') or soup.select_one('.specs')
        if specs_table:
            rows = specs_table.select('tr')
            for row in rows:
                cols = row.select('td')
                if len(cols) >= 2:
                    key = cols[0].text.strip()
                    value = cols[1].text.strip()
                    specs[key] = value
        
        # Clean and process the data
        title = title_elem.text.strip() if title_elem else 'Unknown'
        
        price = None
        if price_elem:
            price_text = price_elem.text.strip()
            price_match = re.search(r'\d+(\.\d+)?', price_text)
            if price_match:
                price = float(price_match.group())
        
        rating = None
        if rating_elem:
            rating_text = rating_elem.text.strip()
            rating_match = re.search(r'\d+(\.\d+)?', rating_text)
            if rating_match:
                rating = float(rating_match.group())
        
        description = desc_elem.text.strip() if desc_elem else ''
        
        # Get images
        image_elems = soup.select('.product-image img') or soup.select('.gallery img')
        images = [img.get('src') for img in image_elems if img.get('src')]
        
        return {
            'title': title,
            'price': price,
            'rating': rating,
            'description': description,
            'specifications': specs,
            'images': images,
            'url': url,
            'timestamp': time.time()
        }