from aionhl.http import HTTP


class Tournaments(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(self, season=None, round=None):
        self.endpoint = 'tournaments/playoffs'
        self.parameters['queries'].update({
            'series': {
                'expand': 'round.series' if round else False,
            },
            'season': {
                'season': season if isinstance(season, list) else False
            }
        })
        return self
