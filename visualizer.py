import os
import pandas as pd
from io import BytesIO
import base64

# Try to import visualization libraries
try:
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    VISUALIZATION_AVAILABLE = True
except ImportError as e:
    print(f"⚠️  Visualization libraries not available: {e}")
    print("📊 Charts and graphs will be disabled, but the app will still work")
    VISUALIZATION_AVAILABLE = False
    # Create dummy objects to prevent errors
    plt = None
    sns = None
    np = None

class Visualizer:
    def __init__(self):
        self.visualization_available = VISUALIZATION_AVAILABLE

        if self.visualization_available:
            # Set the style for all visualizations
            sns.set_style("whitegrid")
            plt.rcParams['figure.figsize'] = (10, 6)
            plt.rcParams['font.size'] = 12

        # Create directory for saving visualizations
        os.makedirs('static/images', exist_ok=True)
    
    def _fig_to_base64(self, fig):
        """Convert matplotlib figure to base64 string for embedding in HTML"""
        if not self.visualization_available:
            return None

        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        img_str = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        return img_str

    def _create_fallback_message(self, chart_type):
        """Create a fallback message when visualization is not available"""
        return f"📊 {chart_type} chart not available - visualization libraries not installed"
    
    def price_comparison(self, df, title="Price Comparison Across Websites"):
        """Create a price comparison visualization"""
        if not self.visualization_available:
            return None

        fig, ax = plt.subplots()
        
        # Create a bar chart for average prices
        sns.barplot(x='source_site', y='avg_price', data=df, ax=ax, palette='viridis')
        
        # Add error bars showing min and max prices
        for i, row in df.iterrows():
            ax.errorbar(i, row['avg_price'], 
                       yerr=[[row['avg_price'] - row['min_price']], [row['max_price'] - row['avg_price']]],
                       fmt='none', ecolor='red', capsize=5)
        
        ax.set_title(title)
        ax.set_xlabel('Website')
        ax.set_ylabel('Price ($)')
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')
        
        # Add value labels on top of bars
        for i, v in enumerate(df['avg_price']):
            ax.text(i, v + 1, f"${v:.2f}", ha='center')
        
        plt.tight_layout()
        return self._fig_to_base64(fig)
    
    def rating_comparison(self, df, title="Rating Comparison Across Websites"):
        """Create a rating comparison visualization"""
        if not self.visualization_available:
            return None

        fig, ax = plt.subplots()
        
        # Create a bar chart for average ratings
        bars = sns.barplot(x='source_site', y='avg_rating', data=df, ax=ax, palette='viridis')
        
        ax.set_title(title)
        ax.set_xlabel('Website')
        ax.set_ylabel('Average Rating (out of 5)')
        
        # Set y-axis to start from 0 and end at 5
        ax.set_ylim(0, 5)
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')
        
        # Add value labels on top of bars
        for i, v in enumerate(df['avg_rating']):
            ax.text(i, v + 0.1, f"{v:.1f}", ha='center')
        
        plt.tight_layout()
        return self._fig_to_base64(fig)
    
    def price_distribution(self, products, title="Price Distribution"):
        """Create a price distribution visualization"""
        if not self.visualization_available:
            return None

        # Convert to DataFrame if it's a list of dictionaries
        if isinstance(products, list):
            df = pd.DataFrame(products)
        else:
            df = products

        # Filter out products with no price
        df = df[df['price'].notna()]

        fig, ax = plt.subplots()
        
        # Create a histogram with KDE
        sns.histplot(df['price'], kde=True, ax=ax, bins=20, color='skyblue')
        
        ax.set_title(title)
        ax.set_xlabel('Price ($)')
        ax.set_ylabel('Number of Products')
        
        # Add vertical line for mean price
        mean_price = df['price'].mean()
        ax.axvline(mean_price, color='red', linestyle='--', linewidth=1)
        ax.text(mean_price + 1, ax.get_ylim()[1] * 0.9, f'Mean: ${mean_price:.2f}', color='red')
        
        plt.tight_layout()
        return self._fig_to_base64(fig)
    
    def price_vs_rating(self, products, title="Price vs. Rating"):
        """Create a scatter plot of price vs. rating"""
        if not self.visualization_available:
            return None

        # Convert to DataFrame if it's a list of dictionaries
        if isinstance(products, list):
            df = pd.DataFrame(products)
        else:
            df = products

        # Filter out products with no price or rating
        df = df[(df['price'].notna()) & (df['rating'].notna())]

        fig, ax = plt.subplots()
        
        # Create a scatter plot with regression line
        sns.regplot(x='rating', y='price', data=df, ax=ax, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
        
        ax.set_title(title)
        ax.set_xlabel('Rating')
        ax.set_ylabel('Price ($)')
        
        # Set x-axis to start from 0 and end at 5
        ax.set_xlim(0, 5)
        
        plt.tight_layout()
        return self._fig_to_base64(fig)
    
    def price_trends(self, products, title="Price Trends Over Time"):
        """Create a visualization of price trends over time"""
        if not self.visualization_available:
            return None

        # Convert to DataFrame if it's a list of dictionaries
        if isinstance(products, list):
            df = pd.DataFrame(products)
        else:
            df = products

        # Convert timestamp to datetime and filter out products with no price
        df = df[df['price'].notna()].copy()
        df['date'] = pd.to_datetime(df['timestamp'], unit='s')

        # Group by date and calculate average price
        daily_avg = df.groupby(df['date'].dt.date)['price'].mean().reset_index()

        fig, ax = plt.subplots()
        
        # Create a line plot
        sns.lineplot(x='date', y='price', data=daily_avg, ax=ax, marker='o')
        
        ax.set_title(title)
        ax.set_xlabel('Date')
        ax.set_ylabel('Average Price ($)')
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')
        
        plt.tight_layout()
        return self._fig_to_base64(fig)