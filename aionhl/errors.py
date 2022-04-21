class NHLException(Exception):
    pass


class HTTPException(NHLException):
    def __init__(self, response):
        self.response = response
        super().__init__(self.response)


class Forbidden(HTTPException):
    pass


class NotFound(HTTPException):
    pass
