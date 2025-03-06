import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)
# print(soup.findAll('div'))
# print(soup.findAll('a'))
print(soup.title)