'''Gather company data more quickly'''

#modules for application use
import re
from bs4 import BeautifulSoup
import requests
import json
import os

def search():
    search_term = input('what would you like to search  for? ') # input from user

    #link we want to use
    url = f"https://find-and-update.company-information.service.gov.uk/search?q={search_term}"





if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    search()