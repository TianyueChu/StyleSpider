import requests
from bs4 import BeautifulSoup
import re


def crawler(num_page, baseurl):
    page = 1
    url_lists = []
    price_lists = []
    priceList = []

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }

    while page != num_page:
        url = baseurl + f"?page={page}"
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.content, "lxml")
        productList = soup.find_all('li', attrs={
            'class': [re.compile(r'^product-grid-block-dynamic product-grid-block-dynamic__container')
                , re.compile(r'^product-grid-product _product')]})
        # productList.append(soup.find_all('li', attrs = {'class': re.compile(r'^product-grid-product _product')})
        # print(productList)

        for item in productList:
            prices = item.find_all('span', class_="price-current__amount")
            for price in prices:
                price_lists.append(price.get_text(strip=True))
                priceList.append(item)

        for product in priceList:
            # print(product)
            link = product.find('a', href=True)
            # print(link)
            url_lists.append(link['href'])

        page = page + 1

    return price_lists, url_lists
