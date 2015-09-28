class FullContactError(Exception):
    pass


class InvalidParamsError(FullContactError):
    def __init__(self, msg):
        message = 'Following parameter is invalid: %s' % msg
        super(InvalidParamsError, self).__init__(message)


class MissingParamsError(FullContactError):
    def __init__(self, msg):
        message = 'Following parameter is missing: %s' % msg
        super(MissingParamsError, self).__init__(message)
