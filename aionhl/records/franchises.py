from aionhl.http import HTTP


class FranchiseRecords(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get(self, franchise=None, team=None, season=None, order=None):
        self.endpoint = 'franchise'
        self.parameters['queries'].update({
            'franchise': {
                'franchiseId': franchise,
            },
            'team': {
                'mostRecentTeamId': team,
            },
            'season': {
                'seasonId': season,
            },
            'order': {
                'dir': order.upper()
            }
        })
        return self

    def get_details(self, franchise=None, team=None, season=None, order=None):
        self.endpoint = 'franchise-detail'
        self.parameters['queries'].update({
            'franchise': {
                'franchiseId': franchise,
            },
            'team': {
                'mostRecentTeamId': team,
            },
            'season': {
                'seasonId': season,
            },
            'order': {
                'dir': order.upper()
            }
        })
        return self

    def get_season_records(self, franchise=None, team=None, season=None, order=None):
        self.endpoint = 'franchise-season-records'
        self.parameters['queries'].update({
            'franchise': {
                'franchiseId': franchise,
            },
            'team': {
                'mostRecentTeamId': team,
            },
            'season': {
                'seasonId': season,
            },
            'order': {
                'dir': order.upper()
            }
        })
        return self

    def get_season_results(self, franchise=None, team=None, season=None, order=None):
        self.endpoint = 'franchise-season-results'
        self.parameters['queries'].update({
            'franchise': {
                'franchiseId': franchise,
            },
            'team': {
                'mostRecentTeamId': team,
            },
            'season': {
                'seasonId': season,
            },
            'order': {
                'dir': order.upper()
            }
        })
        return self

    def get_team_records(self, franchise=None, team=None, season=None, order=None):
        self.endpoint = 'franchise-team-totals'
        self.parameters['queries'].update({
            'franchise': {
                'franchiseId': franchise,
            },
            'team': {
                'mostRecentTeamId': team,
            },
            'season': {
                'seasonId': season,
            },
            'order': {
                'dir': order.upper()
            }
        })
        return self

    def get_goalie_records(self, franchise=None, team=None, season=None, order=None):
        self.endpoint = 'franchise-goalie-records'
        self.parameters['queries'].update({
            'franchise': {
                'franchiseId': franchise,
            },
            'team': {
                'mostRecentTeamId': team,
            },
            'season': {
                'seasonId': season,
            },
            'order': {
                'dir': order.upper()
            }
        })
        return self

    def get_skater_records(self, franchise=None, team=None, season=None, order=None):
        self.endpoint = 'franchise-skater-records'
        self.parameters['queries'].update({
            'franchise': {
                'franchiseId': franchise,
            },
            'team': {
                'mostRecentTeamId': team,
            },
            'season': {
                'seasonId': season,
            },
            'order': {
                'dir': order.upper()
            }
        })
        return self
