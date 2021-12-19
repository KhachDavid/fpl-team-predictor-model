import requests

ENDPOINT_URL = "https://fantasy.premierleague.com/api/fixtures"


def get_fixtures():
    url = f'{ENDPOINT_URL}/'
    response = requests.get(url).json()
    return response


def get_fixtures_for_specific_week(week):
    url = f'{ENDPOINT_URL}/?event={week}'
    response = requests.get(url).json()
    return response


def get_future_fixtures():
    url = 'https://fantasy.premierleague.com/api/fixtures/?future=1'
    response = requests.get(url).json()
    return response


def get_past_fixtures():
    url = 'https://fantasy.premierleague.com/api/fixtures/?future=0'
    response = requests.get(url).json()
    return response