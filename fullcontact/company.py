from fullcontact.api_resource import APIResource
from .error import InvalidParamsError, MissingParamsError


class Company(APIResource):
    _endpoint = 'company/lookup.json'
    _params = ['domain', 'prettyPrint', 'callback', 'webhookUrl', 'webhookId']

    @classmethod
    def find(cls, **options):
        if 'domain' not in options:
            raise MissingParamsError('domain')

        for option in options:
            if option not in cls._params:
                raise InvalidParamsError(option)

        pp = options.get('prettyPrint')
        if pp and type(pp) is not bool:
            raise InvalidParamsError('prettyPrint')

        return cls._get(cls._endpoint, **options)
