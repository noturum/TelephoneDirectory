import os
from json import dump, load, JSONDecodeError

from typing import TypedDict


class Info(TypedDict, total=False):
    first_name: str
    mid_name: str
    last_name: str
    company: str
    phone_number: str
    additional_number: str


class TelephoneDirectory:
    """

    """

    def __init__(self, path: str):
        """
            В конструктор подается путь
        :param path: путь до файла
        """

        self._path: str = path
        self.cur_page: int = 1
        self.count_item: int = 5
        self._directory: None | list[Info] = []
        try:
            self._directory = [Info({k: v for k, v in zip(row.keys(), row.values())}) for row in
                               load(open(path, 'r'))]
        except JSONDecodeError:

            print('empty file')

    def __repr__(self):
        self.draw()
        return '\n'

    @property
    def directory(self) -> list[Info]:
        '''
        гетер справочника
        :return:
        '''
        return self._directory

    @directory.setter
    def directory(self, dir):
        """
        сеттер для бампа в файл и изменене локального файла
        :param dir: значение через =
        :return:
        """
        self._directory.append(dir)
        dump(self._directory, open(self._path, 'w'))

    def draw(self):
        """
        отрисовка справочника по страницам
        """
        for ind, row in enumerate(self.directory):
            print(f'{ind}. {row}')
            if not ind % self.count_item and ind > 0:
                print(f'\npage {self.cur_page}')
                self.cur_page += 1
        print(f'\npage {self.cur_page}')

    def append(self, dir: Info):
        """

        :param dir:
        :return:
        """
        self.directory = dir

    def find(self):
        """
        поиск перебирает по очереди поля ласа Info, после происходит поиск по полям справочника
        :return:
        """
        query = {}
        resp = []
        for field in info_keys:
            value = input(f'Enter {field}')
            if value:
                query[field] = value

        for ind, field in enumerate(directory.directory):
            if len([True for k, v in field.items() if k in query.keys() and v == query[k]]) == len(query):
                resp.append(f'{ind}. {field}')
        os.system('cls')
        if resp:
            print(resp)
        else:
            print('Not found \n\n\n')

    def edit(self):
        phone_id = int(input('Enter id'))
        info = directory.directory[phone_id]

        for ind, field in enumerate(keys := list(info_keys)):
            print(f'{ind}. {field}')
        ind_field = int(input('select item'))
        info[keys[ind_field]] = input('enter value')


if __name__ == '__main__':
    ans = None
    directory = TelephoneDirectory('../t.json')
    info_keys = Info.__optional_keys__
    while ans != '4':
        print(directory)
        print('1.Add\n' \
              '2.Edit\n' \
              '3.Find\n' \
              '4.Exit\n')
        ans = input('Choose:')
        match ans:
            case '1':
                info = Info()
                for field in info_keys:
                    info[field] = input(f'enter {field}')
                directory.append(info)
                ...
            case '2':
                try:
                    directory.edit()
                except TypeError:
                    print('Not int')
                    continue
                except IndexError:
                    print('Index out range')

            case '3':
                directory.find()
