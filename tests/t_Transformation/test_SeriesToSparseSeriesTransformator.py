"""
Tester
"""

from datetime import datetime

import pytest
from pandas import Series

import src.Transformation.SeriesToSparseSeriesTransformator as S
from src.GlobalConstants import FP, P
from src.Exception.TDDException import NoProperOptionInIf
from tests.t_Transformation.test_FrequencyResampleSeriesTransformator import TS_INPUT_UNIT, \
    TS_CORRECT_TRPLT_D, TS_INPUT_TRPLT, TS_CORRECT_TRPLT_W

TS_INPUT_TRPLT_D = TS_CORRECT_TRPLT_D
TS_CORRECT_TRPLT_D = TS_INPUT_TRPLT
TS_INPUT_TRPLT_W = TS_CORRECT_TRPLT_W
TS_CORRECT_TRPLT_W = Series(
    data=[1, 1, 1],
    index=[
        datetime(2019, 12, 29), datetime(2020, 1, 5), datetime(2020, 1, 19)
    ]
)
TS_INPUT_EMPTY = Series()


def _sparse(transf_type: str, ts_input: Series) -> Series:
    sts = S.SeriesToSparseSeriesTransformator()
    if transf_type == FP:
        ts_out = sts.fit_predict(ts_input)
    elif transf_type == P:
        ts_out = sts.predict(ts_input)
    else:
        raise NoProperOptionInIf
    return ts_out


@pytest.mark.parametrize("transf_type, ts_input, ts_correct", # type:ignore
                         [(FP, TS_INPUT_UNIT, TS_INPUT_UNIT),
                          (P, TS_INPUT_UNIT, TS_INPUT_UNIT),
                          (FP, TS_INPUT_TRPLT_D, TS_CORRECT_TRPLT_D),
                          (P, TS_INPUT_TRPLT_D, TS_CORRECT_TRPLT_D),
                          (FP, TS_INPUT_TRPLT_W, TS_CORRECT_TRPLT_W),
                          (P, TS_INPUT_TRPLT_W, TS_CORRECT_TRPLT_W),
                          (FP, TS_INPUT_EMPTY, TS_INPUT_EMPTY),
                          (P, TS_INPUT_EMPTY, TS_INPUT_EMPTY)
                          ])
def test_sparse(transf_type: str, ts_input: Series, ts_correct: Series) -> None:
    """
    To test that the outputted timeseries is a sparse timeseries of the original one.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_input: Series. Timeseries.
    :param ts_correct: Series. Expected output of the transformator.
    """
    ts_out = _sparse(transf_type, ts_input)
    assert ts_out.equals(ts_correct)
