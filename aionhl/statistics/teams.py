from aionhl.http import HTTP


class Teams(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(
        self,
        team=None,
        roster=False,
        name=False,
        next=False,
        previous=False,
        statistics=False,
        playoff=False
    ):
        self.endpoint = 'teams'
        self.parameters['queries'].update({
            'team': {
                'teamId': team
            },
            'roster': {
                'expand': 'team.roster' if roster else False,
                'season': roster if isinstance(roster, list) else False
            },
            'name': {
                'expand': 'person.names' if name else False
            },
            'next': {
                'expand': 'team.schedule.next' if next else False
            },
            'previous': {
                'expand': 'team.schedule.previous' if previous else False
            },
            'statistics': {
                'expand': 'team.stats' if statistics else False
            },
            'playoff': {
                'stats': 'statsSingleSeasonPlayoffs' if playoff else False
            }
        })
        return self

    def get_by_id(self, team=None):
        self.endpoint = f'teams/{team}'
        return self

    def get_statistics(self, team=None):
        self.endpoint = f'teams/{team}/stats'
        return self

    def get_roster(self, team=None):
        self.endpoint = f'teams/{team}/roster'
        return self
