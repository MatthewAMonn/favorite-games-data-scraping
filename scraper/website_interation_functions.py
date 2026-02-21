import requests


def get_response(video_game_url: str):
    """
    Simple function to return the response from a given URL

    Args:
        video_game_url (str): URL being tested for a reponse

    Returns:
        Response: The 'response' the website gave from the URL requested
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(video_game_url, headers=headers)
    return response
