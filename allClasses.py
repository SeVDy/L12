import requests
import pprint
import json


class Search:

    def __init__(self):
        self._session = requests.session()
        self._login = ''
        self._token = ''
        self._site_url = ''
        self._data = []
        self._items = ''
        self._q = ''
        self._language = ''
        self._user = ''
        self._data_with_filter = {}

    @property
    def get_login(self):
        return self._login

    @property
    def get_token(self):
        return self._token

    def auth_param(self, login: str, token: str):
        self._login = login
        self._token = token
        self._session.auth = (self._login, self._token)
        return self._session.auth

    def get_data(self, url_srch, type_srch, q, language):
        self._q = q
        self._language = language
        self._data = self._session.get(f'{url_srch}{type_srch}?q={self._q} ' +
                                       f'+in:file' +
                                       f'+language:{self._language}+user:DanteOnline') # &per_page=100

        self._items = self._data.json()['items']
        return self._data.status_code

    def print_data(self):
        pprint.pprint(self._data.json())

    def data_filter(self):
        for i in range(len(self._items)):
            y = self._items[i]['repository']['url']
            if y not in self._data_with_filter:
                self._data_with_filter.update({y: {'words': [f'{self._language}'], 'unsafe_modules': []}})
            # if self._language not in self._data_with_filter[y]['words'] and y in self._data_with_filter:
            #     self._data_with_filter[y]['words'].append(f'{self._language}')
            self._data_with_filter[y]['unsafe_modules'].append({'name': self._items[i]['name'],
                                                                'unsafe code type': f'В коде используется {self._q}',
                                                                'status': 'Потенциально опасен'})

    def print_data_with_filter(self):
        pprint.pprint(self._data_with_filter)

    def save_at_file(self, file_name):
        data_str = json.dumps(self._data_with_filter, indent=4, ensure_ascii=False)
        with open(file_name, "w") as f:
            f.write(data_str)

    @staticmethod
    def print_file(file_name):
        with open(file_name, "r") as f:
            x = f.read()
        capitals = json.loads(x)
        pprint.pprint(capitals)
