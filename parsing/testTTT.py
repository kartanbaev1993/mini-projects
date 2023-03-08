from bs4 import BeautifulSoup
import requests
import json


hakaton_url = 'https://www.enter.kg/computers'
response = requests.get(hakaton_url, verify=False)
# print(response)

soup = BeautifulSoup(response.text, 'lxml')