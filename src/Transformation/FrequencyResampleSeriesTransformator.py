"""
Transformator
"""
from datetime import datetime
from typing import Optional

from pandas import Series

from src.Exception.ConfigurationException import ValueTypeException
from src.Transformation.BaseTransformator import BaseTransformator


class FrequencyResampleSeriesTransformator(BaseTransformator):  # type:ignore
    """
    Transforms a sparse timeseries into a dense, sorted and grouped by period timeseries.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "pd.Series",
            "output_type": "pd.Series"
        }
        BaseTransformator.__init__(self, name="FrequencyResampleSeries", description=d)

    @staticmethod
    def _transform(ts: Series, attr_per: str, fun_type: str,
                   start_date: Optional[datetime], end_date: Optional[datetime]) -> Series:
        """
        To group, dense and sort a timeseries according to a time period and function.
        :param ts: Series. Timeseries to be transformed.
        :param attr_per: String. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m",
        PER_YEAR for "y".
        :param fun_type: String. Function to be applied, either "sum" or "count".
        :param start_date: Datetime or None. If None, it will take the first day available.
        :param end_date: Datetime or None. If None, it will take the last day available.
        :return: Series. Grouped, sorted and dense timeseries.
        """

        if start_date:
            start_series = Series([0], index=[start_date])
            ts = ts.append(start_series)
            ts = ts.loc[ts.index >= start_date]
        if end_date:
            end_series = Series([0], index=[end_date])
            ts = ts.append(end_series)
            ts = ts.loc[ts.index <= end_date]

        if fun_type == "sum":
            pass
        elif fun_type == "count":
            ts.loc[ts > 0] = 1
        else:
            raise ValueTypeException
        return ts.resample(attr_per.upper()).sum()

    # pylint: disable=arguments-differ
    # pylint: disable=too-many-arguments
    def fit(self, ts: Series, attr_per: str, fun_type: str,
            start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
            ) -> None:
        pass

    def fit_predict(self, ts: Series, attr_per: str, fun_type: str,
                    start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
                    ) -> Series:
        return self._transform(ts, attr_per, fun_type, start_date, end_date)

    def predict(self, ts: Series, attr_per: str, fun_type: str,
                start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
                ) -> Series:
        return self._transform(ts, attr_per, fun_type, start_date, end_date)
    # pylint: enable=arguments-differ
    # pylint: enable=too-many-arguments
