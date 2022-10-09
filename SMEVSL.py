'''Gather company data more quickly'''

#modules for application use
import re
from bs4 import BeautifulSoup
import requests
import json
import os

items_found = {}

def search():
    search_term = input('what would you like to search  for? ') # input from user

    #link we want to use
    url = f"https://find-and-update.company-information.service.gov.uk/search?q={search_term}"
    page = requests.get(url).text
    doc= BeautifulSoup(page, 'html.parser')

    page_text = doc.find(class_="type-company")#results-list
    items_found[page_text]
    for items in items_found:
        print(items)

def searchResults():
    pass


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    search()
