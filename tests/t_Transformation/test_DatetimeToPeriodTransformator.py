# pylint: disable=invalid-name
# pylint: enable=invalid-name
"""
Tester
"""

from datetime import datetime

import pytest

import src.Transformation.DatetimeToPeriodTransformator as D
from src.GlobalConstants import FP, P, PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR
from src.Exception.TDDException import NoProperOptionInIf

INPUT_DATE = datetime(2020, 2, 26)

OUTPUT_DAY = datetime(2020, 2, 26)
OUTPUT_WEEK = datetime(2020, 3, 1)
OUTPUT_MONTH = datetime(2020, 2, 29)
OUTPUT_YEAR = datetime(2020, 12, 31)


def _transform(transf_type: str, date: datetime, attr_per: str) -> datetime:
    dtp = D.DatetimeToPeriodTransformator()
    if transf_type == FP:
        period_date = dtp.fit_predict(date, attr_per)
    elif transf_type == P:
        period_date = dtp.predict(date, attr_per)
    else:
        raise NoProperOptionInIf
    #  TODO - We have to specify the return type because mypy is considering it as Any when the
    #   transformator gives back an integer. The error mypy is displaying is: Returning Any from
    #   function declared to return "datetime".
    return datetime(period_date.year, period_date.month, period_date.day)


@pytest.mark.parametrize("transf_type, date, attr_per, correct_date",  # type:ignore
                         [(FP, INPUT_DATE, PER_DAY, OUTPUT_DAY),
                          (P, INPUT_DATE, PER_DAY, OUTPUT_DAY),
                          (FP, INPUT_DATE, PER_WEEK, OUTPUT_WEEK),
                          (P, INPUT_DATE, PER_WEEK, OUTPUT_WEEK),
                          (FP, INPUT_DATE, PER_MONTH, OUTPUT_MONTH),
                          (P, INPUT_DATE, PER_MONTH, OUTPUT_MONTH),
                          (FP, INPUT_DATE, PER_YEAR, OUTPUT_YEAR),
                          (P, INPUT_DATE, PER_YEAR, OUTPUT_YEAR)
                          ])
def test_periods(transf_type: str, date: datetime, attr_per: str, correct_date: datetime) -> None:
    """
    To test that the calculated datetime adjusted to a given period is correct.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param date: Datetime. Input date.
    :param attr_per: String. Attribute period, PER_DAY for "d", PER_WEEK for "w",
    PER_MONTH for "m" and PER_YEAR for "y".
    :param correct_date: Datetime. Correct output of the transformator.
    """
    period_date = _transform(transf_type, date, attr_per)
    assert period_date == correct_date
