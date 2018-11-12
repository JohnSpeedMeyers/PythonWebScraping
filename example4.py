# Modules for url request, web scraping, and regex
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import numpy as np

# Regular expression language to extract bedroom count and square footage
br = re.compile(r'\dbr')  # Bedroom pattern
ft = re.compile(r'\d+ft') # Square footage pattern

# Open up website to find total count of entries
# Necessary to know how many pages to loop through
html = urlopen("https://losangeles.craigslist.org/d/vacation-rentals/search/vac")
bs = BeautifulSoup(html, 'html.parser')
total_count = int(bs.find('span', {'class', 'totalcount'}).text.strip())


## Loop across all pages in counts of 120 - Craigslist idiom
for count in np.arange(0, total_count, 120):
    
    # Open website and convert into beautiful soup object
    link = "https://losangeles.craigslist.org/search/vac?s=" + str(count)
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')

    # Extract all house postings
    houses = bs.find_all('li', {'class', 'result-row'})

    for house in houses: # Loop through houses

        # Extract data on each house
        title    = house.find("a", {'class','result-title hdrlnk'})    
        price    = house.find('span', {'class', 'result-price'})
        location = house.find('span', {'class', 'result-hood'})
        size     = house.find('span', {'class', 'housing'})

        # Print given attribute only if that house has that attribute
        if title is not None:
            print("Title: " + title.get_text())
        if price is not None:    
            print("Price: " + price.get_text())
        if location is not None:
            print("Location: " + location.get_text())
        if size is not None:
            print("Number of bedrooms: " + str(br.findall(size.get_text())))
            print("Square footage: "     + str(ft.findall(size.get_text())))
        print("")     
        