from abc import ABCMeta, abstractmethod
from typing import List, Optional

from src.vacancy import Vacancy


class AbstractSave(metaclass=ABCMeta):
    """
    Класс AbstractSave - это абстрактный базовый класс, необходим для дальнейшего наследования классами, предназначенными
    для работы с внешними классами. 
    Унаследован от класса ABC из модуля abc. 
    
    Содержит абстрактные методы для дальнейшего переопределения в дочерних классах, а также методы, которые являются общими и независимыми
    от типа файлов, с которыми выполняется работа.
    """

    file_path: str = ''

    @abstractmethod
    def write_data(self, data: List[Vacancy]) -> None:
        """
        Функция write_data определяет метод абстрактного класса, который должен быть переопределен в дочернем классе.
        
        Параметры
        ---------
        data : List
                Список экземпляров класса Vacancy. 
        """
        pass

    @abstractmethod
    def get_data(self) -> List[Vacancy]:
        """
        Функция get_data определяет метод абстрактного класса, который должен быть переопределен в дочернем классе.
        Она принимает экземпляр своего собственного класса в качестве параметра.
        """
        pass

    def delete_data(self) -> None:
        """
        Функция delete_data определяет метод класса для использования его функциональности во всех дочерних классах.
        Она принимает экземпляр своего собственного класса в качестве параметра. Удаляет все содержимое файла, указанного
        в атрибутах класса дочернего класса.
        """
        open(self.file_path, 'w').close()

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """
        Функция add_vacancy определяет метод класса для использования его функциональности во всех дочерних классах.
        Извлекает данные из файла хранилища, добавляет экземпляр класса Vacancy к его содержимому
        и записывает обновленные данные в файл.

        Параметры
        ---------
        vacancy : Vacancy
                Экземпляр класса Vacancy.
        
        """
        vacancies: List[Vacancy] = self.get_data()
        vacancies.append(vacancy)
        self.write_data(vacancies)

    def get_vacancies_by_salary(self, salary: str) -> List[Vacancy]:
        """
        Функция get_vacancies_by_salary определяет метод базового класса и предназначена для использования в дочерних классах.
        Анализирует значения запроса, запрашивает все данные, хранящиеся в файле, фильтрует экземпляры по значению
        поля salary_from, возвращает экземпляры класса Vacancy, удовлетворяющие запросу, в виде списка экземпляров класса Vacancy.
        
        Параметры
        ---------
        salary : str
                Зарплата.

        """
        salary: List[str] = salary.split('-')
        for i in range(2):
            salary[i]: List[str] = salary[i].split()
            result: str = ''
            for j in range(len(salary[i])):
                if salary[i][j].isdigit():
                    result += salary[i][j]
            salary[i]: str = result

        vacancies = self.get_data()
        filtred_vacancies: List[Vacancy] = list(filter(
            lambda x: x.salary_from >= int(salary[0]) and x.salary_from <= int(salary[1]), vacancies
        ))
        return filtred_vacancies

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """
        Функция delete_vacancy определяет метод класса для использования его функциональности во всех дочерних классах.
        Извлекает данные из файла хранилища, находит экземпляр класса Vacancy, соответствующий
        полученному в аргументах, удаляет его из сохраненных данных и записывает обновленные данные в файл.

        Параметры
        ---------
        vacancy : Vacancy
                Экземпляр класса Vacancy.
        
        """
        vacancies: List[Vacancy] = self.get_data()

        i_del: Optional[int] = None

        for i, instance in enumerate(vacancies):
            if instance.url == vacancy.url:
                i_del = i
                break

        if i_del is not None:
            vacancies.pop(i_del)

        self.write_data(vacancies)