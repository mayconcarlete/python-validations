class MissingParamError(Exception):
    def __init__(self, paramName):
        self.paramName = paramName
    def __str__(self):
        return 'Missing param error: ' + self.paramName
