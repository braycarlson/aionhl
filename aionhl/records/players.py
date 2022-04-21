from aionhl.http import HTTP


class PlayerRecords(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get(self):
        self.endpoint = 'player'
        return self

    def get_by(self, team_id=None):
        self.endpoint = f'player/byTeam/{team_id}'
        return self
