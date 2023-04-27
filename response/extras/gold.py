import requests
from bs4 import BeautifulSoup



def GOLD():
    url = 'https://www.goodreturns.in/gold-rates/'

    html_text = requests.get(url).text

    main = BeautifulSoup(html_text,'lxml')

    table = main.find('strong',id='el').text.strip().strip('\n')
    return table


def population():
    url = 'https://www.worldometers.info/world-population/'

    html_text = requests.get(url).text
    html_text = requests.get(url).text

    main = BeautifulSoup(html_text,'lxml')

    data = main.find('div',class_='maincounter-number').text.strip()
    return data


def BTC():
    url = 'https://www.google.com/finance/quote/BTC-inr'

    html_text = requests.get(url).text

    main = BeautifulSoup(html_text,'lxml')

    data = main.find('div',class_='ln0Gqe').text.strip()
    return data


def GBP():
    url = 'https://www.google.com/finance/quote/GBP-INR'

    html_text = requests.get(url).text

    main = BeautifulSoup(html_text,'lxml')

    data = main.find('div',class_='YMlKec fxKbKc').text.strip()
    return data

def EUR():
    url = 'https://www.google.com/finance/quote/EUR-INR'

    html_text = requests.get(url).text

    main = BeautifulSoup(html_text,'lxml')

    data = main.find('div',class_='ln0Gqe').text.strip()
    return data


def USD():
    url = 'https://www.google.com/finance/quote/USD-INR'

    html_text = requests.get(url).text

    main = BeautifulSoup(html_text,'lxml')

    data = main.find('div',class_='ln0Gqe').text.strip()
    return data

def AUD():
    url = 'https://www.google.com/finance/quote/AUD-INR'

    html_text = requests.get(url).text

    main = BeautifulSoup(html_text,'lxml')

    data = main.find('div',class_='ln0Gqe').text.strip()
    return data



