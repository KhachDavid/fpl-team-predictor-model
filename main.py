from fantasy_api.get_team import get_my_team
from fantasy_api.get_player_details import get_player_details
from fantasy_api.get_generic_data import get_generic_data
from objects.player import Player


def get_players_fantasy_data(my_team, data):
    my_picks = [pick['element'] for pick in my_team['picks']]

    new_players = []
    for this_player in data['players']:
        if this_player['id'] in my_picks:
            new_players.append(format_player(this_player, is_my_team=True, print_player=False))
        else:
            new_players.append(format_player(this_player, is_my_team=False, print_player=False))

    return new_players

def format_player(player, is_my_team=False, print_player=True):
    if print_player:
        print("Name: " + player['web_name'])
        print("id: " + str(player['id']))
        print("Chances of playing this round: " + str(player['chance_of_playing_this_round']))
        print("Chances Of Playing Next Round: " + str(player['chance_of_playing_next_round']))
        print("Owned by team: " + str(player['selected_by_percent']))
        print("Transfers in Next Round: " + str(player['transfers_in_event']))
        print("Transfers Out Next Round: " + str(player['transfers_out_event']))
        print("Transfer In Total: " + str(player['transfers_in']))
        print("Transfers Out Total: " + str(player['transfers_out']))
        print("Form: " + str(player['form']))
        print("News: " + str(player['news']))
        print("News added: " + str(player['news_added']))
        print("Team: " + str(player['team']))
        print("Now-cost: " + str(player['now_cost']))
        print("Cost change event: " + str(player['cost_change_event']))
        print("Cost change event fall: " + str(player['cost_change_event_fall']))
        print("Cost change start: " + str(player['cost_change_start']))
        print("Cost change start fall: " + str(player['cost_change_start_fall']))
        print("Dreamteam count: " + str(player['dreamteam_count']))
        print("Event-points: " + str(player['event_points']))
        print("Total-points: " + str(player['total_points']))
        print("Minutes: " + str(player['minutes']))
        print("Goals scored: " + str(player['goals_scored']))
        print("Assists: " + str(player['assists']))
        print("Clean Sheets: " + str(player['clean_sheets']))
        print("Goals Conceded: " + str(player['goals_conceded']))
        print("Own goals: " + str(player['own_goals']))
        print("Penalties saved: " + str(player['penalties_saved']))
        print("Penalties missed: " + str(player['penalties_missed']))
        print("Yellow cards: " + str(player['yellow_cards']))
        print("Red cards: " + str(player['red_cards']))
        print("Saves: " + str(player['saves']))
        print("Bonus: " + str(player['bonus']))
        print("BPS: " + str(player['bps']))
        print("Influence: " + str(player['influence']))
        print("Creativity: " + str(player['creativity']))
        print("Threat: " + str(player['threat']))
        print("Ict Index: " + str(player['ict_index']))
        print("Influence Rank: " + str(player['influence_rank']))
        print("Influence Rank Type: " + str(player['influence_rank_type']))
        print("Creativity Rank: " + str(player['creativity_rank']))
        print("Creativity Rank Type: " + str(player['creativity_rank_type']))
        print("Threat Rank: " + str(player['threat_rank']))
        print("Threat Rank Type: " + str(player['threat_rank_type']))
        print("Ict Index Rank: " + str(player['ict_index_rank']))
        print("Ict Index Rank Type: " + str(player['ict_index_rank_type']))
        print("Corners and indirect freekicks order: "+str(player['corners_and_indirect_freekicks_order']))
        print("Corners and indirect freekicks text: "+str(player['corners_and_indirect_freekicks_text']))
        print("Direct Freekicks Order: "+str(player['direct_freekicks_order']))
        print("Direct Freekicks Text: "+str(player['direct_freekicks_text']))
        print("Penalties Order: "+str(player['penalties_order']))
        print("Penalties Text: "+str(player['penalties_text']))

    player = Player(
        id=player['id'],
        first_name=player['first_name'],
        web_name=player['web_name'],
        chance_of_playing_this_round=player['chance_of_playing_this_round'],
        chance_of_playing_next_round=player['chance_of_playing_next_round'],
        owned_by_team=player['selected_by_percent'],
        transfers_in_event=player['transfers_in_event'],
        transfers_out_event=player['transfers_out_event'],
        transfers_in=player['transfers_in'],
        transfers_out=player['transfers_out'],
        form=player['form'],
        news=player['news'],
        news_added=player['news_added'],
        team=player['team'],
        now_cost=player['now_cost'],
        cost_change_event=player['cost_change_event'],
        cost_change_event_fall=player['cost_change_event_fall'],
        cost_change_start=player['cost_change_start'],
        cost_change_start_fall=player['cost_change_start_fall'],
        dreamteam_count=player['dreamteam_count'],
        event_points=player['event_points'],
        total_points=player['total_points'],
        minutes=player['minutes'],
        goals_scored=player['goals_scored'],
        assists=player['assists'],
        clean_sheets=player['clean_sheets'],
        goals_conceded=player['goals_conceded'],
        own_goals=player['own_goals'],
        penalties_saved=player['penalties_saved'],
        penalties_missed=player['penalties_missed'],
        yellow_cards=player['yellow_cards'],
        red_cards=player['red_cards'],
        saves=player['saves'],
        bonus=player['bonus'],
        bps=player['bps'],
        influence=player['influence'],
        creativity=player['creativity'],
        threat=player['threat'],
        ict_index=player['ict_index'],
        influence_rank=player['influence_rank'],
        influence_rank_type=player['influence_rank_type'],
        creativity_rank=player['creativity_rank'],
        creativity_rank_type=player['creativity_rank_type'],
        threat_rank=player['threat_rank'],
        threat_rank_type=player['threat_rank_type'],
        ict_index_rank=player['ict_index_rank'],
        ict_index_rank_type=player['ict_index_rank_type'],
        corners_and_indirect_freekicks_order=player['corners_and_indirect_freekicks_order'],
        corners_and_indirect_freekicks_text=player['corners_and_indirect_freekicks_text'],
        direct_freekicks_order=player['direct_freekicks_order'],
        direct_freekicks_text=player['direct_freekicks_text'],
        penalties_order=player['penalties_order'],
        penalties_text=player['penalties_text'],
        element_type=player['element_type'],
        selected_by_percent=player['selected_by_percent'],
        is_my_team=is_my_team
    )

    return player

def setup():
    picks, transfer, chips = (get_my_team())
    my_team = {
        'picks': picks,
        'transfer': transfer,
        'chips': chips
    }

    events, teams, total_players, elements, element_types = (get_generic_data())
    data = {
        'events': events,
        'teams': teams,
        'total_players': total_players,
        'players': elements,
        'element_types': element_types
    }

    return my_team, data
