from aionhl.http import HTTP


class Schedules(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://statsapi.web.nhl.com/api/v1'

    def get(
        self,
        broadcast=None,
        linescore=None,
        ticket=None,
        team=None,
        date=None,
        start_date=None,
        end_date=None,
        season=None,
        gametype=None
    ):
        self.endpoint = 'schedule'
        self.parameters['queries'].update({
            'team': {
                'teamId': team
            },
            'date': {
                'date': date
            },
            'start_date': {
                'startDate': start_date
            },
            'end_date': {
                'endDate': end_date
            },
            'season': {
                'season': season
            },
            'gametype': {
                'gameType': gametype
            },
            'broadcast': {
                'expand': 'schedule.broadcasts' if broadcast else False
            },
            'linescore': {
                'expand': 'schedule.linescore' if linescore else False
            },
            'ticket': {
                'expand': 'schedule.ticket' if ticket else False
            }
        })
        return self
