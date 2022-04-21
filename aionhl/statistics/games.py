from aionhl.http import HTTP


class Games(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get_feed(self, game=None):
        self.endpoint = f'game/{game}/feed/live'
        return self

    def get_boxscore(self, game=None):
        self.endpoint = f'game/{game}/boxscore'
        return self

    def get_linescore(self, game=None):
        self.endpoint = f'game/{game}/linescore'
        return self

    def get_content(self, game=None):
        self.endpoint = f'game/{game}/content'
        return self

    def get_feed_by_timecode(self, game=None, time=None):
        self.endpoint = f'game/{game}/feed/live/diffPatch'
        self.parameters['queries'].update({
            'time': {
                'startTimecode': time
            }
        })
        return self
