"""
Transformator
"""
from pandas import Series, Grouper

from src.Exception.TDDException import NoProperOptionInIf
from src.Transformation.BaseTransformator import BaseTransformator


class GroupBySeriesTransformator(BaseTransformator):  # type:ignore
    """
    Groups a timeseries upon time period (day, week, month and year).
    """

    def __init__(self) -> None:
        d = {
            "input_type": "pd.Series",
            "output_type": "pd.Series"
        }
        BaseTransformator.__init__(self, name="GroupBySeries", description=d)

    @staticmethod
    def _transform(ts: Series, attr_period: str, fun_type: str) -> Series:
        """
        Groups a timeseries by a specified time period.
        :param ts: Series. Timeseries.
        :param attr_period: String. Attribute period, PER_DAY for "d", PER_WEEK for "w",
        PER_MONTH for "m" and PER_YEAR for "y".
        :param fun_type: String. Function, either "sum" or "count", to be applied on each of the
        grouped periods.
        :return: Series. Grouped timeseries.
        """
        if fun_type == "sum":
            ts = ts.groupby(Grouper(freq=attr_period.upper())).sum()
        elif fun_type == "count":
            ts = ts.groupby(Grouper(freq=attr_period.upper())).count()
        else:
            raise NoProperOptionInIf

        ts = ts[ts != 0]  # To drop VALUE = 0 rows

        return ts

    # pylint: disable=arguments-differ
    def fit(self, ts: Series, attr_period: str, fun_type: str) -> None:
        pass

    def predict(self, ts: Series, attr_period: str, fun_type: str) -> Series:
        return self._transform(ts, attr_period, fun_type)

    def fit_predict(self, ts: Series, attr_period: str, fun_type: str) -> Series:
        return self._transform(ts, attr_period, fun_type)
    # pylint: enable=arguments-differ
