from bs4 import BeautifulSoup
import requests
import re

IGN_START_URL = 'https://www.ign.com/games/'
METACRITIC_START_URL = 'https://www.metacritic.com/game/'


def get_ign_rating(video_game_name: str):
    ign_url = get_ign_url_for_video_game(video_game_name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(ign_url, headers=headers)
    if response.status_code == 404:
        print("Error: 404. Invalid URL")
        return 0
    soup = BeautifulSoup(response.text, 'html.parser')
    rating = soup.find('span', class_='hexagon-content-wrapper').text
    return rating


def get_ign_url_for_video_game(video_game_name: str):
    """
    Provides the IGN url for a video game based on the name of said video game

    Args:
        video_game_name (str): Name of the video game being checked for an IGN url

    Returns:
        str: IGN url for the video game
    """
    # Ign has their urls for video games have each word separated by a hyphen, removes special characters like semicolons.
    # For example, 'Warcraft III: The Frozen Throne' would be 'warcraft-iii-the-frozen-throne'
    ending_url = ''
    video_game_name_as_list = video_game_name.lower().split(' ')
    for word in video_game_name_as_list:
        edited_word = re.sub(r'[^a-zA-Z0-9]', '', word)
        ending_url += edited_word + '-'
    ign_ending_url = ending_url[:-1]
    full_url = IGN_START_URL + ign_ending_url
    return full_url


print(get_ign_url_for_video_game('Warcraft III: The Frozen Throne'))
print(
    f"Ign rating for Warcraft III: The Frozen Throne is a {get_ign_rating("Warcraft III: The Frozen Throne")}")
