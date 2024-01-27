from typing import Optional, List, Tuple

from src.abstract_parser import AbstractParser
from src.hhru.hhru_parser import HHruParser
from src.superjob.superjob_parser import SuperJobParser
from views.save.json_save import JsonSave
from views.save.csv_save import CSVSave
from views.save.exсel_save import ExcelSave
from views.view import display_vacancy


def main():
    """
    Основная функция необходима для взаимодействия с пользователем через консоль.
    Создает экземпляры класса. 
    Связывает функционирование программы в единую оболочку.
    """
    save_json = JsonSave()
    save_csv = CSVSave()
    save_excel = ExcelSave()

    parsers: List[Tuple[str, AbstractParser]] = [('HeadHunter', HHruParser()), ('SuperJob', SuperJobParser())]

    print('Здравствуй, соискатель!')
    while True:
        print('\nГотов продолжить? \nВведите "отмена", чтобы выйти из программы.\n')
        if input(': ').strip().lower() == 'отмена':
            break
        data: list = []
        print('\nВакансии по какому ключевому слову мы будем искать? \nЧтобы выполнить поиск по всем вакансиям, нажмите Enter.')
        keyword: Optional[str] = input(': ').strip().lower()
        if keyword == '' or keyword == ' ':
            keyword = None

        for item in parsers:
            print()
            print(f'Выполните поиск на {item[0]}? \nВведите "да" или "нет"')
            if input(': ').strip().lower() == 'да':
                parser = item[1]
                data += parser.get_vacancy(keyword)

        if data == []:
            print('\nДанные для дальнейшего использования получены не были.')
            continue
        else:
            save_json.write_data(data)
            save_csv.write_data(data)
            save_excel.write_data(data)
            print(f'\nНайдено: {len(data)} вакансий.')

        print('\nВведите номер вакансии для отображения.')
        count = int(input(': '))
        _data = save_json.get_data()
        display_vacancy(_data[:count])


if __name__ == '__main__':
    main()