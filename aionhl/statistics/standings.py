from aionhl.http import HTTP


class Standings(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(self, season=None, date=None, record=False):
        self.endpoint = 'standings'
        self.parameters['queries'].update({
            'record': {
                'expand': 'standings.record' if record else False
            },
            'season': {
                'season': season
            },
            'date': {
                'date': date
            }
        })
        return self

    def get_wildcards(self, season=None, date=None, record=False):
        self.endpoint = 'standings/wildCardWithLeaders'
        self.parameters['queries'].update({
            'record': {
                'expand': 'standings.record' if record else False
            },
            'season': {
                'season': season if isinstance(season, list) else False
            },
            'date': {
                'date': date
            }
        })
        return self
