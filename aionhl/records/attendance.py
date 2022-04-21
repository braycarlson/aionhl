from aionhl.http import HTTP


class AttendanceRecords(HTTP):
    def __init__(self, loop=None, session=None):
        super().__init__(loop, session)
        self.base = 'https://records.nhl.com/site/api'
        self.records = True

    def get(self):
        self.endpoint = 'attendance'
        return self
