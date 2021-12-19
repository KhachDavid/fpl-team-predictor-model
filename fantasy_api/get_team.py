import requests
from decouple import config

ENDPOINT_URL = "https://fantasy.premierleague.com/api"

session = requests.session()

def get_my_team():
    url = 'https://users.premierleague.com/accounts/login/'
    payload = {
     'password': config('PASSWORD'),
     'login': 'esdavitnem@gmail.com',
     'redirect_uri': 'https://fantasy.premierleague.com/a/login',
     'app': 'plfpl-web'
    }
    session.post(url, data=payload)

    response = session.get(f'{ENDPOINT_URL}/my-team/28967').json()

    return response['picks'], response['transfers'], response['chips']
