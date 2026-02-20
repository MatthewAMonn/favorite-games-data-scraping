from bs4 import BeautifulSoup
import requests
import re

IGN_START_URL = 'https://www.ign.com/games/'
METACRITIC_START_URL = 'https://www.metacritic.com/game/'
GAME_SITES_SUPPORTED = ['ign', 'metacritic']


def get_response(video_game_url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(video_game_url, headers=headers)
    return response


def get_video_game_rating(video_game_name: str, website_name: str):
    """
    Grabs the gaming site's review rating for the video game requested. Returns "NotFound" if a rating couldn't be found.

    Args:
        video_game_name (str): Video game being checked for a review rating
        website_name (str): Website name being used to check their review rating for a video game

    Returns:
        str: Rating the gaming site have for the video game or a 
    """
    video_game_url = get_url_for_video_game(video_game_name, website_name)
    response = get_response(video_game_url)
    if response.status_code == 200 and website_name.lower() == 'ign':
        soup = BeautifulSoup(response.text, 'html.parser')
        rating = soup.find('span', class_='hexagon-content-wrapper').text
        return str(rating)
    elif response.status_code == 200 and website_name.lower() == 'metacritic':
        soup = BeautifulSoup(response.text, 'html.parser')
        rating = soup.find(
            'div', class_='c-siteReviewScore u-flexbox-column u-flexbox-alignCenter u-flexbox-justifyCenter g-text-bold c-siteReviewScore_green g-color-gray90 c-siteReviewScore_medium').text
        return rating
    elif response.status_code == 404:
        print('Error: 404 Invalid URL. Returning "NotFound" as the rating')
        return 'NotFound'
    else:
        print(
            f'Reponse code was {response.status_code}. Could not obtain rating from website {website_name}. Returning "NotFound" as the rating')
        return '0'


# def get_video_game_rating_with_url(video_game_name: str, video_game_url: str):
    # return 5


def get_url_for_video_game(video_game_name: str, website_name: str):
    """
    Provides the website url for a video game based on the name of the video game and the gaming site requested

    Args:
        video_game_name (str): Name of the video game being checked for an IGN url
        website_name (str): Name of the gaming website

    Returns:
        str: Url for the video game
    """

    if website_name.lower() not in GAME_SITES_SUPPORTED:
        print(
            f'Error: Invalid game website "{website_name}" used. Only IGN and Metacritic are supported at this time.')
        return 'NoUrlReturned'
    ending_url = ''
    video_game_name_as_list = video_game_name.lower().split(' ')
    for word in video_game_name_as_list:
        edited_word = re.sub(r'[^a-zA-Z0-9]', '', word)
        ending_url += edited_word + "-"
    ending_url = ending_url[:-1]
    if website_name.lower() == 'ign':
        full_url = IGN_START_URL + ending_url
    elif website_name.lower() == 'metacritic':
        full_url = METACRITIC_START_URL + ending_url
    return full_url


# print(get_url_for_video_game('Warcraft III: The Frozen Throne', 'asd'))
# print(get_url_for_video_game('Warcraft III: The Frozen Throne', 'IGN'))
# print(get_url_for_video_game('Warcraft III: The Frozen Throne', 'Metacritic'))
# print(get_url_for_video_game('Warcraft III: The Frozen Throne', 'IGN'))
# print(get_video_game_rating('REANIMAL', 'Metacritic'))
# print(
# f'Ign rating for Warcraft III: The Frozen Throne is a {get_video_game_rating('Warcraft III: The Frozen Throne', 'IGN')}')
