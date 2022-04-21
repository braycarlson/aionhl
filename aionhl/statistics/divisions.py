from aionhl.http import HTTP


class Divisions(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(self):
        self.endpoint = 'divisions'
        return self

    def get_by(self, id=None):
        self.endpoint = f'divisions/{id}'
        return self
