"""
Transformator
"""
from datetime import datetime
from typing import List, Tuple
import pandas as pd
from pandas import Series

from src.Transformation.BaseTransformator import BaseTransformator


class ListTSToSeriesTransformator(BaseTransformator):  # type:ignore
    """
    Transforms the time series of list of tuples List[Tuple[datetime, int]]
    into pandas Series and sort it with respect to time.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "List[Tuple[datetime, int]]",
            "output_type": "pd.Series"
        }
        BaseTransformator.__init__(self, name="ListTSToSeries", description=d)

    @staticmethod
    def _transform(ts_list: List[Tuple[datetime, int]], attr_names: List[str]) \
            -> Series:
        """
        Transforms the time series of list of tuples into pandas Series and sort
        it with respect to time.
        :param ts_list: List. List of tuples (timestamp, value).
        :param attr_names: List. Name of time column and name of Data column.
        :returns Series.
        """
        ts = pd.Series(dict(ts_list))
        ts.rename(attr_names[1], inplace=True)
        ts.sort_index(inplace=True)

        return ts

    # pylint: disable=arguments-differ
    def fit(self, ts_list: List[Tuple[datetime, int]], attr_names: List[str]) \
            -> None:
        pass

    def fit_predict(self, ts_list: List[Tuple[datetime, int]], attr_names: List[str]) \
            -> Series:
        return self._transform(ts_list, attr_names)

    def predict(self, ts_list: List[Tuple[datetime, int]], attr_names: List[str]) \
            -> Series:
        return self._transform(ts_list, attr_names)
    # pylint: enable=arguments-differ
