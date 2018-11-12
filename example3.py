# Modules for url request, web scraping, and regex
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

## NAVIGATE ACROSS ALL RELEVANT PAGES 1 to 33
## After page 33, almost all topics are people, not reports
for page_no in range(1, 33):

    link = "https://www.rand.org/topics/cyber-and-data-sciences.html?page=" + str(page_no)
    # Open website and convert into beautiful soup object
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')

    # Extract all attributes of each item - type, blurb, and date
    type_list  = bs.find_all('p', {'class', 'type'})
    #title_list = bs.select('header> h3 > a') Too hard to just extract titles. It stumped me.
    blurb_list = bs.find_all('p', {'class', 'desc'})
    date_list  = bs.find_all('p', {'class', 'date'})

    #Loop through items
    for index, item in enumerate(type_list):
        #print("Title: " + title_list[index].text.strip())
        print("Type: "  + type_list[index].text.strip())
        print("Date: "  + date_list[index].text.strip())
        print("Blurb: " + blurb_list[index].text.strip())
        print("")