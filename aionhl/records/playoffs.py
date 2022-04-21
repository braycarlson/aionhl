from aionhl.http import HTTP


class PlayoffRecords(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get(self, series=None, season=None):
        self.endpoint = 'playoff-series'
        self.parameters['queries'].update({
            'series': {
                'seriesTitle': series,
            },
            'season': {
                'seasonId': season if isinstance(season, list) else False
            }
        })
        self.build = True
        return self
