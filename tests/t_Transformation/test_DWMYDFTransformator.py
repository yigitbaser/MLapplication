"""
Testing
"""
from typing import Any, Tuple

import numpy as np
import pandas as pd
import pytest
from numpy import ndarray
from pandas import DataFrame

# TODO - Find out if there is a more effective to avoid long imports
import src.Data.TimeSeriesGenerator as TSG
import src.Transformation.DWMYDFTransformator as T
import src.Transformation.ListTSToDFTransformator as TS_T
import src.Transformation.NumberToOneTransformator as NTO_T
from src.GlobalConstants import ATTR_TIME, ATTR_VALUE, PER_DAY, \
    PER_WEEK, PER_MONTH, PER_YEAR, FP, P

PER_TIME = (PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR)
ATTRS_DF = (ATTR_TIME, ATTR_VALUE)
TRANSF_TYPE = (FP, P)

GROUND_TRUTH_DAY = np.array([20190801, 20190805, 20190809, 20190811, 20190813, 20190822,
                             20190824, 20190825,
                             20190826, 20190827, 20190827, 20190828, 20190829, 20190829,
                             20190901, 20190901,
                             20190903,
                             20190909, 20190909, 20190911, 20190912, 20190913, 20190917,
                             20190917, 20190922,
                             20190922,
                             20190923, 20190924, 20190929, 20190930])
GROUND_TRUTH_MONTH = np.array([201801, 201803, 201803, 201805, 201806, 201809, 201809,
                               201810, 201810,
                               201811, 201811, 201812, 201812, 201901, 201901, 201901, 201901,
                               201904, 201904,
                               201905, 201906, 201906, 201907, 201908, 201909, 201909, 201909,
                               201909,
                               201911, 201911])
GROUND_TRUTH_WEEK = np.array([201801, 201801, 201801, 201803, 201805, 201806, 201807, 201845,
                              201845,
                              201847, 201848, 201849, 201850, 201901, 201901, 201902, 201903,
                              201903,
                              201907, 201908, 201908, 201909, 201909, 201944, 201944, 201947,
                              201948,
                              201948, 201949, 201950])
GROUND_TRUTH_YEAR = np.array([2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018,
                              2018, 2018, 2018, 2018, 2019, 2019, 2019, 2019, 2019, 2019,
                              2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019,
                              2019, 2019])


def _get_ts_df(time_type: str, per_time: Tuple[str, str, str, str] = PER_TIME,
               attrs_df: Tuple[str, str] = ATTRS_DF) -> DataFrame:
    tsg = TSG.TimeSeriesGenerator()
    ts_to_df_transf = TS_T.ListTSToDFTransformator()
    nto_t = NTO_T.NumberToOneTransformator()

    if time_type == per_time[0]:
        ts = tsg.generate_day_data()
    elif time_type == per_time[1]:
        ts = tsg.generate_week_data()
    elif time_type in (per_time[2], per_time[3]):
        ts = tsg.generate_month_data()

    ts_df = ts_to_df_transf.fit_predict(ts, attrs_df)
    ts_df = nto_t.fit_predict(ts_df, ATTR_VALUE)

    return ts_df


def _transform_ts_df(ts_df: DataFrame, transformation_type: str, time_type: str,
                     transf_type: Tuple[str, str] = TRANSF_TYPE, attr_time: str = ATTR_TIME) \
        -> DataFrame:
    t = T.DWMYDFTransformator()

    if transformation_type == transf_type[0]:
        transformed_data = t.fit_predict(ts_df, time_type, attr_time)
    elif transformation_type == transf_type[1]:
        transformed_data = t.predict(ts_df, time_type, attr_time)

    return transformed_data


@pytest.mark.parametrize("transformation_type, time_type, ground_truth", # type:ignore
                         [
                             (FP, PER_DAY, GROUND_TRUTH_DAY),
                             (P, PER_DAY, GROUND_TRUTH_DAY),
                             (FP, PER_WEEK, GROUND_TRUTH_WEEK),
                             (P, PER_WEEK, GROUND_TRUTH_WEEK),
                             (FP, PER_MONTH, GROUND_TRUTH_MONTH),
                             (P, PER_MONTH, GROUND_TRUTH_MONTH),
                             (FP, PER_YEAR, GROUND_TRUTH_YEAR),
                             (P, PER_YEAR, GROUND_TRUTH_YEAR)
                         ])
def test_conversion(transformation_type: str, time_type: str, ground_truth: ndarray,
                    attr_value: str = ATTR_VALUE, attr_time: str = ATTR_TIME) -> Any:
    """
    Test for transformator.
    :param transformation_type:  str. FP for "f" (fit-predict) and P for "p" (predict).
    :param time_type: str. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m", PER_YEAR for "y".
    :param ground_truth: ndarray. Array of true values.
    """
    df_ground_truth = pd.DataFrame()
    df_ground_truth[attr_value] = [1] * len(ground_truth)
    df_ground_truth[attr_time + "_" + time_type] = ground_truth

    ts_df = _get_ts_df(time_type)
    transform_data = _transform_ts_df(ts_df, transformation_type, time_type)

    assert transform_data.equals(df_ground_truth)
