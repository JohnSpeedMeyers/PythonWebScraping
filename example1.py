## TOY EXAMPLE 1
## SCRAPE COMPUTER PRODUCT DATA
## https://www.webscraper.io/test-sites/e-commerce/allinone/computers/laptops

# Modules for url request, web scraping, and regex
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

# Open website and convert into beautiful soup object
html = urlopen('https://www.webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
bs = BeautifulSoup(html, 'html.parser')

# Extract all titles and prices of products
title_list = bs.find_all('a', {'class', 'title'})
price_list = bs.find_all('h4', {'class', 'pull-right price'})
description_list = bs.find_all('p', {'class', 'description'})

# Loop through products, print product name and price
for index, item in enumerate(title_list):
    print("Product: " + item.attrs['title'] + ", Price: " + price_list[index].text.strip() )
    print("Description: " + description_list[index].text.strip())
    print("")