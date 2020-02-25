"""
Transformator
"""
from typing import List, Tuple
from datetime import datetime
import pandas as pd
from pandas import DataFrame

from src.Transformation.BaseTransformator import BaseTransformator


class ListTSToDFTransformator(BaseTransformator):  # type:ignore
    """
    Transforms the time series of list of tuples List[Tuple[datetime, int]]
    into pandas Data Frame and sort it with respect to time.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "List[Tuple[datetime, int]]",
            "output_type": "pd.DataFrame"
        }
        BaseTransformator.__init__(self, name="ListTSToDF", description=d)

    @staticmethod
    def _transform(ts_list: List[Tuple[datetime, int]], attr_names: List[str]) \
            -> DataFrame:
        """
        Transforms the time series of list of tuples into pandas Series and sort
        it with respect to time.
        :param ts_list: List. List of tuples (timestamp, value).
        :param attr_names: List. Name of time column and name of Data column.
        :returns DataFrame.
        """
        df = pd.DataFrame(ts_list)
        df.columns = attr_names
        df.sort_values(by=attr_names[0], inplace=True)
        df.reset_index(drop=True, inplace=True)

        return df

    # pylint: disable=arguments-differ
    def fit(self, ts_list: List[Tuple[datetime, int]], attr_names: List[str]) \
            -> None:
        pass

    def fit_predict(self, ts_list: List[Tuple[datetime, int]], attr_names: List[str]) \
            -> DataFrame:
        return self._transform(ts_list, attr_names)

    def predict(self, ts_list: List[Tuple[datetime, int]], attr_names: List[str]) \
            -> DataFrame:
        return self._transform(ts_list, attr_names)
    # pylint: enable=arguments-differ
