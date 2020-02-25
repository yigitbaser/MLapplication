#pylint: disable=invalid-name
#pylint: enable=invalid-name
"""
Tester
"""

from datetime import datetime
from typing import List

import pytest

import src.Transformation.TimePeriodToSizeTransformator as T
from src.GlobalConstants import FP, P, PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR
from src.Exception.TDDException import NoProperOptionInIf

INPUT_DAY = [datetime(2020, 1, 1), datetime(2020, 1, 31)]
INPUT_WEEK = [datetime(2020, 1, 5), datetime(2020, 2, 9)]
INPUT_MONTH = [datetime(2019, 1, 31), datetime(2020, 2, 29)]
INPUT_YEAR = [datetime(2015, 1, 31), datetime(2020, 1, 31)]

OUTPUT_DAY = 31
OUTPUT_WEEK = 6
OUTPUT_MONTH = 14
OUTPUT_YEAR = 6


def _transform(transf_type: str, input_per: List[datetime], attr_per: str) -> int:
    tps = T.TimePeriodToSizeTransformator()
    if transf_type == FP:
        period_size = tps.fit_predict(input_per[0], input_per[1], attr_per)
    elif transf_type == P:
        period_size = tps.predict(input_per[0], input_per[1], attr_per)
    else:
        raise NoProperOptionInIf
    #  TODO - We have to specify the return type because mypy is considering it as Any when the
    #   transformator gives back an integer. The error mypy is displaying is: Returning Any from
    #   function declared to return "int".
    return int(period_size)


@pytest.mark.parametrize("transf_type, input_per, attr_per, correct_per",  # type:ignore
                         [(FP, INPUT_DAY, PER_DAY, OUTPUT_DAY),
                          (P, INPUT_DAY, PER_DAY, OUTPUT_DAY),
                          (FP, INPUT_WEEK, PER_WEEK, OUTPUT_WEEK),
                          (P, INPUT_WEEK, PER_WEEK, OUTPUT_WEEK),
                          (FP, INPUT_MONTH, PER_MONTH, OUTPUT_MONTH),
                          (P, INPUT_MONTH, PER_MONTH, OUTPUT_MONTH),
                          (FP, INPUT_YEAR, PER_YEAR, OUTPUT_YEAR),
                          (P, INPUT_YEAR, PER_YEAR, OUTPUT_YEAR)
                          ])
def test_period_size(transf_type: str, input_per: List[datetime], attr_per: str,
                     correct_per: int) -> None:
    """
    To test that for a given attribute period and two dates, the estimated
    number of periods is the expected.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param input_per: List[datetime, datetime]. Start date and end date (respectively).
    :param attr_per: String. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m",
    PER_YEAR for "y".
    :param correct_per: Integer. Correct output of the transformator.
    """
    period_size = _transform(transf_type, input_per, attr_per)
    assert period_size == correct_per
