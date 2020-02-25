"""
Tester
"""

from datetime import datetime

import pytest
from pandas import Series

import src.Transformation.SortSeriesTransformator as S
from src.GlobalConstants import FP, P
from src.Exception.TDDException import NoProperOptionInIf

# Create three TS pairs, 1-3-5 Data points
TS_INPUT_UNIT = Series(data=[1],
                       index=[datetime(2020, 1, 1)]
                       )  # Output is the same as input

TS_INPUT_TRIPLET = Series(
    data=[2, 1, 3],
    index=[
        datetime(2020, 1, 2), datetime(2020, 1, 1), datetime(2020, 1, 3)
    ]
)
TS_CORRECT_TRIPLET = Series(
    data=[1, 2, 3],
    index=[
        datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)
    ]
)

TS_INPUT_QUINTUPLET = Series(
    data=[3, 2, 1, 5, 4],
    index=[
        datetime(2020, 1, 3), datetime(2020, 1, 2), datetime(2020, 1, 1), datetime(2020, 1, 5),
        datetime(2020, 1, 4)
    ]
)
TS_CORRECT_QUINTUPLET = Series(
    data=[1, 2, 3, 4, 5],
    index=[
        datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4),
        datetime(2020, 1, 5)
    ]
)


def _sort(transf_type: str, ts_input: Series) -> Series:
    sst = S.SortSeriesTransformator()
    if transf_type == FP:
        ts_out = sst.fit_predict(ts_input)
    elif transf_type == P:
        ts_out = sst.predict(ts_input)
    else:
        raise NoProperOptionInIf
    return ts_out


@pytest.mark.parametrize("transf_type, ts_input, ts_correct", # type:ignore
                         [(FP, TS_INPUT_UNIT, TS_INPUT_UNIT),
                          (P, TS_INPUT_UNIT, TS_INPUT_UNIT),
                          (FP, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET),
                          (P, TS_INPUT_TRIPLET, TS_CORRECT_TRIPLET),
                          (FP, TS_INPUT_QUINTUPLET, TS_CORRECT_QUINTUPLET),
                          (P, TS_INPUT_QUINTUPLET, TS_CORRECT_QUINTUPLET)]
                         )
def test_sorting(transf_type: str, ts_input: Series, ts_correct: Series) -> None:
    """
    Test to verify that the ts inputs are sorted and thus equal to ts correct.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_input: Series. Timeseries to be transformed.
    :param ts_correct: Series. Timeseries that is the correct output of the transformation.
    """
    ts_out = _sort(transf_type, ts_input)
    assert ts_correct.equals(ts_out)
