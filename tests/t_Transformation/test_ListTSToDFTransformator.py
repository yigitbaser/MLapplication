"""
Tester
"""

import datetime

from pandas import DataFrame

import src.Data.TimeSeriesGenerator as G
import src.Transformation.ListTSToDFTransformator as T
from src.GlobalConstants import ATTR_TIME, ATTR_VALUE


def _get_ts_df(attr_time: str = ATTR_TIME, attr_value: str = ATTR_VALUE) -> DataFrame:
    tsg = G.TimeSeriesGenerator()
    t = T.ListTSToDFTransformator()

    df = t.fit_predict(
        tsg.generate_month_data(),
        [attr_time, attr_value]
    )

    return df


def test_ts_df_shape() -> None:
    """
    To confirm the correct shape of the generated DataFrame.
    """
    df = _get_ts_df()
    assert df.shape == (30, 2)


def test_ts_df_date_type(attr_time: str = ATTR_TIME) -> None:
    """
    To test the format of the output Data.
    :param attr_time: String. Time attribute.
    """
    df = _get_ts_df()
    assert isinstance(df[attr_time][0], datetime.datetime)


def test_ts_df_names(attr_time: str = ATTR_TIME, attr_value: str = ATTR_VALUE) -> None:
    """
    To test that the attr name are the DataFrame columns.
    :param attr_time: String. Time attribute.
    :param attr_value: String. Value attribute.
    """
    df = _get_ts_df()
    assert df.columns[0] == attr_time and df.columns[1] == attr_value
