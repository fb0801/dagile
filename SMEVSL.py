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
    findings = requests.get(url).text
    doc= BeautifulSoup(findings, 'html.parser')

    #page_text = doc.find(class_="type-company")#results-list
    div = doc.find(class_="results-list type-company")
    companies = div.find_all(list=re.compile(search_term))
    
    for results in companies:
        
    #for com in companies:
        #res = doc.find_all('type-company', limit=5)
    #    print (com)

    #items_found[items]
    #for companies in items_found:
    #print(div)
    #for companies in page_text:
        #print(companies)

def searchResults():
    pass


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    search()
