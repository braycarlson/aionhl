from aionhl.http import HTTP


class Prospects(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(self):
        self.endpoint = 'draft/prospects'
        return self

    def get_by(self, id=None):
        self.endpoint = f'draft/prospects/{id}'
        return self
