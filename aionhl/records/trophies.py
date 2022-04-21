from aionhl.http import HTTP


class TrophyRecords(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get(self):
        self.endpoint = 'trophy'
        return self
