from aionhl.http import HTTP


class DraftRecords(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get(self, team=None, year=None):
        self.endpoint = 'draft'
        self.parameters['queries'].update({
            'team': {
                'draftedByTeamId': team
            },
            'year': {
                'draftYear': year,
            }
        })
        self.build = True
        return self
