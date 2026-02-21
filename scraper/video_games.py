from bs4 import BeautifulSoup
from website_interation_functions import get_response
import re

IGN_START_URL = 'https://www.ign.com/games/'
METACRITIC_START_URL = 'https://www.metacritic.com/game/'
GAME_SITES_SUPPORTED = ['ign', 'metacritic']


class VideoGame:

    def __init__(self, name):
        self.name = name
        self._ign_rating = 'Does not exist'
        self.ign_url = ''
        self._metacritic_rating = 'Does not exist'
        self.metacritic_url = ''
        self._set_urls()
        self._set_ratings()

    @property
    def ign_rating(self):
        return self._ign_rating

    @property
    def metacritic_rating(self):
        return self._metacritic_rating

    def _set_ratings(self):
        # IGN portion
        response = get_response(self.ign_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            self._ign_rating = soup.find(
                'span', class_='hexagon-content-wrapper').text
        # Metacritic portion
        response = get_response(self.metacritic_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            self._metacritic_rating = soup.find(
                'div', class_='c-siteReviewScore u-flexbox-column u-flexbox-alignCenter u-flexbox-justifyCenter g-text-bold c-siteReviewScore_green g-color-gray90 c-siteReviewScore_medium').text

    def _set_urls(self):
        ending_url = ''
        if not self.name:
            print("Error: No video game name was provided")
            return ending_url
        video_game_name_as_list = self.name.lower().split(' ')
        for word in video_game_name_as_list:
            edited_word = re.sub(r'[^a-zA-Z0-9]', '', word)
            ending_url += edited_word + "-"
        ending_url = ending_url[:-1]
        self.ign_url = IGN_START_URL + ending_url
        self.metacritic_url = METACRITIC_START_URL + ending_url

    def as_dict(self):
        return {'Video Game Name': self.name, 'IGN Rating': self._ign_rating, 'Metacritic Rating': self._metacritic_rating, 'IGN URL': self.ign_url, 'Metacritic URL': self.metacritic_url}
