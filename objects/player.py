from .team import get_team_by_id

class Player:
    def __init__(self, *args, **kwargs):

        # Basic Data
        self.id = kwargs.get('id')
        self.first_name = kwargs.get('first_name')
        self.web_name = kwargs.get('web_name')
        self.team = kwargs.get('team')
        self.element_type = kwargs.get('element_type') # This is the position
        self.is_my_team = kwargs.get('is_my_team')

        # Player Data For The Coming Round
        self.chance_of_playing_this_round = kwargs.get('chance_of_playing_this_round')
        self.chance_of_playing_next_round = kwargs.get('chance_of_playing_next_round')
        self.form = kwargs.get('form')

        # Players Dynamic Data
        self.selected_by_percent = kwargs.get('selected_by_percent')
        self.transfers_in = kwargs.get('transfers_in')
        self.transfers_out = kwargs.get('transfers_out')
        self.transfers_in_event = kwargs.get('transfers_in_event')
        self.transfers_out_event = kwargs.get('transfers_out_event')
        self.news = kwargs.get('news')
        self.news_added = kwargs.get('news_added')

        # Season Data
        self.dreamteam_count = kwargs.get('dreamteam_count')
        self.total_points = kwargs.get('total_points')
        self.minutes = kwargs.get('minutes')

        # Prolific Data
        self.goals_scored = kwargs.get('goals_scored')
        self.assists = kwargs.get('assists')
        self.penalties_missed = kwargs.get('penalties_missed')

        # Defense Data
        self.saves = kwargs.get('saves')
        self.goals_conceded = kwargs.get('goals_conceded')
        self.clean_sheets = kwargs.get('clean_sheets')
        self.penalties_saved = kwargs.get('penalties_saved')
        self.own_goals = kwargs.get('own_goals')

        # Discipline Data
        self.yellow_cards = kwargs.get('yellow_cards')
        self.red_cards = kwargs.get('red_cards')


        # Season Numerical Data
        self.bonus = kwargs.get('bonus')
        self.bps = kwargs.get('bps')
        self.influence = kwargs.get('influence')
        self.creativity = kwargs.get('creativity')
        self.threat = kwargs.get('threat')
        self.ict_index = kwargs.get('ict_index')
        self.influence_rank = kwargs.get('influence_rank')
        self.influence_rank_type = kwargs.get('influence_rank_type')
        self.creativity_rank = kwargs.get('creativity_rank')
        self.creativity_rank_type = kwargs.get('creativity_rank_type')
        self.threat_rank = kwargs.get('threat_rank')
        self.threat_rank_type = kwargs.get('threat_rank_type')
        self.ict_index_rank = kwargs.get('ict_index_rank')
        self.ict_index_rank_type = kwargs.get('ict_index_rank_type')

        # Points
        self.event_points = kwargs.get('event_points')

        # Price Data
        self.now_cost = kwargs.get('now_cost')
        self.cost_change_event = kwargs.get('cost_change_event')
        self.cost_change_start = kwargs.get('cost_change_start')
        self.cost_change_event_fall = kwargs.get('cost_change_event_fall')
        self.cost_change_start_fall = kwargs.get('cost_change_start_fall')

        # Set Piece Data
        self.corners_and_indirect_freekicks_order = kwargs.get('corners_and_indirect_freekicks_order')
        self.direct_freekicks_order = kwargs.get('direct_freekicks_order')
        self.penalties_order = kwargs.get('penalties_order')

    
    def get_position(self):
        if self.element_type == 1:
            return 'Goalkeeper'
        elif self.element_type == 2:
            return 'Defender'
        elif self.element_type == 3:
            return 'Midfielder'
        elif self.element_type == 4:
            return 'Forward'
        else:
            return 'Unknown'

    def get_basic_data(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'web_name': self.web_name,
            'team': self.get_team(),
            'element_type': self.get_position(),
            'is_my_team': self.is_my_team
        }

    def get_player_data_for_the_coming_round(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'chance_of_playing_this_round': self.chance_of_playing_this_round,
            'chance_of_playing_next_round': self.chance_of_playing_next_round,
            'form': self.form
        }

    def get_players_dynamic_data(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'selected_by_percent': self.selected_by_percent,
            'transfers_in': self.transfers_in,
            'transfers_out': self.transfers_out,
            'transfers_in_event': self.transfers_in_event,
            'transfers_out_event': self.transfers_out_event,
            'news': self.news,
            'news_added': self.news_added
        }
    
    def get_season_data(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'dreamteam_count': self.dreamteam_count,
            'total_points': self.total_points,
            'minutes': self.minutes
        }

    def get_prolific_data(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'goals_scored': self.goals_scored,
            'assists': self.assists,
            'penalties_missed': self.penalties_missed
        }

    def get_defense_data(self):
        return {

            'first_name': self.first_name,
            'web_name': self.web_name,

            'saves': self.saves,
            'goals_conceded': self.goals_conceded,
            'clean_sheets': self.clean_sheets,
            'penalties_saved': self.penalties_saved,
            'own_goals': self.own_goals
        }

    def get_discipline_data(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'yellow_cards': self.yellow_cards,
            'red_cards': self.red_cards
        }

    def get_season_numerical_data(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'bonus': self.bonus,
            'bps': self.bps,
            'influence': self.influence,
            'creativity': self.creativity,
            'threat': self.threat,
            'ict_index': self.ict_index,
            'influence_rank': self.influence_rank,
            'influence_rank_type': self.influence_rank_type,
            'creativity_rank': self.creativity_rank,
            'creativity_rank_type': self.creativity_rank_type,
            'threat_rank': self.threat_rank,
            'threat_rank_type': self.threat_rank_type,
            'ict_index_rank': self.ict_index_rank,
            'ict_index_rank_type': self.ict_index_rank_type
        }

    def get_points_data(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'event_points': self.event_points
        }

    def get_price_data(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'now_cost': self.now_cost,
            'cost_change_event': self.cost_change_event,
            'cost_change_start': self.cost_change_start,
            'cost_change_event_fall': self.cost_change_event_fall,
            'cost_change_start_fall': self.cost_change_start_fall
        }

    def get_set_piece_data(self):
        return {
            'first_name': self.first_name,
            'web_name': self.web_name,

            'corners_and_indirect_freekicks_order': self.corners_and_indirect_freekicks_order,
            'direct_freekicks_order': self.direct_freekicks_order,
            'penalties_order': self.penalties_order,
        }

    def get_team(self):
        return get_team_by_id(self.team)

    def get_player_by_id(self, id):
        return self

    def __str__(self) -> str:
        return f"{self.first_name} {self.web_name}"

    def __repr__(self) -> str:
        return f"{self.first_name} {self.web_name}"

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return self.id
