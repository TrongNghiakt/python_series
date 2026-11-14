from bs4 import BeautifulSoup
import requests

# with open('D:\\python_learning\\BeautifulSoup\\simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# # print(soup.prettify())

# # match = soup.title.text

# # match = soup.div
# # article = soup.find('div', class_='article')
# for article in soup.find_all('div', class_='article'):

#     headline = article.h2.a.text
#     print(headline)

#     summary = article.p.text
#     print(summary)

# print()


source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

containers = soup.find('div', class_='container')

headline = containers.a.text

print(headline)
