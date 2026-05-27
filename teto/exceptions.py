class TetoException(Exception):
    pass


class TetoAPIError(TetoException):
    pass


class TetoRateLimitError(TetoException):
    pass
