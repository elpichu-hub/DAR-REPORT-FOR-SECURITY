from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests

source = requests.get('http://icu-dar-report.herokuapp.com').text
soup = BeautifulSoup(source, 'html.parser')
print(soup.h4)



