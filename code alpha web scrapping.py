import requests  # type: ignore
from bs4 import BeautifulSoup # type: ignore
import  pandas as pd # type: ignore
import html.parser
base_url ="https://books.toscrape.com/catalogue/page-{}.html"
titles, prices, stocks = [], [], []
# Scrape first 5 pages
for page in range(1, 6):
    print(f"Scraping page {page}...")
    response = requests.get(base_url.format(page))
    response.encoding ='utf-8'
    soup = BeautifulSoup(response.text, "lxml")
    
        
    books = soup.select("article.product_pod")
    
    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.replace("£", "")
        stock = book.select_one(".instock.availability").text.strip()
        
        titles.append(title)
        prices.append(float(price))

        stocks.append(stock)

# Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price (GBP)": prices,
    "Stock Status": stocks
})
        

df.to_csv("books_data.csv", index=False)
print(" Web Scraping complete. Data saved as books_data.csv") 