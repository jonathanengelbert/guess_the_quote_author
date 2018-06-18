#Scrapping script to acquire all quotes from http://quotes.toscrape.com/

import requests
from random import randint
from bs4 import BeautifulSoup


#checks if the 'next' button exists in the page. Used to find where to stop the loop
def get_page():
    """Loops through website and stores number of pages available.
       It then randomly select a page to return. Example: http://quotes.toscrape.com/page/(number)
    """
    base_url = 'http://quotes.toscrape.com/page/'
    counter = 1

    while True:
        try:
            url = base_url + str(counter)
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(response.text, 'html.parser')
            pages = soup.select('.next')
            next_available = (pages[0]('a')[0].get_text())

            counter += 1

        except IndexError:
            page = base_url + str(randint(1, counter))
            return page


def get_quote():
    """Retrives a quote from randomly select page"""

    page = get_page()
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select('.quote')

    quote_counter = 0
    for quote in quotes:
        quote_counter += 1

    quote_number = randint(1, quote_counter)

    #DATA
    quote = quotes[quote_number].find('span').get_text()
    author = quotes[quote_number].find('small').get_text()
    author_link = quotes[quote_number].find('a')['href']

    return quote, author, author_link












