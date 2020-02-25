"""
Tester
"""

from datetime import datetime
from typing import List, Optional, Tuple

import numpy as np
import pytest
from pandas import DataFrame

import src.Data.FloatTripletGenerator as F
from src.Exception.TDDException import NoProperOptionInIf
from src.GlobalConstants import ATTR_VALUE, ATTR_TIME

ID_LIST_UNIT = [1]
ID_LIST_FIFTH = [1, 2, 3, 4, 5]
ID_LIST_TENTH = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

SHAPE_UNIT = (1, 3)
SHAPE_FIFTH = (5, 3)
SHAPE_TENTH = (10, 3)


def _generator(data_type: str, data_boundary: Optional[int] = 100,
               id_list: Optional[List[int]] = None) -> DataFrame:
    ftp = F.FloatTripletGenerator()
    df = ftp.generate_sample_triplet_df(data_type, data_boundary, id_list)
    return df


@pytest.mark.parametrize("data_type",  # type:ignore
                         ["ones", "integers", "amount"]
                         )
def test_value_type(data_type: str) -> None:
    """
    To assert that the data_type outputs the correct value (1) or dtype (int, float).
    :param data_type: String. If ones ("ones"), integer ("integers") or float ("amount").
    """
    df = _generator(data_type=data_type)
    if data_type == "ones":
        assert df[ATTR_VALUE].dtype == np.dtype("int64") and df[ATTR_VALUE].sum() == df.shape[0]
    elif data_type == "integers":
        assert df[ATTR_VALUE].dtype == np.dtype("int64")
    elif data_type == "amount":
        assert df[ATTR_VALUE].dtype == float
    else:
        raise NoProperOptionInIf


@pytest.mark.parametrize("data_type, id_list, shape_triplet",  # type:ignore
                         [("ones", ID_LIST_UNIT, SHAPE_UNIT),
                          ("integers", ID_LIST_FIFTH, SHAPE_FIFTH),
                          ("amount", ID_LIST_TENTH, SHAPE_TENTH)]
                         )
def test_shape(data_type: str, id_list: List[int], shape_triplet: Tuple[int, int]) -> None:
    """
    To test that for different id lists we get the proper shape.
    :param data_type: String. If ones ("ones"), integer ("integers") or float ("amount").
    :param id_list: List[int]. list of unique IDs.
    :param shape_triplet: Tuple of two integers. Correct shape of the output triplet.
    """
    df = _generator(data_type=data_type, id_list=id_list)
    assert df.shape == shape_triplet


@pytest.mark.parametrize("data_type",  # type:ignore
                         ["ones", "integers", "amount"]
                         )
def test_time_type(data_type: str) -> None:
    """
    To verify that the ATTR_TIME column is producing datetimes.
    :param data_type: String. If ones ("ones"), integer ("integers") or float ("amount").
    """
    df = _generator(data_type=data_type)
    assert isinstance(df[ATTR_TIME][0], datetime)
