"""
Transformator
"""
from pandas import Series

from src.Transformation.BaseTransformator import BaseTransformator


class SeriesToSparseSeriesTransformator(BaseTransformator):  # type:ignore
    """
    Transforms timeseries into a sparse timeseries.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "pd.Series",
            "output_type": "pd.Series"
        }
        BaseTransformator.__init__(self, name="SeriesToSparseSeries", description=d)

    @staticmethod
    def _transform(ts: Series) -> Series:
        """
        Drops all rows from a timeseries that are equal to zero.
        :param ts: Series. Timeseries.
        :return: Series. Sparse timeseries.
        """
        return ts[ts != 0]

    # pylint: disable=arguments-differ
    def fit(self, ts: Series) -> None:
        pass

    def fit_predict(self, ts: Series) -> Series:
        return self._transform(ts)

    def predict(self, ts: Series) -> Series:
        return self._transform(ts)
    # pylint: enable=arguments-differ
