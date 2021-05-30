from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests


username = 'lazaro'
password = 'yemaya07'
scrape_url = 'http://icu-dar-report.herokuapp.com'

login_url = 'http://icu-dar-report.herokuapp.com/login'
login_info = {'username': username,'password': password}

session = requests.session()

session.post(url=login_url, data=login_info)



url = session.get(url=scrape_url)

soup = BeautifulSoup(url.content, 'html.parser')
print(soup)



