"""
Generator
"""

import random
from datetime import datetime, timedelta
from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pandas import DataFrame

from src.GlobalConstants import ATTR_ID, ATTR_TIME, ATTR_VALUE
from src.Exception.TDDException import NoProperOptionInIf


class FloatTripletGenerator:
    """
    Class for generating Data frame with three columns:
    First is ID, a list of integers.
    Second is TIME, which is composed of datetimes.
    Third is VALUE, each value is either an integer, a float or equal to one.
    Please see doctest file for more info.
    """

    def __init__(self, attr_id: str = ATTR_ID, attr_time: str = ATTR_TIME,
                 attr_value: str = ATTR_VALUE, exp_dist_mean: int = 100) -> None:
        self.seed = 123
        self.attr_id = attr_id
        self.attr_time = attr_time
        self.attr_value = attr_value
        self.exp_dist_mean = exp_dist_mean

    def set_seed_number(self, seed_number: int) -> None:
        """
        Set seed number.
        :param seed_number: int. New seed
        """
        self.seed = seed_number

    def _set_seed(self) -> None:
        """
        Set seed for random generator.
        """
        random.seed(self.seed)
        np.random.seed(self.seed)

    @staticmethod
    def _random_date(start: datetime = datetime(2015, 1, 1), end: datetime = datetime(2020, 1, 1)
                     ) -> datetime:
        """
        Generate a random datetime between a start and an end date.
        :param start: datetime. Start date.
        :param end: datetime. End date.
        :return: datetime.
        """
        delta = end - start
        return start + timedelta(days=random.randint(0, delta.days + 1))

    def generate_year_data(self, data_type: str, max_int: int = 100, n: int = 30
                           ) -> List[Tuple[datetime, int]]:
        """
        Generates time series of year Data with the values . For example see doctest file.
        :param data_type: String. If ones ("ones"), integer ("integers") or amount ("amount").
        :param max_int: Integer or None. Max limit for each value generated. Default is 100.
        :param n: int. Number of observations.
        :return: List[Tuple[datetime, int]]. Time series as list.
        """
        self._set_seed()
        if data_type == "ones":
            upper = 1
            data = [(self._random_date(), random.randint(1, upper)) for i in range(0, n)]
        elif data_type == "integers":
            upper = max_int
            data = [(self._random_date(), random.randint(1, upper)) for i in range(0, n)]
        elif data_type == "amount":
            data = [(self._random_date(),
                     np.round(np.random.exponential(scale=self.exp_dist_mean), 2)
                     ) for i in range(0, n)]
        else:
            raise NoProperOptionInIf

        return data

    def generate_sample_triplet_df(self, data_type: str, max_int: int = 100,
                                   id_list: Optional[List[int]] = None) -> DataFrame:
        """
        Generates sample Data frame with IDs, Timestamps and Values. For example see doctest file.
        :param data_type: String. If ones ("ones"), integer ("integers") or float ("floats").
        :param max_int: Integer of None. Max limit for each value generated.
        :param id_list: List[int]. list of unique IDs.
        :return: DataFrame. DF with three columns named (in order) ATTR_ID, ATTR_TIME, ATTR_VALUE.
        """
        if id_list is None:
            self._set_seed()
            id_list = [random.randint(1, 5) for i in range(100)]

        df_triplet = pd.DataFrame()
        n = len(id_list)

        timestamp, value = zip(*self.generate_year_data(
            data_type=data_type, n=n, max_int=max_int))

        df_triplet[self.attr_id] = list(id_list)
        df_triplet[self.attr_time] = list(timestamp)
        df_triplet[self.attr_value] = list(value)

        return df_triplet
