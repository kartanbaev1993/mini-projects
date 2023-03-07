import requests
from bs4 import BeautifulSoup
source = requests.get('http://www.example.com/').text
my_page = BeautifulSoup(source, 'lxml')

print(my_page.h1.text)
print(my_page.p.text)
print(my_page.a.get('href').text)