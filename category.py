import requests
from bs4 import BeautifulSoup

import config


def categorylist(baseurl):
    header = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
    r = requests.get(baseurl, headers=header)
    soup = BeautifulSoup(r.content, "lxml")
    categoryLink = soup.find_all('a', class_="layout-categories-category__link link")
    category_list = []
    for link in categoryLink:
      list = link.get("href")
      if list:
        category_list.append(list)
    return category_list


if __name__ == "__main__":
    baseurl = config.baseurl
    category_list = categorylist(baseurl)
    print("category list", category_list)
    print("end point", category_list.index('https://www.zara.com/es/en/woman-shoes-l1251.html'))