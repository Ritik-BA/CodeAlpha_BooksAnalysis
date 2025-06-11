
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('books_data.csv')

# Basic Info
print("Dataset Info:")
print(df.info())

# Describe dataset
print("\nDescriptive Statistics:")
print(df.describe())

# Top 5 most expensive books
top5_expensive = df.sort_values(by='Price (GBP)', ascending=False).head(5)
print("\nTop 5 Most Expensive Books:")
print(top5_expensive[['Title', 'Price (GBP)']])

# Plot - Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Price (GBP)'], kde=True, bins=6, color='skyblue')
plt.title('Price Distribution of Books')
plt.xlabel('Price (GBP)')
plt.ylabel('Number of Books')
plt.grid(True)
plt.tight_layout()
plt.savefig('price_distribution.png')
plt.show()

# Bar Plot - Top 5 Expensive Books
plt.figure(figsize=(15,10))
sns.barplot(x='Price (GBP)', y='Title', data=top5_expensive, palette='viridis')
plt.title('Top 5 Most Expensive Books')
plt.xlabel('Price (GBP)')
plt.ylabel('Book Title')
plt.tight_layout()
plt.savefig('top5_books.png')
plt.show()
