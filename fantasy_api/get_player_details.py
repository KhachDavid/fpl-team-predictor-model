import requests

import requests

ENDPOINT_URL = "https://fantasy.premierleague.com/api"

def get_player_details(id):

    url = f'{ENDPOINT_URL}/element-summary/{id}/'
    response = requests.get(url).json()
    return response['fixtures'], response['history'], response['history_past']