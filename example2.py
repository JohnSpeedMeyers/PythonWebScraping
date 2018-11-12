## Scrape computer product data across multiple pages
## Toy example 2
## John Speed Meyers

# Modules for url request, web scraping, and regex
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

## Loop through pages -- the pagination is for 1-20
for page_no in range(1, 21):

    link = "http://webscraperio.us-east-1.elasticbeanstalk.com/test-sites/e-commerce/static/computers/laptops?page=" + str(page_no)
    # Open website and convert into beautiful soup object
    html = urlopen(link)
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