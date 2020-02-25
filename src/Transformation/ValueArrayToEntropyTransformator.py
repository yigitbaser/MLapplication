"""
Transformator. For other options see:
https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
"""
from typing import Optional
import numpy as np

from src.Transformation.BaseTransformator import BaseTransformator


class ValueArrayToEntropyTransformator(BaseTransformator):  # type:ignore
    """
    Computes the entropy for an array of values.
    ASSUMES NON ZERO VALUES.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "np.ndarray",
            "output_type": "np.float64"
        }
        BaseTransformator.__init__(self, name="ValueArrayToEntropy", description=d)

    @staticmethod
    def _transform(array: np.ndarray, sample_size: Optional[int]) -> np.float:
        """
        It calculates the entropy based on probability. It normalizes the entropy range to [0,1].
        ASSUMES NON ZERO VALUES.
        :param sample_size: Integer. Size of the dense timeseries. If none, it will take the length
        of the array.
        :param array: np.array. Array of values of a sparse timeseries.
        :return: Float. Normalized entropy value. In case of the presence of zero values in the
        value array, it will return Nan.
        """
        if sample_size is None:
            sample_size = len(array)

        if sample_size > 1:
            norm_prob = np.true_divide(array, sum(array))
            log_norm_array = np.log(norm_prob)
            sum_product = sum(np.multiply(norm_prob, log_norm_array))
            norm_factor = np.reciprocal(np.log(sample_size))
            norm_entropy = - np.multiply(norm_factor, sum_product)
        else:
            norm_entropy = 0

        return norm_entropy

    # pylint: disable=arguments-differ
    def fit(self, array: np.ndarray, sample_size: Optional[int] = None) -> None:
        pass

    def fit_predict(self, array: np.ndarray, sample_size: Optional[int] = None) -> np.float:
        return self._transform(array, sample_size)

    def predict(self, array: np.ndarray, sample_size: Optional[int] = None) -> np.float:
        return self._transform(array, sample_size)
    # pylint: enable=arguments-differ
