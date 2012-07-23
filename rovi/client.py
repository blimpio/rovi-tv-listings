from .exceptions import RoviMissingApiKeyException


class RoviClient(object):

    def __init__(self, *args, **kwargs):
        self.api_key = kwargs.get('api_key')
        self.use_https = kwargs.get('use_https', False)
        self.format = kwargs.get('format', 'json')
        self.locale = kwargs.get('locale', 'en-US')

        if self.api_key is None or self.api_key == 'CHANGE-ME':
            raise RoviMissingApiKeyException('Get api key from: http://developer.rovicorp.com/page/Get_Started')

        if self.use_https:
            self.protocol = 'https://'
        else:
            self.protocol = 'http://'
