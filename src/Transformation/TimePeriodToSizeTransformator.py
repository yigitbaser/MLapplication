"""
Transformator
"""
from datetime import datetime

from src.Exception.TDDException import NoProperOptionInIf
from src.GlobalConstants import PER_DAY, PER_WEEK, PER_MONTH, PER_YEAR
from src.Transformation.BaseTransformator import BaseTransformator


class TimePeriodToSizeTransformator(BaseTransformator):  # type:ignore
    """
    It calculates the difference between two dates upon an attribute period.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "List[datetime, datetime]",
            "output_type": "integer"
        }
        BaseTransformator.__init__(self, name="TimePeriodToSize", description=d)

    @staticmethod
    def _transform(start_date: datetime, end_date: datetime, attr_per: str) -> int:
        """
        Calculates the number of respective time periods in the range given by
        start_date and end_date including both edges.
        :param start_date: Datetime. Start date of the period.
        :param end_date: Datetime. End date of the period.
        :param attr_per: String. String. PER_DAY for "d", PER_WEEK for "w", PER_MONTH for "m",
        PER_YEAR for "y".
        :return: Integer. Number of time periods within the range (with a given time period).
        """
        if attr_per == PER_DAY:
            delta = (end_date - start_date).days
        elif attr_per == PER_WEEK:
            delta = (end_date - start_date).days // 7
        elif attr_per == PER_MONTH:
            delta = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month
        elif attr_per == PER_YEAR:
            delta = end_date.year - start_date.year
        else:
            raise NoProperOptionInIf

        # add one because it is not a difference, but number of time periods, the
        # first edge has to be included as well.
        return int(delta + 1)

    # pylint: disable=arguments-differ
    def fit(self, start_date: datetime, end_date: datetime, attr_per: str) -> int:
        pass

    def fit_predict(self, start_date: datetime, end_date: datetime, attr_per: str) -> int:
        return self._transform(start_date, end_date, attr_per)

    def predict(self, start_date: datetime, end_date: datetime, attr_per: str) -> int:
        return self._transform(start_date, end_date, attr_per)
    # pylint: enable=arguments-differ
