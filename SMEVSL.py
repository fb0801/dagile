'''Gather company data more quickly
part of https://github.com/fb0801/dagile created by Farhan Bhatti

GNU General Public License v2.0
'''

#modules for application use
import re
from bs4 import BeautifulSoup
import requests
import json
import os

items_found = {
    "Company Name":"",
    "Company Status":"",
    "Company details":""
}

def search():
    search_term = input('Enter the company name: ') # input from user

    #link we want to use
    url = f"https://find-and-update.company-information.service.gov.uk/search?q={search_term}"
    findings = requests.get(url).text
    doc= BeautifulSoup(findings, 'html.parser')

    #page_text = doc.find(class_="type-company")#results-list
    soup = doc.find(class_="results-list")
    #companies = div.find_all(text=re.compile(search_term))
    companies = soup.find_all(class_="type-company")

    article = doc.article
    trs = article.contents
    

    for results in companies:
        
        fixed_name = companies.a.string
        comp_status =  companies.p.string
        comp_descrip = companies.p.string    
    
       
    print(fixed_name, comp_status,comp_descrip)
    #for results in companies:
    #    title = soup.find_all(class_="type-company")
        
    
        #res = doc.find_all('type-company', limit=5)
    #    print (com)

     
   
def searchResults():
    pass


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    search()
