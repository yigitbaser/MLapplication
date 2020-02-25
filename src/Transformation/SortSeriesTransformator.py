"""
Transformator
"""
from pandas import Series

from src.Transformation.BaseTransformator import BaseTransformator


class SortSeriesTransformator(BaseTransformator):  # type:ignore
    """
    Transforms timeseries into a sorted timeseries.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "pd.Series",
            "output_type": "pd.Series"
        }
        BaseTransformator.__init__(self, name="SortSeries", description=d)

    @staticmethod
    def _transform(ts: Series) -> Series:
        """
        It sorts a timeseries upon its index. From oldest datetime to most recent.
        :param ts: Series. Timeseries.
        :return: Series.  Transformed timeseries.
        """
        return ts.sort_index()

    # pylint: disable=arguments-differ
    def fit(self, ts: Series) -> None:
        pass

    def fit_predict(self, ts: Series) -> Series:
        return self._transform(ts)

    def predict(self, ts: Series) -> Series:
        return self._transform(ts)
    # pylint: enable=arguments-differ
