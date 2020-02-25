# pylint: disable=invalid-name
# pylint: enable=invalid-name
"""
Tester
"""

import numpy as np
import pytest

import src.Transformation.ValueArrayToEntropyTransformator as E
from src.GlobalConstants import FP, P
from src.Exception.TDDException import NoProperOptionInIf

ORDER_INPUT = [5]
CHAOS_INPUT = [5, 5, 5]
ENTROPY_INPUT = [1, 2]
ENTROPY_INPUT_NULL = [1, 0, 2]

ORDER_OUTPUT = 0
CHAOS_OUTPUT = 0.9999999999999998
ENTROPY_OUTPUT = 0.9182958340544894
ENTROPY_OUTPUT_DENSE = 0.1627071638923428

DENSE_SIZE = 50


def _entropy(transf_type: str, array: np.ndarray, sample_size: int) -> np.float:
    vae = E.ValueArrayToEntropyTransformator()
    if transf_type == FP:
        norm_entropy = vae.fit_predict(array, sample_size)
    elif transf_type == P:
        norm_entropy = vae.predict(array, sample_size)
    else:
        raise NoProperOptionInIf
    return norm_entropy


@pytest.mark.parametrize("transf_type, sample_size, array_input, correct_entropy",  # type:ignore
                         [(FP, 1, ORDER_INPUT, ORDER_OUTPUT),
                          (P, 1, ORDER_INPUT, ORDER_OUTPUT),
                          (FP, 3, CHAOS_INPUT, CHAOS_OUTPUT),
                          (P, 3, CHAOS_INPUT, CHAOS_OUTPUT),
                          (FP, 2, ENTROPY_INPUT, ENTROPY_OUTPUT),
                          (P, 2, ENTROPY_INPUT, ENTROPY_OUTPUT),
                          (FP, DENSE_SIZE, ENTROPY_INPUT, ENTROPY_OUTPUT_DENSE),
                          (P, DENSE_SIZE, ENTROPY_INPUT, ENTROPY_OUTPUT_DENSE),
                          ])
def test_entropy(transf_type: str, sample_size: int, array_input: np.ndarray,
                 correct_entropy: float) -> None:
    """
    To corroborate the correct entropy output for a chaotic situation (E=1), complete order (E=0)
    and for a given array of values with a specific sample size n.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param sample_size: Integer. Size of the dense timeseries.
    :param array_input: np.array. Array of values.
    :param correct_entropy: Float. Correct entropy.
    """
    calculated_entropy = _entropy(transf_type, array_input, sample_size)
    assert calculated_entropy == correct_entropy


# Although we assume a sparse array, we want to assert that for a dense array the return is nan.
@pytest.mark.parametrize("transf_type, sample_size, array_input",  # type:ignore
                         [(FP, 3, ENTROPY_INPUT_NULL),
                          (P, 3, ENTROPY_INPUT_NULL)])
def test_null_value(transf_type: str, sample_size: int, array_input: np.ndarray) -> None:
    """
    To check behaviour outside assumptions (only non zero values present in the value array).
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param sample_size: Integer. Size of the dense timeseries.
    :param array_input: np.array. Array of values.
    """
    calculated_entropy = _entropy(transf_type, array_input, sample_size)
    assert np.isnan(calculated_entropy)
