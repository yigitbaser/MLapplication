"""
Tester
"""

from datetime import datetime
from typing import Optional

import pytest
from pandas import Series

import src.Transformation.FrequencyResampleSeriesTransformator as S
from src.Exception.TDDException import NoProperOptionInIf
from src.GlobalConstants import FP, P, PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR

TS_INPUT_UNIT = Series(data=[1], index=[datetime(2020, 1, 1)])  # Output equal to input for PER_DAY
TS_CORRECT_UNIT_W = Series(data=[1], index=[datetime(2020, 1, 5)])
TS_CORRECT_UNIT_M = Series(data=[1], index=[datetime(2020, 1, 31)])
TS_CORRECT_UNIT_Y = Series(data=[1], index=[datetime(2020, 12, 31)])
TS_INPUT_TRPLT = Series(
    data=[1, 1, 1], index=[datetime(2019, 12, 29), datetime(2020, 1, 1),
                           datetime(2020, 1, 13)]
)
TS_INPUT_TRPLT_UNSORTED = Series(
    data=[1, 1, 1],
    index=[datetime(2020, 1, 13), datetime(2020, 1, 1),
           datetime(2019, 12, 29)]
)
TS_INPUT_TRPLT_UNIQUE = Series(
    data=[1, 2, 3],
    index=[datetime(2019, 12, 29), datetime(2020, 1, 1),
           datetime(2020, 1, 13)]
)
TS_CORRECT_TRPLT_D = Series(
    data=[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    index=[datetime(2019, 12, 29), datetime(2019, 12, 30),
           datetime(2019, 12, 31), datetime(2020, 1, 1),
           datetime(2020, 1, 2), datetime(2020, 1, 3),
           datetime(2020, 1, 4), datetime(2020, 1, 5),
           datetime(2020, 1, 6), datetime(2020, 1, 7),
           datetime(2020, 1, 8), datetime(2020, 1, 9),
           datetime(2020, 1, 10), datetime(2020, 1, 11),
           datetime(2020, 1, 12), datetime(2020, 1, 13)]
)
TS_CORRECT_TRPLT_W = Series(
    data=[1, 1, 0, 1],
    index=[
        datetime(2019, 12, 29), datetime(2020, 1, 5),
        datetime(2020, 1, 12), datetime(2020, 1, 19)]
)
TS_CORRECT_TRPLT_M = Series(
    data=[1, 2],
    index=[datetime(2019, 12, 31), datetime(2020, 1, 31)]
)
TS_CORRECT_TRPLT_Y = Series(
    data=[1, 2],
    index=[datetime(2019, 12, 31), datetime(2020, 12, 31)]
)
TS_CORRECT_TRPLT_SUM_M = Series(
    data=[1, 5],
    index=[datetime(2019, 12, 31), datetime(2020, 1, 31)]
)  # Output for sum resample of Unique triplet
TS_CORRECT_TRPLT_COUNT_M = Series(
    data=[1, 2],
    index=[datetime(2019, 12, 31), datetime(2020, 1, 31)]
)  # Output for count resample of Unique triplet
START_IN_D = datetime(2019, 12, 31)
END_IN_D = datetime(2020, 1, 2)
TS_CORRECT_TRPLT_D_PERIOD = Series(
    data=[0, 1, 0],
    index=[datetime(2019, 12, 31), datetime(2020, 1, 1),
           datetime(2020, 1, 2)]
)
START_IN_M = datetime(2019, 10, 16)
END_IN_M = datetime(2020, 2, 22)
TS_CORRECT_TRPLT_M_PERIOD = Series(
    data=[0, 0, 1, 2, 0],
    index=[datetime(2019, 10, 31), datetime(2019, 11, 30),
           datetime(2019, 12, 31), datetime(2020, 1, 31),
           datetime(2020, 2, 29)])

START_OUT_W = datetime(2019, 12, 4)
END_OUT_W = datetime(2020, 2, 2)
TS_CORRECT_TRPLT_W_PERIOD = Series(
    data=[0, 0, 0, 1, 1, 0, 1, 0, 0],
    index=[datetime(2019, 12, 8), datetime(2019, 12, 15),
           datetime(2019, 12, 22), datetime(2019, 12, 29),
           datetime(2020, 1, 5), datetime(2020, 1, 12),
           datetime(2020, 1, 19), datetime(2020, 1, 26),
           datetime(2020, 2, 2)]
)

START_OUT_Y = datetime(2016, 12, 4)
END_OUT_Y = datetime(2021, 2, 2)
TS_CORRECT_TRPLT_Y_PERIOD = Series(
    data=[0, 0, 0, 1, 2, 0],
    index=[datetime(2016, 12, 31), datetime(2017, 12, 31),
           datetime(2018, 12, 31), datetime(2019, 12, 31),
           datetime(2020, 12, 31), datetime(2021, 12, 31)]
)


# pylint: disable=too-many-arguments
def _transform(transf_type: str, ts_input: Series, attr_per: str, fun_type: str,
               start_date: Optional[datetime], end_date: Optional[datetime]) -> Series:
    sds = S.FrequencyResampleSeriesTransformator()
    if transf_type == FP:
        ts_out = sds.fit_predict(ts_input, attr_per, fun_type, start_date, end_date)
    elif transf_type == P:
        ts_out = sds.predict(ts_input, attr_per, fun_type, start_date, end_date)
    else:
        raise NoProperOptionInIf
    return ts_out


# pylint: enable=too-many-arguments


@pytest.mark.parametrize(  # type:ignore
    "transf_type, ts_input, ts_correct, attr_per, fun_type, start_date, end_date",
    [(FP, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY, "sum", None, None),
     (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_W, PER_WEEK, "sum", None, None),
     (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_M, PER_MONTH, "sum", None, None),
     (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_Y, PER_YEAR, "sum", None, None),
     (P, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY, "sum", None, None),
     (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_W, PER_WEEK, "sum", None, None),
     (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_M, PER_MONTH, "sum", None, None),
     (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_Y, PER_YEAR, "sum", None, None),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_D, PER_DAY, "sum", None, None),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_W, PER_WEEK, "sum", None, None),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_M, PER_MONTH, "sum", None, None),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_Y, PER_YEAR, "sum", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_D, PER_DAY, "sum", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_W, PER_WEEK, "sum", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_M, PER_MONTH, "sum", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_Y, PER_YEAR, "sum", None, None),
     (FP, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_D, PER_DAY, "sum", None, None),
     (FP, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_W, PER_WEEK, "sum", None, None),
     (FP, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_M, PER_MONTH, "sum", None, None),
     (FP, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_Y, PER_YEAR, "sum", None, None),
     (P, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_D, PER_DAY, "sum", None, None),
     (P, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_W, PER_WEEK, "sum", None, None),
     (P, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_M, PER_MONTH, "sum", None, None),
     (P, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_Y, PER_YEAR, "sum", None, None),
     (FP, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY, "count", None, None),
     (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_W, PER_WEEK, "count", None, None),
     (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_M, PER_MONTH, "count", None, None),
     (FP, TS_INPUT_UNIT, TS_CORRECT_UNIT_Y, PER_YEAR, "count", None, None),
     (P, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY, "count", None, None),
     (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_W, PER_WEEK, "count", None, None),
     (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_M, PER_MONTH, "count", None, None),
     (P, TS_INPUT_UNIT, TS_CORRECT_UNIT_Y, PER_YEAR, "count", None, None),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_D, PER_DAY, "count", None, None),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_W, PER_WEEK, "count", None, None),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_M, PER_MONTH, "count", None, None),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_Y, PER_YEAR, "count", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_D, PER_DAY, "count", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_W, PER_WEEK, "count", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_M, PER_MONTH, "count", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_Y, PER_YEAR, "count", None, None),
     (FP, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_D, PER_DAY, "count", None, None),
     (FP, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_W, PER_WEEK, "count", None, None),
     (FP, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_M, PER_MONTH, "count", None, None),
     (FP, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_Y, PER_YEAR, "count", None, None),
     (P, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_D, PER_DAY, "count", None, None),
     (P, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_W, PER_WEEK, "count", None, None),
     (P, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_M, PER_MONTH, "count", None, None),
     (P, TS_INPUT_TRPLT_UNSORTED, TS_CORRECT_TRPLT_Y, PER_YEAR, "count", None, None),
     (P, TS_INPUT_TRPLT_UNIQUE, TS_CORRECT_TRPLT_SUM_M, PER_MONTH, "sum", None, None),
     (P, TS_INPUT_TRPLT_UNIQUE, TS_CORRECT_TRPLT_COUNT_M, PER_MONTH, "count", None, None),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_D_PERIOD, PER_DAY, "sum", START_IN_D, END_IN_D),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_M_PERIOD, PER_MONTH, "count", START_IN_M, END_IN_M),
     (P, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_W_PERIOD, PER_WEEK, "sum", START_OUT_W, END_OUT_W),
     (FP, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_Y_PERIOD, PER_YEAR, "count", START_OUT_Y, END_OUT_Y)
     ])
# pylint: disable=too-many-arguments
def test_density_groupby_sorting(
        transf_type: str, ts_input: Series, ts_correct: Series, attr_per: str,
        fun_type: str, start_date: Optional[datetime], end_date: Optional[datetime]) -> None:
    """
    To test the density of the transformed timeseries.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_input: Series. Timeseries to be transformed.
    :param ts_correct: Series. Timeseries that is the correct output of the transformator.
    :param attr_per: String. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m",
    PER_YEAR for "y".
    :param fun_type: String. Function to be applied, either "sum" or "count".
    """
    ts_out = _transform(transf_type, ts_input, attr_per, fun_type, start_date, end_date)
    assert ts_out.equals(ts_correct)
# pylint: enable=too-many-arguments
