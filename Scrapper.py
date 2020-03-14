
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36

import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
    "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
# you can get user agent from https://www.whatismybrowser.com/detect/what-is-my-user-agent
URL = 'https://www.amazon.de/dp/B07XVWXW1Q/ref=sr_1_10?keywords=laptop&qid=1581888312&sr=8-10'
def amazon_de():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle")
    price = soup.find(id="priceblock_ourprice")
    titleText = title.getText()
    #priceText = price.getText()
    sep = ','
    #con_price = priceText.split(sep, 1)[0]
    #converted_price = int(con_price.replace('.', ''))

    # price
    print(titleText.strip())
    #print(converted_price)


amazon_de()