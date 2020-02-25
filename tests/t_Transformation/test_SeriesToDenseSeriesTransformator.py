"""
Tester
"""

from datetime import datetime
from typing import Optional, List

import pytest
from pandas import Series

import src.Transformation.SeriesToDenseSeriesTransformator as S
from src.GlobalConstants import FP, P, PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR
from src.Exception.TDDException import NoProperOptionInIf

TS_INPUT_UNIT = Series(
    data=[1],
    index=[datetime(2020, 1, 1)]
)  # Output is the same as input for PER_DAY
TS_INPUT_UNIT_Y = Series(
    data=[1],
    index=[datetime(2020, 12, 31)]
)
TS_CORRECT_UNIT_Y = Series(
    data=[1],
    index=[datetime(2020, 12, 31)]
)
TS_INPUT_TRPLT_D = Series(
    data=[1, 2, 3],
    index=[datetime(2019, 12, 29), datetime(2020, 1, 1), datetime(2020, 1, 13)
           ]
)
TS_INPUT_TRPLT_UNSORTED_D = Series(
    data=[3, 2, 1],
    index=[datetime(2020, 1, 13), datetime(2020, 1, 1), datetime(2019, 12, 29)
           ]
)
TS_CORRECT_TRPLT_D = Series(
    data=[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    index=[datetime(2019, 12, 29), datetime(2019, 12, 30), datetime(2019, 12, 31),
           datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3),
           datetime(2020, 1, 4), datetime(2020, 1, 5), datetime(2020, 1, 6),
           datetime(2020, 1, 7), datetime(2020, 1, 8), datetime(2020, 1, 9),
           datetime(2020, 1, 10), datetime(2020, 1, 11), datetime(2020, 1, 12),
           datetime(2020, 1, 13)
           ]
)
TS_INPUT_TRPLT_M = Series(
    data=[1, 2, 3],
    index=[datetime(2019, 2, 28), datetime(2019, 11, 30), datetime(2020, 1, 31)
           ]
)
TS_CORRECT_TRPLT_M = Series(
    data=[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    index=[datetime(2019, 2, 28), datetime(2019, 3, 31), datetime(2019, 4, 30),
           datetime(2019, 5, 31), datetime(2019, 6, 30), datetime(2019, 7, 31),
           datetime(2019, 8, 31), datetime(2019, 9, 30), datetime(2019, 10, 31),
           datetime(2019, 11, 30), datetime(2019, 12, 31), datetime(2020, 1, 31)
           ]
)
TS_INPUT_TRPLT_W = Series(
    data=[1, 2, 3],
    index=[datetime(2019, 12, 8), datetime(2019, 12, 29), datetime(2020, 1, 12)
           ]
)
TS_CORRECT_TRPLT_W = Series(
    data=[1, 0, 0, 2, 0, 3],
    index=[datetime(2019, 12, 8), datetime(2019, 12, 15), datetime(2019, 12, 22),
           datetime(2019, 12, 29), datetime(2020, 1, 5), datetime(2020, 1, 12)
           ]
)

START_OUT = datetime(2019, 12, 1)
START_IN = datetime(2019, 12, 15)
END_OUT = datetime(2020, 1, 19)
END_IN = datetime(2019, 12, 29)

TS_CORRECT_TRPLT_W_OUT = Series(
    data=[0, 1, 0, 0, 2, 0, 3, 0],
    index=[datetime(2019, 12, 1), datetime(2019, 12, 8), datetime(2019, 12, 15),
           datetime(2019, 12, 22), datetime(2019, 12, 29), datetime(2020, 1, 5),
           datetime(2020, 1, 12), datetime(2020, 1, 19)
           ]
)
TS_CORRECT_TRPLT_W_IN = Series(
    data=[0, 0, 2],
    index=[datetime(2019, 12, 15), datetime(2019, 12, 22), datetime(2019, 12, 29)
           ]
)


def _to_dense(transf_type: str, ts_input: Series, attr_per: str, start: Optional[datetime] = None,
              end: Optional[datetime] = None) -> Series:
    sds = S.SeriesToDenseSeriesTransformator()
    if transf_type == FP:
        ts_out = sds.fit_predict(ts_input, attr_per, start, end)
    elif transf_type == P:
        ts_out = sds.predict(ts_input, attr_per, start, end)
    else:
        raise NoProperOptionInIf
    return ts_out


@pytest.mark.parametrize("transf_type, ts_input, ts_correct, attr_per", # type:ignore
                         [(FP, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY),
                          (P, TS_INPUT_UNIT, TS_INPUT_UNIT, PER_DAY),
                          (FP, TS_INPUT_UNIT_Y, TS_CORRECT_UNIT_Y, PER_YEAR),
                          (P, TS_INPUT_UNIT_Y, TS_CORRECT_UNIT_Y, PER_YEAR),
                          (FP, TS_INPUT_TRPLT_D, TS_CORRECT_TRPLT_D, PER_DAY),
                          (P, TS_INPUT_TRPLT_D, TS_CORRECT_TRPLT_D, PER_DAY),
                          (FP, TS_INPUT_TRPLT_UNSORTED_D, TS_CORRECT_TRPLT_D, PER_DAY),
                          (P, TS_INPUT_TRPLT_UNSORTED_D, TS_CORRECT_TRPLT_D, PER_DAY),
                          (FP, TS_INPUT_TRPLT_M, TS_CORRECT_TRPLT_M, PER_MONTH),
                          (P, TS_INPUT_TRPLT_M, TS_CORRECT_TRPLT_M, PER_MONTH),
                          (FP, TS_INPUT_TRPLT_W, TS_CORRECT_TRPLT_W, PER_WEEK),
                          (P, TS_INPUT_TRPLT_W, TS_CORRECT_TRPLT_W, PER_WEEK)]
                         )
def test_density(transf_type: str, ts_input: Series, ts_correct: Series, attr_per: str) -> None:
    """
    To test the density of the transformed timeseries.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_input: Series. Timeseries to be transformed.
    :param ts_correct: Series. Timeseries that is the correct output of the transformator.
    :param attr_per: String. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m",
    PER_YEAR for "y".
    """
    ts_out = _to_dense(transf_type, ts_input, attr_per)
    assert ts_out.equals(ts_correct)


@pytest.mark.parametrize("transf_type, ts_input, ts_correct, attr_per, boundaries", # type:ignore
                         [(FP, TS_INPUT_TRPLT_W, TS_CORRECT_TRPLT_W_IN, PER_WEEK, [START_IN,
                                                                                   END_IN]),
                          (P, TS_INPUT_TRPLT_W, TS_CORRECT_TRPLT_W_IN, PER_WEEK, [START_IN,
                                                                                  END_IN]),
                          (FP, TS_INPUT_TRPLT_W, TS_CORRECT_TRPLT_W_OUT, PER_WEEK, [START_OUT,
                                                                                    END_OUT]),
                          (P, TS_INPUT_TRPLT_W, TS_CORRECT_TRPLT_W_OUT, PER_WEEK, [START_OUT,
                                                                                   END_OUT])]
                         )
def test_defined_dates(transf_type: str, ts_input: Series, ts_correct: Series, attr_per: str,
                       boundaries: List[datetime]) -> None:
    """
    To test the density of the transformed timeseries with an explicit start and end date.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_input: Series. Timeseries to be transformed.
    :param ts_correct: Series. Timeseries that is the correct output of the transformator.
    :param attr_per: String. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m",
    PER_YEAR for "y".
    :param boundaries: List of two datetimes. Starting and ending date.
    """
    ts_out = _to_dense(transf_type, ts_input, attr_per, boundaries[0], boundaries[1])
    assert ts_out.equals(ts_correct)
