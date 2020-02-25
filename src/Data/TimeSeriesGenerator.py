"""
Generator of Data frame with time series column.
"""

# TODO - find workaround the days for month of February

import random
from datetime import datetime
from typing import List, Tuple, Union

import numpy as np
import pandas as pd
from pandas import DataFrame

from src.GlobalConstants import ATTR_ID, ATTR_TIME, ATTR_VALUE, ATTR_TIMESERIES


class TimeSeriesGenerator:
    """
    Class for generating Data frame with two columns.
    First is ID.
    Second list of tuples datetime, number.
    Please see doctest file for more info.
    """

    def __init__(self, attr_id: str = ATTR_ID, attr_time: str = ATTR_TIME,
                 attr_value: str = ATTR_VALUE, attr_timeseries: str = ATTR_TIMESERIES) \
            -> None:
        self.seed = 123
        self.attr_id = attr_id
        self.attr_time = attr_time
        self.attr_value = attr_value
        self.attr_timeseries = attr_timeseries

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

    # pylint disable = dangerous_default_value
    def generate_sample_ts_df(self, ts_lengths: Union[List[int], None] = None,
                              int_data: bool = False) -> DataFrame:
        """
        # TODO - add possibility of choosing the type
        Generates sample Data frame with time series. For example see doctest file.
        :param ts_lengths: List[int].
        :param int_data: bool. If ones or integer Data.
        :return: DataFrame. DF with two columns named as in GlobalConstants. First is ATTR_ID.
                 Second list of tuples ATTR_TIME, ATTR_VALUE (the column is named ATTR_TIMESERIES).
        """
        if ts_lengths is None:
            ts_lengths = [20, 30, 40, 50]

        df = pd.DataFrame()
        id_list = []
        data_list = []
        i = 10

        for n in ts_lengths:
            id_list.append(i)
            i = i + 10
            data_list.append(self.generate_day_data(int_data=int_data, n=n))

        df[self.attr_id] = id_list
        df[self.attr_timeseries] = data_list

        return df

    def generate_day_data(self, int_data: bool = True, n: int = 30) -> List[Tuple[datetime, int]]:
        """
        Generates time series of day Data. For example see doctest file.
        :param int_data: bool. If ones or integer Data.
        :param n: int. Number of observations.
        :return: List[Tuple[datetime, int]]. Time series as list.
        """
        self._set_seed()
        if int_data:
            upper = 100
        else:
            upper = 1
        data = [(datetime(
            year=2019,
            month=random.randint(8, 9),
            day=random.randint(1, 30)
        ), random.randint(1, upper)) for i in range(0, n)]

        return data

    def generate_week_data(self, int_data: bool = True, n: int = 30) -> List[Tuple[datetime, int]]:
        """
        Generates time series of week Data. For example see doctest file.
        :param int_data: bool. If ones or integer Data.
        :param n: int. Number of observations.
        :return: List[Tuple[datetime, int]]. Time series as list.
        """
        self._set_seed()
        if int_data:
            upper = 100
        else:
            upper = 1
        data = [(datetime(
            year=random.randint(2018, 2019),
            month=random.choice([11, 12, 1, 2]),
            day=random.randint(1, 30)
        ), random.randint(1, upper)) for i in range(0, n)]

        return data

    def generate_month_data(self, int_data: bool = True, n: int = 30) -> List[Tuple[datetime, int]]:
        """
        Generates time series of month Data. For example see doctest file.
        :param int_data: bool. If ones or integer Data.
        :param n: int. Number of observations.
        :return: List[Tuple[datetime, int]]. Time series as list.
        """
        self._set_seed()
        if int_data:
            upper = 100
        else:
            upper = 1
        data = [(datetime(
            year=random.randint(2018, 2019),
            month=random.randint(1, 12),
            day=random.randint(1, 30)
        ), random.randint(1, upper)) for i in range(0, n)]

        return data

    def generate_year_data(self, int_data: bool = True, n: int = 30) -> List[Tuple[datetime, int]]:
        """
        Generates time series of year Data. For example see doctest file.
        :param int_data: bool. If ones or integer Data.
        :param n: int. Number of observations.
        :return: List[Tuple[datetime, int]]. Time series as list.
        """
        self._set_seed()
        if int_data:
            upper = 100
        else:
            upper = 1
        data = [(datetime(
            year=random.randint(2015, 2019),
            month=random.randint(1, 12),
            day=random.randint(1, 30)
        ), random.randint(1, upper)) for i in range(0, n)]

        return data

    def generate_sample_triplet_df(
            self,
            id_list: Union[List[int], None] = None,
            int_data: bool = False
    ) -> DataFrame:
        """
        Generates sample Data frame with IDs, Timestamps and Values. For example see doctest file.
        :param id_list: List[int].
        :param int_data: bool. If ones or integer Data.
        :return: DataFrame. DF with three columns named as in GlobalConstants. First is ATTR_ID.
                 Second ATTR_TIME. Third ATTR_VALUE.
        """
        if id_list is None:
            self._set_seed()
            id_list = [random.randint(1, 9) for i in range(99)]
            id_list.append(10)

        df = pd.DataFrame()

        n = len(id_list)
        timestamp, value = zip(*self.generate_day_data(int_data=int_data, n=n))
        df[self.attr_id] = list(id_list)
        df[self.attr_time] = list(timestamp)
        df[self.attr_value] = list(value)
        df.loc[df[self.attr_id] == id_list[-1], self.attr_value] = 105

        return df
