import os
from json import dump, load, JSONDecodeError

from typing import TypedDict


class Info(TypedDict, total=False):
    """
    типовой словарь для записи в справочник

    first_name: Имя пользователя

     mid_name: str Отчество\n
     last_name: str Фамилия\n
     company: str Компания\n
     phone_number: str номер телефона \n
    additional_number: str дополнительный\n
    """
    first_name: str
    mid_name: str
    last_name: str
    company: str
    phone_number: str
    additional_number: str


class TelephoneDirectory:
    HEAD = {'uid': 'НПП', 'first_name': 'Имя', 'mid_name': 'Отчество', 'last_name': 'Фамилия', 'company': 'Компания',
            'phone_number': 'Номер', 'additional_number': 'Сотовый'}
    """

    """

    def __init__(self, path: str):
        """
            В конструктор подается путь
        :param path: путь до файла
        :exception JSONDecodeError : Файл пуст, нет
        """

        self._path: str = path
        self.cur_page: int = 1
        self.count_item: int = 5
        self.len_sep = 30
        self._directory: None | list[Info] = []

        try:
            if os.path.isfile(path):
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

        [print(name_col, end=' ' * (self.len_sep - len(name_col)) + '|') for name_col in self.HEAD.values()]
        print('\n')

        for ind, rows in enumerate(self.directory):
            [print(row, end=' ' * (self.len_sep - len(row)) + '|') for row in [str(ind)] + list(rows.values())]
            print('\n')
            if not ind % self.count_item and ind > 0:
                print(f'\npage {self.cur_page}'.format())
                self.cur_page += 1
        print(f'\npage {self.cur_page}')

    def append(self, ):
        """
        Добавляет запись в справочник

        :return:
        """
        info = Info()
        for field in info_keys:
            info[field] = input(f'enter {field}')
        self.directory = info

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
        phone_id = int(input('Enter НПП'))
        info = directory.directory[phone_id]

        for ind, field in enumerate(keys := list(self.HEAD.keys())[1:]):
            print(f'{ind}. {self.HEAD[field]}')
        ind_field = int(input('select item'))
        info[keys[ind_field]] = input('enter value')


if __name__ == '__main__':
    ans = None
    directory = TelephoneDirectory('../l.json')
    info_keys = list(directory.HEAD.keys())[1:0]
    while ans != '4':
        print(directory)
        print('1.Add\n' \
              '2.Edit\n' \
              '3.Find\n' \
              '4.Exit\n')
        ans = input('Choose:')
        match ans:
            case '1':
                directory.append()
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
