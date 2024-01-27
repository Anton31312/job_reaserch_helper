from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    """
    Класс Vacancy представляет модель данных для использования в приложении.
    Содержит аннотации ко всем полям и переопределенные "магические" методы.

    Атрибуты
    --------
    name : str
            Наименования вакансии
    url : str
            Ссылка на вакансию
    employer : str
            Сотрудник
    salary_from : int
            Зарплата от
    salary_to : int
            Зарплата до
    description : str
            Описание

    """

    def __init__(self, name: str, url: str, employer: str, salary_from: Optional[int], salary_to: Optional[int], description: str):
        """
        Функция __init__ переопределяет магический метод, 
        устанавливает все необходимые атрибуты для объекта Vacancy.

        Атрибуты
        --------
        name : str
            Наименования вакансии
        url : str
            Ссылка на вакансию
        employer : str
            Сотрудник
        salary_from : int
            Зарплата от
        salary_to : int
            Зарплата до
        description : str
            Описание
        """
        self.name = name
        self.url = url
        self.employer = employer
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description

    def __repr__(self) -> str:
        """
        Функция __repr__ переопределяет магический метод, определенный классом данных.
        
        :return: str представление экземпляра класса.
        """
        return self.name

    def __lt__(self, other) -> bool:
        """
        Функция __lt__ определяет магический метод для сравнения двух экземпляров класса.
        Определяет поле, по значению которого производится сравнение. 

        :param: other другой объект для сравнения.
        
        :return: bool результата сравнения экземпляров класса.
        """
        return self.salary_from < other.salary_from

    def __le__(self, other) -> bool:
        """
        Функция __le__ определяет магический метод для сравнения двух экземпляров класса. 
        Определяет поле, по значению которого производится сравнение.
        
        :param: other другой объект для сравнения. 

        :return: bool результата сравнения экземпляров класса.
        """
        return self.salary_from <= other.salary_from

    def __gt__(self, other) -> bool:
        """
        Функция __gt__ определяет магический метод для сравнения двух экземпляров класса. 
        Определяет поле, по значению которого производится сравнение.

        :param: other другой объект для сравнения. 

        :return: bool результата сравнения экземпляров класса.
        """
        return self.salary_from > other.salary_from

    def __ge__(self, other) -> bool:
        """
        Функция __ge__ определяет магический метод для сравнения двух экземпляров класса. 
        Определяет поле, по значению которого производится сравнение.
        
        :param: other другой объект для сравнения. 

        :return: bool результата сравнения экземпляров класса.
        """
        return self.salary_from >= other.salary_from

    def __eq__(self, other) -> bool:
        """
        Функция __eq__ определяет магический метод для сравнения двух экземпляров класса. 
        Определяет поле, по значению которого производится сравнение.
        
        :param: other другой объект для сравнения. 

        :return: bool результата сравнения экземпляров класса.
        """
        return self.salary_from == other.salary_from