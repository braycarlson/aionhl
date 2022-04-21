from aionhl.http import HTTP


class Seasons(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(self):
        self.endpoint = 'seasons'
        return self

    def get_current(self):
        self.endpoint = 'seasons/current'
        return self

    def get_by(self, start=None, end=None):
        self.endpoint = f'seasons/{start}{end}'
        return self
