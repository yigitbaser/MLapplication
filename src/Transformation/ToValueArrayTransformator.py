"""
Transformator
"""
from typing import List, Tuple, Union
from datetime import datetime
from numpy import array, ndarray

from src.Transformation.BaseTransformator import BaseTransformator


class ToValueArrayTransformator(BaseTransformator):  # type:ignore
    """
    Transforms the timeseries of list of tuples List[Tuple[datetime, value]] - extract only the
    values into numpy array.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "List[Tuple[datetime, value]]",
            "output_type": "np.array"
        }
        BaseTransformator.__init__(self, name="ListTSToArray", description=d)

    @staticmethod
    def _transform(ts_list: List[Tuple[datetime, Union[int, float]]]) -> ndarray:
        """
        Returns the values of a timeseries of list of tuples as an numpy array.
        :param ts_list: List of tuples of datetime and a numerical value. List of tuples (timestamp,
        value). The values can be either integers or floats.
        :returns np.array. Array of values which can be either integers or floats.
        """
        _, value_array = zip(*ts_list)

        return array(value_array)

    # pylint: disable=arguments-differ
    def fit(self, ts_list: List[Tuple[datetime, Union[int, float]]]) -> None:
        pass

    def fit_predict(self, ts_list: List[Tuple[datetime, Union[int, float]]]) -> ndarray:
        return self._transform(ts_list)

    def predict(self, ts_list: List[Tuple[datetime, Union[int, float]]]) -> ndarray:
        return self._transform(ts_list)
    # pylint: enable=arguments-differ
