"""
Tester
"""

from datetime import datetime

import pytest
from pandas import Series

import src.Transformation.GroupBySeriesTransformator as G
from src.GlobalConstants import PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR, FP, P
from src.Exception.TDDException import NoProperOptionInIf

TS_INPUT_UNIT = Series(data=[1],
                       index=[datetime(2020, 1, 1)]
                       )  # Output is the same as input

TS_CORRECT_UNIT_WEEK = Series(data=[1],
                              index=[datetime(2020, 1, 5)]
                              )
TS_CORRECT_UNIT_MONTH = Series(data=[1],
                               index=[datetime(2020, 1, 31)]
                               )
TS_CORRECT_UNIT_YEAR = Series(data=[1],
                              index=[datetime(2020, 12, 31)]
                              )
TS_INPUT_TRIPLET = Series(
    data=[1, 2, 3],
    index=[
        datetime(2019, 12, 25), datetime(2020, 1, 1), datetime(2020, 1, 2)
    ]
)
TS_CORRECT_TRIPLET_DAY = Series(
    data=[1, 2, 3],
    index=[
        datetime(2019, 12, 25), datetime(2020, 1, 1), datetime(2020, 1, 2)
    ]
)
TS_CORRECT_TRIPLET_WEEK = Series(
    data=[1, 5],
    index=[
        datetime(2019, 12, 29), datetime(2020, 1, 5)
    ]
)
TS_CORRECT_TRIPLET_MONTH = Series(
    data=[1, 5],
    index=[
        datetime(2019, 12, 31), datetime(2020, 1, 31)
    ]
)
TS_CORRECT_TRIPLET_YEAR = Series(
    data=[1, 5],
    index=[
        datetime(2019, 12, 31), datetime(2020, 12, 31)
    ]
)


def _transform(ts: Series, transformation_type: str, attr_per: str, fun_type: str) -> Series:
    gps = G.GroupBySeriesTransformator()
    if transformation_type == FP:
        ts_out = gps.fit_predict(ts, attr_per, fun_type)
    elif transformation_type == P:
        ts_out = gps.predict(ts, attr_per, fun_type)
    else:
        raise NoProperOptionInIf
    return ts_out


@pytest.mark.parametrize("trans_type, ts_input, ts_correct, attr_per", # type:ignore
                         [(FP, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY),
                          (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_WEEK, PER_WEEK),
                          (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_MONTH, PER_MONTH),
                          (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_YEAR, PER_YEAR),
                          (P, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY),
                          (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_WEEK, PER_WEEK),
                          (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_MONTH, PER_MONTH),
                          (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_YEAR, PER_YEAR),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_DAY, PER_DAY),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_WEEK, PER_WEEK),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_MONTH, PER_MONTH),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_YEAR, PER_YEAR),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_DAY, PER_DAY),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_WEEK, PER_WEEK),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_MONTH, PER_MONTH),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_YEAR, PER_YEAR)
                          ]
                         )
def test_periods(trans_type: str, ts_input: Series, ts_correct: Series, attr_per: str) -> None:
    """
    To test if the grouping is done accordingly per period.
    :param trans_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_input: Series. Timeseries to be transformed.
    :param ts_correct: Series. Timeseries that is the correct output of the transformation.
    :param attr_per: String. Attribute period, PER_DAY for "d", PER_WEEK for "w",
    PER_MONTH for "m" and PER_YEAR for "y".
    """
    ts_out = _transform(ts_input, trans_type, attr_per, "sum")
    assert ts_out.to_list() == ts_correct.to_list() and \
           ts_out.index.to_list() == ts_correct.index.to_list()


@pytest.mark.parametrize("trans_type, ts_input, ts_correct, attr_per", # type:ignore
                         [(FP, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY),
                          (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_WEEK, PER_WEEK),
                          (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_MONTH, PER_MONTH),
                          (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_YEAR, PER_YEAR),
                          (P, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY),
                          (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_WEEK, PER_WEEK),
                          (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_MONTH, PER_MONTH),
                          (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_YEAR, PER_YEAR),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_DAY, PER_DAY),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_WEEK, PER_WEEK),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_MONTH, PER_MONTH),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_YEAR, PER_YEAR),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_DAY, PER_DAY),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_WEEK, PER_WEEK),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_MONTH, PER_MONTH),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET_YEAR, PER_YEAR)
                          ]
                         )
def test_value_conservation(
        trans_type: str, ts_input: Series, ts_correct: Series, attr_per: str) -> None:
    """
    To test that the total sum of values of the timeseries is conserved after the transformation.
    :param trans_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_input: Series. Timeseries to be transformed.
    :param ts_correct: Series. Timeseries that is the correct output of the transformation.
    :param attr_per: String. Attribute period, PER_DAY for "d", PER_WEEK for "w",
    PER_MONTH for "m" and PER_YEAR for "y".
    """
    ts_out = _transform(ts_input, trans_type, attr_per, "sum")
    assert ts_out.sum() == ts_correct.sum()


@pytest.mark.parametrize("trans_type, ts_input, attr_per", # type:ignore
                         [(FP, TS_INPUT_UNIT, PER_DAY),
                          (FP, TS_INPUT_UNIT, PER_WEEK),
                          (FP, TS_INPUT_UNIT, PER_MONTH),
                          (FP, TS_INPUT_UNIT, PER_YEAR),
                          (P, TS_INPUT_UNIT, PER_DAY),
                          (P, TS_INPUT_UNIT, PER_WEEK),
                          (P, TS_INPUT_UNIT, PER_MONTH),
                          (P, TS_INPUT_UNIT, PER_YEAR),
                          (FP, TS_INPUT_TRIPLET, PER_DAY),
                          (FP, TS_INPUT_TRIPLET, PER_WEEK),
                          (FP, TS_INPUT_TRIPLET, PER_MONTH),
                          (FP, TS_INPUT_TRIPLET, PER_YEAR),
                          (P, TS_INPUT_TRIPLET, PER_DAY),
                          (P, TS_INPUT_TRIPLET, PER_WEEK),
                          (P, TS_INPUT_TRIPLET, PER_MONTH),
                          (P, TS_INPUT_TRIPLET, PER_YEAR)
                          ]
                         )
def test_information_conservation(
        trans_type: str, ts_input: Series, attr_per: str) -> None:
    """
    To test that all elements of the timeseries are present in the transformed timeseries.
    :param trans_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_input: Series. Timeseries to be transformed.
    :param attr_per: String. Attribute period, PER_DAY for "d", PER_WEEK for "w",
    PER_MONTH for "m" and PER_YEAR for "y".
    """
    ts_out = _transform(ts_input, trans_type, attr_per, "count")
    assert len(ts_input) == ts_out.sum()
