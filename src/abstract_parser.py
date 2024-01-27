from abc import ABCMeta, abstractmethod
from typing import Optional


class AbstractParser(metaclass=ABCMeta):
    """
    Класс AbstractParser является абстрактным классом. 
    Унаследован от класса ABC из модуля abc.
    Определяет методы, которые должны быть переопределены в унаследованных классах.
    """

    @abstractmethod
    def get_vacancy(self, keyword: Optional[str]):
        """
        Функция get_vacancy определяет метод абстрактного класса, который должен быть переопределен в дочернем классе.
        """
        pass