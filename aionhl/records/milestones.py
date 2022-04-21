from aionhl.http import HTTP


class MilestoneRecords(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get_one_thousand_point_career(self):
        self.endpoint = 'milestone-1000-point-career'
        return self

    def get_five_hundred_goal_career(self):
        self.endpoint = 'milestone-500-goal-career'
        return self

    def get_one_hundred_point_season(self):
        self.endpoint = 'milestone-100-point-season'
        return self

    def get_fifty_goal_season(self):
        self.endpoint = 'milestone-50-goal-season'
        return self

    def get_five_goal_game(self):
        self.endpoint = 'milestone-5-goal-game'
        return self
