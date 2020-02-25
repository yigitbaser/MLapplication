"""
Transformator
"""
from calendar import monthrange
from datetime import datetime
from dateutil.relativedelta import relativedelta, SU

from src.Exception.TDDException import NoProperOptionInIf
from src.GlobalConstants import PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR
from src.Transformation.BaseTransformator import BaseTransformator


class DatetimeToPeriodTransformator(BaseTransformator):  # type:ignore
    """
    Adjusts a datetime to the specific datetime of the indicated period.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "datetime",
            "output_type": "datetime"
        }
        BaseTransformator.__init__(self, name="DatetimeToPeriod", description=d)

    @staticmethod
    def _transform(date: datetime, attr_per: str) -> datetime:
        """
        It calculates the corresponding datetime of the given period for the input datetime. For
        "w" it uses Sundays as a datetime reference and for "m" or "y" is uses the last day of
        month or year. For the period "d", as expected it returns the input datetime.
        :param date: Datetime. Input date.
        :param attr_per: String. Attribute period, PER_DAY for "d", PER_WEEK for "w",
        PER_MONTH for "m" and PER_YEAR for "y".
        :return: Datetime. Calculated datetime for the given attribute period.
        """
        if attr_per == PER_DAY:
            period_date = date
        elif attr_per == PER_WEEK:
            period_date = date + relativedelta(weekday=SU)
        elif attr_per == PER_MONTH:
            period_date = datetime(date.year, date.month, monthrange(date.year, date.month)[-1])
        elif attr_per == PER_YEAR:
            period_date = datetime(date.year, 12, 31)
        else:
            raise NoProperOptionInIf

        return period_date

    # pylint: disable=arguments-differ
    def fit(self, date: datetime, attr_per: str) -> None:
        pass

    def fit_predict(self, date: datetime, attr_per: str) -> datetime:
        return self._transform(date, attr_per)

    def predict(self, date: datetime, attr_per: str) -> datetime:
        return self._transform(date, attr_per)
    # pylint: enable=arguments-differ
