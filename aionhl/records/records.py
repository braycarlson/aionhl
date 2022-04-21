from aionhl.http import HTTP


class Records(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get_detail(self, franchise=None, gametype=None):
        self.endpoint = 'record-detail'
        self.parameters['queries'].update({
            'franchise': {
                'teamFranchiseId': franchise
            },
            'gametype': {
                'gameTypeId': gametype
            },
        })
        return self

    def get_all_time(self, franchise=None, gametype=None):
        self.endpoint = 'all-time-record-vs-franchise'
        self.parameters['queries'].update({
            'franchise': {
                'teamFranchiseId': franchise
            },
            'gametype': {
                'gameTypeId': gametype
            },
        })
        return self

    def get_playoff(self, franchise=None, gametype=None):
        self.endpoint = 'playoff-franchise-vs-franchise'
        self.parameters['queries'].update({
            'franchise': {
                'teamFranchiseId': franchise
            },
            'gametype': {
                'gameTypeId': gametype
            },
        })
        return self
