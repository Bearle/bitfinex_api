class InvalidApiKey(Exception):
    message = 'Could not find a key matching the given X-BFX-APIKEY.'

class UnknownError(Exception):
    pass
