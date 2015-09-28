import requests

import fullcontact
from .error import FullContactError

__author__ = 'Amil Osmanli'


class APIResource(dict):
    _api_url = 'https://api.fullcontact.com/v2'
    options = {}

    @classmethod
    def set_version(cls, value):
        cls.options['headers'] = {'API-Version': value}

    @classmethod
    def new(cls, item, response=None):
        if isinstance(item, list):
            instances = (cls(rec) for rec in item)
            for instance in instances:
                instance['response'] = response

        else:
            instances = cls(item)
            instances['response'] = response

        return instances

    @classmethod
    def _get(cls, endpoint, **kwargs):

        if fullcontact.key:
            kwargs['apiKey'] = fullcontact.key
        else:
            raise FullContactError('No key provided')

        url = '%s/%s' % (cls._api_url, endpoint)
        response = requests.get(url, params=kwargs)
        instance = None

        if response.status_code == 200:
            instance = cls.new(response.json())
        if response.status_code == 202:
            instance = cls.new({'pending': True})
        elif response.status_code == requests.codes.not_found:
            instance = None
        else:
            response.raise_for_status()

        if instance:
            instance['response'] = response

        return instance

    def __getitem__(self, key):
        return dict.__getitem__(self, key)
