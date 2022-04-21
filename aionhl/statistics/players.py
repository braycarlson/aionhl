from aionhl.http import HTTP


class Players(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(self, player=None):
        self.endpoint = f'people/{player}'
        return self

    def get_statistics(
        self,
        player=None,
        playoff=False,
        year=False,
        homeandaway=False,
        win_loss=False,
        month=False,
        dayofweek=False,
        division=False,
        conference=False,
        team=False,
        gamelog=False,
        ranking=False,
        goals=False,
        onpace=False,
    ):
        self.endpoint = f'people/{player}/stats'
        self.parameters['queries'].update({
            'playoff': {
                'stats': 'statsSingleSeasonPlayoffs' if playoff else False,
                'season': playoff if isinstance(playoff, list) else False
            },
            'year': {
                'stats': 'yearByYear' if year else False
            },
            'month': {
                'stats': 'byMonth' if month else False,
                'season': month if isinstance(month, list) else False
            },
            'dayofweek': {
                'stats': 'byDayOfWeek' if dayofweek else False,
                'season': dayofweek if isinstance(dayofweek, list) else False
            },
            'homeandaway': {
                'stats': 'homeAndAway' if homeandaway else False,
                'season': homeandaway if isinstance(homeandaway, list) else False
            },
            'win_loss': {
                'stats': 'winLoss' if win_loss else False,
                'season': win_loss if isinstance(win_loss, list) else False
            },
            'division': {
                'stats': 'vsDivision' if division else False,
                'season': division if isinstance(division, list) else False
            },
            'conference': {
                'stats': 'vsConference' if conference else False,
                'season': conference if isinstance(conference, list) else False
            },
            'team': {
                'stats': 'vsTeam' if team else False,
                'season': team if isinstance(team, list) else False
            },
            'gamelog': {
                'stats': 'gameLog' if gamelog else False,
                'season': gamelog if isinstance(gamelog, list) else False
            },
            'ranking': {
                'stats': 'regularSeasonStatRankings' if ranking else False,
                'season': ranking if isinstance(ranking, list) else False
            },
            'goals': {
                'stats': 'goalsByGameSituation' if goals else False,
                'season': goals if isinstance(goals, list) else False
            },
            'onpace': {
                'stats': 'onPaceRegularSeason' if onpace else False,
                'season': onpace if isinstance(onpace, list) else False
            },
        })
        return self
