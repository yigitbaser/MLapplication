"""
Transformator
"""
from typing import Optional
from numpy import ndarray
from pandas.core.arrays.datetimes import DatetimeArray

from src.GlobalConstants import PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR
from src.Transformation.BaseTransformator import BaseTransformator


class DWMYTransformator(BaseTransformator):  # type:ignore
    """
    Transforms datetime array to format yyyymmdd, yyyymm, yyyyww, yyyy.
    """

    def __init__(self, per_day: str = PER_DAY, per_week: str = PER_WEEK,
                 per_month: str = PER_MONTH, per_year: str = PER_YEAR) -> None:
        d = {
            "input_type": "",
            "output_type": ""
        }
        BaseTransformator.__init__(self, name="DWMY", description=d)

        self.per_day = per_day
        self.per_week = per_week
        self.per_month = per_month
        self.per_year = per_year

    def _transform(self, X: DatetimeArray, time_type: str) -> Optional[ndarray]:
        """
        Transforms datetime array to format yyyymmdd, yyyymm, yyyyww, yyyy.
        :param X: DatetimeArray. Original array.
        :param time_type: str. "d" for day, "w" for week, "m" for month, "y" for year.
        :return: ndarray.
        """
        if time_type == self.per_day:
            return ((X.year + X.month / 100 + X.day / 10000) * 10000).astype(int)
        if time_type == self.per_week:
            return ((X.year + X.week / 100) * 100).astype(int)
        if time_type == self.per_month:
            return ((X.year + X.month / 100) * 100).astype(int)
        if time_type == self.per_year:
            return X.year.astype(int)

        return None

    # pylint: disable=arguments-differ
    def fit(self, X: DatetimeArray, time_type: str) -> None:
        pass

    def fit_predict(self, X: DatetimeArray, time_type: str) -> ndarray:
        return self._transform(X, time_type)

    def predict(self, X: DatetimeArray, time_type: str) -> ndarray:
        return self._transform(X, time_type)
    # pylint: enable=arguments-differ
