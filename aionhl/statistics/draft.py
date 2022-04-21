from aionhl.http import HTTP


class Drafts(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(self):
        self.endpoint = 'draft'
        return self

    def get_by(self, start=None, end=None):
        self.endpoint = f'draft/{start}{end}'
        return self
