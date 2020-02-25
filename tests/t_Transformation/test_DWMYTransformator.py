"""
Tester
"""

# pylint: disable=c0103
from typing import Tuple

import numpy as np
import pytest
from numpy import ndarray
from pandas.core.arrays.datetimes import DatetimeArray

import src.Data.TimeSeriesGenerator as TSG
import src.Transformation.DWMYTransformator as T
import src.Transformation.ListTSToDFTransformator as TS_T
from src.GlobalConstants import ATTR_TIME, ATTR_VALUE, PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR, \
    FP, P

TRANS_TYPE = (FP, P)
ATTRS_DF = (ATTR_TIME, ATTR_VALUE)
PER_TIME = (PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR)

ground_truth_day = np.array([20190801, 20190805, 20190809, 20190811, 20190813, 20190822, 20190824,
                             20190825, 20190826, 20190827, 20190827, 20190828, 20190829, 20190829,
                             20190901, 20190901, 20190903, 20190909, 20190909, 20190911, 20190912,
                             20190913, 20190917, 20190917, 20190922, 20190922, 20190923, 20190924,
                             20190929, 20190930])
ground_truth_month = np.array([201801, 201803, 201803, 201805, 201806, 201809, 201809, 201810,
                               201810, 201811, 201811, 201812, 201812, 201901, 201901, 201901,
                               201901, 201904, 201904, 201905, 201906, 201906, 201907, 201908,
                               201909, 201909, 201909, 201909, 201911, 201911])
ground_truth_week = np.array([201801, 201801, 201801, 201803, 201805, 201806, 201807, 201845,
                              201845, 201847, 201848, 201849, 201850, 201901, 201901, 201902,
                              201903, 201903, 201907, 201908, 201908, 201909, 201909, 201944,
                              201944, 201947, 201948, 201948, 201949, 201950])
ground_truth_year = np.array([2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018,
                              2018, 2018, 2018, 2018, 2019, 2019, 2019, 2019, 2019, 2019,
                              2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019,
                              2019, 2019])


def _get_ts_array(time_type: str, attrs_df: Tuple[str, str] = ATTRS_DF,
                  per_time: Tuple[str, str, str, str] = PER_TIME) -> DatetimeArray:
    tsg = TSG.TimeSeriesGenerator()
    ts_to_df_transf = TS_T.ListTSToDFTransformator()

    if time_type == per_time[0]:
        ts = tsg.generate_day_data()
    elif time_type == per_time[1]:
        ts = tsg.generate_week_data()
    elif time_type in [per_time[2], per_time[3]]:
        ts = tsg.generate_month_data()

    ts_d = ts_to_df_transf.fit_predict(ts, attrs_df)

    return ts_d[attrs_df[0]].array


def _transform_ts_array(ts_array: DatetimeArray, transformation_type: str, time_type: str,
                        transf_type: Tuple[str, str] = TRANS_TYPE) -> DatetimeArray:
    t = T.DWMYTransformator()

    if transformation_type == transf_type[0]:
        transformed_data = t.fit_predict(ts_array, time_type)
    elif transformation_type == transf_type[1]:
        transformed_data = t.predict(ts_array, time_type)

    return transformed_data


@pytest.mark.parametrize("transformation_type, time_type, ground_truth",  # type:ignore
                         [
                             (FP, PER_DAY, ground_truth_day),
                             (P, PER_DAY, ground_truth_day),
                             (FP, PER_WEEK, ground_truth_week),
                             (P, PER_WEEK, ground_truth_week),
                             (FP, PER_MONTH, ground_truth_month),
                             (P, PER_MONTH, ground_truth_month),
                             (FP, PER_YEAR, ground_truth_year),
                             (P, PER_YEAR, ground_truth_year)
                         ])
def test_conversion(transformation_type: str, time_type: str, ground_truth: ndarray) -> None:
    """

    :param transformation_type: String. FP for "fp" (fit_predict) and P for "p" (predict).
    :param time_type: String. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m",
    PER_YEAR for "y".
    :param ground_truth:
    """
    time_array = _get_ts_array(time_type)
    transform_data = _transform_ts_array(time_array, transformation_type, time_type)

    assert np.array_equal(transform_data, ground_truth)
