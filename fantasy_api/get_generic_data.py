import requests

ENDPOINT_URL = "https://fantasy.premierleague.com/api"

def get_generic_data():
    url = f'{ENDPOINT_URL}/bootstrap-static/'
    response = requests.get(url).json()
    return response['events'], response['teams'], response['total_players'], response['elements'], response['element_types']