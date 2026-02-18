from bs4 import BeautifulSoup
import requests

url = 'https://www.ign.com/games/the-legend-of-zelda-a-link-to-the-past'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# rating = soup.find_all(
# a', class_='stack jsx-2509706801 analytic-with-text-box ign-rating')
rating = soup.find('span', class_='hexagon-content-wrapper').text
print(rating)
# print(soup.prettify())


"""

url = 'https://www.scrapethissite.com/pages/forms/'
# url = 'https://www.metacritic.com/game/elden-ring/'
# url = 'https://www.ign.com/games/the-legend-of-zelda-a-link-to-the-past/'
page = requests.get(url)  # returns a response object
print(page)

soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)
# print(soup.find('p', class_='lead').text.strip())

# Note, 'find' can use '.text' but 'find_all' can not.
# print(soup.find('h1', class_='text-5xl leading-normal tracking-tighter font-medium text-white'))
# print(soup.find_all('a'))
"""
