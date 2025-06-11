import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('books_data.csv')

# Set up plotting style
sns.set(style='whitegrid')

# 1. Histogram of Book Prices
plt.figure(figsize=(8, 5))
sns.histplot(df['Price (GBP)'], bins=6, color='coral', kde=True)
plt.title('Histogram of Book Prices')
plt.xlabel('Price (GBP)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histogram_book_prices.png')
plt.show()

# 2. Boxplot of Book Prices
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Price (GBP)'], color='lightblue')
plt.title('Boxplot of Book Prices')
plt.tight_layout()
plt.savefig('boxplot_book_prices.png')
plt.show()

# 3. Bar Plot: All Books Sorted by Price (with shortened titles)
plt.figure(figsize=(10,6))

# Shorten long titles to 20 characters
df['Short Title'] = df['Title'].apply(lambda x: x if len(x) <= 20 else x[:20] + '...')

# Sort by price
sorted_df = df.sort_values('Price (GBP)', ascending=False)

# Use 'Short Title' for plotting
sns.barplot(x='Price (GBP)', y='Short Title', data=sorted_df, palette='magma')
plt.title('Book Prices (High to Low)')
plt.xlabel('Price (GBP)')
plt.ylabel('Book Title')
plt.tight_layout()
plt.savefig('barplot_all_books_short_titles.png')
plt.show()


# 4. Pie Chart: Stock Availability (simulated data)
stock_counts = df['Stock Status'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(stock_counts, labels=stock_counts.index, autopct='%1.1f%%', colors=['lightgreen'])
plt.title('Stock Availability')
plt.tight_layout()
plt.savefig('pie_stock_status.png')
plt.show()
