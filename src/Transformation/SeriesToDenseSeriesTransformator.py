"""
Transformator
"""
from typing import Optional
from datetime import datetime
import numpy as np
import pandas as pd
from pandas import Series

from src.Transformation.BaseTransformator import BaseTransformator


class SeriesToDenseSeriesTransformator(BaseTransformator):  # type:ignore
    """
    Transforms a sparse timeseries to a dense timeseries.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "pd.Series",
            "output_type": "pd.Series"
        }
        BaseTransformator.__init__(self, name="SeriesToDenseSeries", description=d)

    @staticmethod
    def _transform(ts: Series, attr_per: str, start: Optional[datetime], end: Optional[datetime]) \
            -> Series:
        """
        To dense a timeseries with a specific time period. It allows the option to set a start and
        end date.
        :param ts: Series. Timeseries.
        :param attr_per: String. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m",
        PER_YEAR for "y".
        :param start: Datetime or None. Initial start date for the transformed timeseries. Default
        is the starting date of the original timeseries.
        :param end: Datetime or None. End start date for the transformed timeseries. Default
        is the starting date of the original timeseries.
        :return: Series. Transformed dense timeseries.
        """
        start = start or min(ts.index)
        end = end or max(ts.index)
        idx = pd.date_range(start=start, end=end, freq=attr_per.upper())
        ts_dense = Series(data=np.zeros(len(idx)), index=idx)
        ts_dense[ts_dense.index.isin(ts.index)] = ts
        ts_dense = ts_dense.astype(ts.dtype)
        return ts_dense

    # pylint: disable=arguments-differ
    def fit(self, ts: Series, attr_per: str, start: Optional[datetime] = None,
            end: Optional[datetime] = None) -> None:
        pass

    def fit_predict(self, ts: Series, attr_per: str, start: Optional[datetime] = None,
                    end: Optional[datetime] = None) -> Series:
        return self._transform(ts, attr_per, start, end)

    def predict(self, ts: Series, attr_per: str, start: Optional[datetime] = None,
                end: Optional[datetime] = None) -> Series:
        return self._transform(ts, attr_per, start, end)
    # pylint: enable=arguments-differ
