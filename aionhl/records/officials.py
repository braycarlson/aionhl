from aionhl.http import HTTP


class OfficialRecords(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get(self, active=False):
        self.endpoint = 'officials'
        self.parameters['queries'].update({
            'active': {
                'active': 'true' if active else 'false'
            }
        })
        return self
