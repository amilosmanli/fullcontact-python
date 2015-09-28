from fullcontact.api_resource import APIResource
from .error import InvalidParamsError, MissingParamsError


class Person(APIResource):
    _endpoint = 'person.json'
    _params = ['email', 'emailMD5', 'queue', 'callback', 'css', 'style',
               'prettyPrint', 'webhookUrl', 'webhookId', 'webhookBody']
    _web_hook_body = ['json', 'xml', 'html']

    @classmethod
    def find(cls, **options):
        if 'email' not in options:
            raise MissingParamsError('email')

        for option in options:
            if option not in cls._params:
                raise InvalidParamsError(option)

        wh_body = options.get('webhookBody')
        if wh_body and wh_body not in cls._web_hook_body:
            raise InvalidParamsError('webhookBody')

        pp = options.get('prettyPrint')
        if pp and type(pp) is not bool:
            raise InvalidParamsError('prettyPrint')

        return cls._get(cls._endpoint, **options)
