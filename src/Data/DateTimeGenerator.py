"""
Generating random dates with two possibilities.
The function get_random_datetime is not included into tests and class. It is just
another possibility.
"""

import random
from datetime import datetime, timedelta
from typing import Tuple


def is_leap(year: int) -> bool:
    """
    If the year is leap.
    :param year: int. Year
    :return: bool. If the year is leap.
    """
    return bool(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_random_datetime(min_year: int = 1900, max_year: int = datetime.now().year) -> datetime:
    """
    Function to generate random date time within the range in format yyyy-mm-dd hh:mm:ss.000000.
    :param min_year: int.
    :param max_year: int.
    :return: datetime. Random date in format yyyy-mm-dd hh:mm:ss.000000.
    """
    start = datetime(min_year, 1, 1, 0, 0, 0)
    n_years = max_year - min_year + 1
    end = start + timedelta(days=365.25 * n_years)

    return start + (end - start) * random.random()


class DateTimeGenerator:
    """
    Class for generating random dates.
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_year(year_from: int = 1900, year_to: int = datetime.now().year) -> int:
        """
        Generate a random year in interval year_from to year_to both included.
        :param year_from: int.
        :param year_to: int.
        :return: int. Random year from interval.
        """
        return random.randint(year_from, year_to)

    @staticmethod
    def generate_month(month_from: int = 1, month_to: int = 12) -> int:
        """
        Generate a random month in the interval month_from to month_to both included.
        :param month_from: int.
        :param month_to: int.
        :return: int. Random month from the interval.
        """
        return random.randint(month_from, month_to)

    @staticmethod
    def generate_day(year: int, month: int) -> int:
        """
        Generate a random date from month and year.
        :param year: int.
        :param month: int.
        :return: int. Random date.
        """
        day_from = 1
        if month in {1, 3, 5, 7, 8, 10, 12}:
            day_to = 31
        elif month in {4, 6, 9, 11}:
            day_to = 30
        if month == 2:
            if is_leap(year):
                day_to = 29
            else:
                day_to = 28

        return random.randint(day_from, day_to)

    def generate_date(self, year_from: int = 1900, year_to: int = datetime.now().year,
                      month_from: int = 1, month_to: int = 12) -> Tuple[int, int, int]:
        """
        Generate random date as triplet (yyyy, m, d).
        :param year_from: int.
        :param year_to: int.
        :param month_from: int.
        :param month_to: int.
        :return: Tuple[int, int, int]. Triplet (yyyy, m, d).
        """
        year = self.generate_year(year_from, year_to)
        month = self.generate_month(month_from, month_to)
        day = self.generate_day(year, month)

        return (year, month, day)

    @staticmethod
    def convert_triplet(triplet: Tuple[int, int, int]) -> int:
        """
        Converts triplet from Tuple[yyyy, m, d] to yyyymmdd.
        :param triplet: Tuple[int, int, int]. Triplet (yyyy, m, d)
        :return: int. Date in format yyyymmdd.
        """
        y = str(triplet[0])

        if triplet[1] < 10:
            m = "0" + str(triplet[1])
        else:
            m = str(triplet[1])

        if triplet[2] < 10:
            d = "0" + str(triplet[2])
        else:
            d = str(triplet[2])

        return int(y + m + d)
