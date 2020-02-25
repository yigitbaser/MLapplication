"""
Tester
"""

from pandas import Series

import src.Data.TimeSeriesGenerator as G
import src.Transformation.ListTSToSeriesTransformator as T
from src.GlobalConstants import ATTR_TIME, ATTR_VALUE


def _get_ts_series(attr_time: str = ATTR_TIME, attr_value: str = ATTR_VALUE) -> Series:
    tsg = G.TimeSeriesGenerator()
    t = T.ListTSToSeriesTransformator()

    series = t.fit_predict(
        tsg.generate_month_data(),
        [attr_time, attr_value]
    )

    return series


def test_ts_series_shape() -> None:
    """
    To check that the transformation output is a series.
    """
    series = _get_ts_series()
    assert series.shape == (30,)


def test_ts_series_name(attr_value: str = ATTR_VALUE) -> None:
    """
    To corroborate that the series has been named appropriately.
    :param attr_value: String. Value attribute.
    """
    series = _get_ts_series()
    assert series.name == attr_value
