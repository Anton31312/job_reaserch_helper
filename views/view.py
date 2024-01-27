from typing import List
import pandas

from src.func import create_dict_for_data_frame_pandas
from src.vacancy import Vacancy


def display_vacancy(data: List[Vacancy]) -> None:
    """
    Функция display_vacancy производит вывод полученных данных в удобном 
    виде с помощью инструментов библиотеки pandas.
    
    Параметры
    ---------
    data : List
            Список экземпляров класса Vacancy. 
    
    """
    pandas.set_option('display.max_row', None)
    pandas.set_option('display.max_columns', None)
    pandas.options.display.expand_frame_repr = False

    num_row: int = len(data)
    data_frame = pandas.DataFrame(create_dict_for_data_frame_pandas(data))
    print(data_frame.head(num_row))
    print('-' * 120)