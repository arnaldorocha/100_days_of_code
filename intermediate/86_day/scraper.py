import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def scrape_books(pages=1):
    books = []

    for page in range(1, pages + 1):
        print(f"Scraping page {page}...")
        url = BASE_URL.format(page)
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Failed to retrieve page {page}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='product_pod')

        for article in articles:
            title = article.h3.a['title']
            price = article.find('p', class_='price_color').text.strip()
            books.append({'title': title, 'price': price})

    return books


def export_to_csv(data, filename='books.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price'])
        writer.writeheader()
        writer.writerows(data)
    print(f"Dados exportados para {filename}")


if __name__ == "__main__":
    results = scrape_books(pages=3)  # Ex: scrape 3 pages
    export_to_csv(results)
