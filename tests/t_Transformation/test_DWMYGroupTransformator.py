"""
Tester
"""
from typing import Any, Tuple

import pytest
from pandas import DataFrame

import src.Transformation.DWMYGroupTransformator as T
from src.GlobalConstants import ATTR_TIME, ATTR_VALUE, PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR, \
    FP, P

TRANS_TYPE = (FP, P)
PER_TIME = (PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR)
ATTRS_DF = (ATTR_TIME, ATTR_VALUE)


def _get_ground_truth_day(attr_time: str = ATTR_TIME, attr_value: str = ATTR_VALUE,
                          per_day: str = PER_DAY) -> DataFrame:
    ground_truth = DataFrame()
    ground_truth[attr_time + "_" + per_day] = [20190101, 20190102, 20190103]
    ground_truth[attr_value] = [1, 2, 3]

    return ground_truth


def _get_ground_truth_week(attr_time: str = ATTR_TIME, attr_value: str = ATTR_VALUE,
                           per_week: str = PER_WEEK) -> DataFrame:
    ground_truth = DataFrame()
    ground_truth[attr_time + "_" + per_week] = [201901, 201902, 201903]
    ground_truth[attr_value] = [1, 2, 3]

    return ground_truth


def _get_ground_truth_month(attr_time: str = ATTR_TIME, attr_value: str = ATTR_VALUE,
                            per_month: str = PER_MONTH) -> DataFrame:
    ground_truth = DataFrame()
    ground_truth[attr_time + "_" + per_month] = [201901, 201902, 201903]
    ground_truth[attr_value] = [1, 2, 3]

    return ground_truth


def _get_ground_truth_year(attr_time: str = ATTR_TIME, attr_value: str = ATTR_VALUE,
                           per_year: str = PER_YEAR) -> DataFrame:
    ground_truth = DataFrame()
    ground_truth[attr_time + "_" + per_year] = [2019, 2020, 2021]
    ground_truth[attr_value] = [1, 2, 3]

    return ground_truth


def _get_ts_df(time_type: str, attrs_df: Tuple[str, str] = ATTRS_DF,
               per_time: Tuple[str, str, str, str] = PER_TIME) -> DataFrame:
    ts_df = DataFrame()
    if time_type == per_time[0]:
        ts_df[attrs_df[0] + "_" + time_type] = \
            [20190101, 20190102, 20190102, 20190103, 20190103, 20190103]
    elif time_type in (per_time[1], per_time[2]):
        ts_df[attrs_df[0] + "_" + time_type] = [201901, 201902, 201902, 201903, 201903, 201903]
    elif time_type == per_time[3]:
        ts_df[attrs_df[0] + "_" + time_type] = [2019, 2020, 2020, 2021, 2021, 2021]

    ts_df[ATTR_VALUE] = [1] * 6

    return ts_df


def _transform_ts_df(ts_df: DataFrame, transformation_type: str, time_type: str,
                     attrs_df: Tuple[str, str] = ATTRS_DF,
                     trans_type: Tuple[str, str] = TRANS_TYPE) -> DataFrame:
    t = T.DWMYGroupTransformator()

    if transformation_type == trans_type[0]:
        transformed_data = t.fit_predict(ts_df, time_type, [attrs_df[0], attrs_df[1]], sum)
    elif transformation_type == trans_type[1]:
        transformed_data = t.predict(ts_df, time_type, [attrs_df[0], attrs_df[1]], sum)

    return transformed_data


@pytest.mark.parametrize("transformation_type, time_type, ground_truth", # type:ignore
                         [
                             (FP, PER_DAY, _get_ground_truth_day()),
                             (P, PER_DAY, _get_ground_truth_day()),
                             (FP, PER_WEEK, _get_ground_truth_week()),
                             (P, PER_WEEK, _get_ground_truth_week()),
                             (FP, PER_MONTH, _get_ground_truth_month()),
                             (P, PER_MONTH, _get_ground_truth_month()),
                             (FP, PER_YEAR, _get_ground_truth_year()),
                             (P, PER_YEAR, _get_ground_truth_year())
                         ])
def test_conversion(transformation_type: str, time_type: str, ground_truth: DataFrame) -> Any:
    """
    Performs tests.
    :param transformation_type: str. F for "f" (fit), P for "p" (predict)
    and FP for "fp (fit_predict).
    :param time_type: str. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m", PER_YEAR for "y".
    :param ground_truth: Data Frame. True results.
    """
    ts_df = _get_ts_df(time_type)
    transformed_data = _transform_ts_df(ts_df, transformation_type, time_type)

    assert transformed_data.equals(ground_truth)
