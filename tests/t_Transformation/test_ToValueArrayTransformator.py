"""
Tester
"""

from datetime import datetime
from typing import List, Union, Tuple

import pytest
from numpy import array_equal, ndarray

import src.Transformation.ToValueArrayTransformator as A
from src.GlobalConstants import FP, P
from src.Exception.TDDException import NoProperOptionInIf

LIST_UNIT_INT = [(datetime(2020, 1, 1), 1)]
LIST_UNIT_FLOAT = [(datetime(2020, 1, 1), 1.23)]
LIST_TRIPLET_INT = [(datetime(2020, 1, 1), 1), (datetime(2020, 1, 2), 2),
                    (datetime(2020, 1, 3), 3)]
LIST_TRIPLET_FLOAT = [(datetime(2020, 1, 1), 1.23), (datetime(2020, 1, 2), 2.34),
                      (datetime(2020, 1, 3), 3.45)]

OUTPUT_UNIT_INT = [1]
OUTPUT_UNIT_FLOAT = [1.23]
OUTPUT_TRIPLET_INT = [1, 2, 3]
OUTPUT_TRIPLET_FLOAT = [1.23, 2.34, 3.45]


def _transform(transf_type: str, ts_list: List[Tuple[datetime, Union[int, float]]]) -> ndarray:
    lta = A.ToValueArrayTransformator()
    if transf_type == FP:
        value_array = lta.fit_predict(ts_list)
    elif transf_type == P:
        value_array = lta.predict(ts_list)
    else:
        raise NoProperOptionInIf

    return value_array


@pytest.mark.parametrize("transf_type, ts_list, correct_output", # type:ignore
                         [(FP, LIST_UNIT_INT, OUTPUT_UNIT_INT),
                          (P, LIST_UNIT_INT, OUTPUT_UNIT_INT),
                          (FP, LIST_UNIT_FLOAT, OUTPUT_UNIT_FLOAT),
                          (P, LIST_UNIT_FLOAT, OUTPUT_UNIT_FLOAT),
                          (FP, LIST_TRIPLET_INT, OUTPUT_TRIPLET_INT),
                          (P, LIST_TRIPLET_INT, OUTPUT_TRIPLET_INT),
                          (FP, LIST_TRIPLET_FLOAT, OUTPUT_TRIPLET_FLOAT),
                          (P, LIST_TRIPLET_FLOAT, OUTPUT_TRIPLET_FLOAT)
                          ])
def test_tuple_list_to_array(transf_type: str, ts_list: List[Tuple[datetime, Union[int, float]]],
                             correct_output: List[Union[str, float]]) -> None:
    """
    To compare the transformator's output of a given list of tuples to a defined correct output.
    :param transf_type: String. FP for "fp" (fit-predict), P for "p" (predict).
    :param ts_list: List of tuples of datetime and a numerical value. List of tuples (timestamp,
    value). The values can be either integers or floats.
    :param correct_output: List of tuples (timestamp, integer or float). Correct output of the
    transformation.
    """
    value_array = _transform(transf_type, ts_list)
    assert array_equal(value_array, correct_output)
