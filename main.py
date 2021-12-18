from fantasy_api.get_team import get_my_team
from fantasy_api.get_player_details import get_player_details

picks, transfer, chips = (get_my_team())

for pick, val in enumerate(picks):
    print(get_player_details(pick))

