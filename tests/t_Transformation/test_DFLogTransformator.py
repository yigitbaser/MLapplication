"""
Tester
"""

from typing import List, Tuple

import numpy as np
import pytest
from pandas import DataFrame

import src.Data.TimeSeriesGenerator as G
import src.Transformation.DFLogTransformator as L
from src.GlobalConstants import ATTR_ID, ATTR_VALUE, FP, P
from src.Exception.DataException import NotPositiveNumber

BASE = 10
INT_DATA = True
SIZE = 50
ATTR = (ATTR_VALUE, BASE, SIZE)


def _gen_id_list(size: int = SIZE) -> List[int]:
    np.random.seed(123)
    id_list = [np.random.randint(1, 9) for i in range(size - 1)]
    id_list.append(10)  # To add a unique ID, same ID as used in tsg.generate_sample_triplet_df()
    return id_list


def _get_real_numbers_df(size: int = SIZE, positive: bool = True, zero: bool = False,
                         int_data: bool = INT_DATA, attr_name: str = ATTR_VALUE
                         ) -> DataFrame:
    tsg = G.TimeSeriesGenerator()
    df = tsg.generate_sample_triplet_df(id_list=_gen_id_list(size), int_data=int_data)
    non_natural_values = [
        np.random.uniform(0 if positive else -100, 100) for i in range(df.shape[0])
    ]
    df[attr_name] = non_natural_values
    df.loc[df[ATTR_ID] == 10, attr_name] = 101
    while not zero and any(df[attr_name] == 0):
        mask = df[attr_name] == 0
        df.loc[mask, attr_name] = df.loc[mask, attr_name].apply(
            lambda v: np.random.uniform(0, 100)
        )
    return df


def _transform_log_df(df: DataFrame, transformation_type: str,
                      attr_value: str, base: int) -> DataFrame:
    lgthm = L.DFLogTransformator()
    if transformation_type == FP:
        transformed_data = lgthm.fit_predict(df, attr_value, base)
    elif transformation_type == P:
        transformed_data = lgthm.predict(df, attr_value, base)

    return transformed_data


@pytest.mark.parametrize("transformation_type, base", # type:ignore
                         [(FP, 2),
                          (P, 8)]
                         )
def test_log_calculation(transformation_type: str, base: int, attr_name: str = ATTR_VALUE) -> None:
    """
    This test is to check that the logarithms are being correctly calculated.
    :param attr_name: Str. Name of the attribute to have applied on a logarithmic transformation.
    :param transformation_type: Str. Transformation type ("f" for fit, "p" for predict,
    "fp" for fit_predict).
    :param base: Int. Logarithm base.
    """
    df_in = _get_real_numbers_df()
    df_out = _transform_log_df(df_in, transformation_type, attr_name, base)
    df_out[attr_name] = np.power(base, df_out[attr_name])
    df_out[attr_name] = df_out[attr_name] - 1
    assert df_in[attr_name][0] == df_out[attr_name][0]


@pytest.mark.parametrize("transformation_type, size", # type:ignore
                         [(FP, 100),
                          (P, 1000)]
                         )
def test_df_shape(transformation_type: str, size: int,
                  attr_name: str = ATTR_VALUE, base: int = BASE
                  ) -> None:
    """
    To test if the shape of the transformed DataFrame remains unchanged from the input DataFrame.
    :param attr_name: Str. Name of the attribute to have applied on a logarithmic transformation.
    :param base: Int. Base of the logarithm.
    :param transformation_type: Str. Transformation type ("f" for fit, "p" for predict,
    "fp" for fit_predict).
    :param size: Int. Number of rows of the DataFrame.
    """
    df_in = _get_real_numbers_df(size=size)
    df_out = _transform_log_df(df_in, transformation_type, attr_name, base)
    assert df_in.shape == df_out.shape


@pytest.mark.parametrize("transformation_type, positive, single, zero", # type:ignore
                         [(FP, False, 101, False),
                          (P, False, 101, False),
                          (FP, False, 0, True),
                          (P, False, 0, True),
                          (FP, True, 0, False),
                          (P, True, 0, False)]
                         )
def test_negative_null_raise_error(transformation_type: str, positive: bool, single: int,
                                   zero: bool, attr: Tuple[str, int, int] = ATTR
                                   ) -> None:
    """
    To test if a ValueError is raised when negative or null values are located in the column
    to be transformed.
    :param transformation_type: Str. Transformation type ("f" for fit, "p" for predict,
    "fp" for fit_predict).
    :param positive: Bool. False introduces negative values in the DataFrame's column. True only
    generates positive values.
    :param single: Int. To change the value of the unique ID.
    :param zero: Bool. True accepts zero values. False substitute them by a random number (0,100).
    :param attr: Tuple of a String and two Integers. Provides ATTR_NAME, BASE and SIZE.
    """
    with pytest.raises(NotPositiveNumber):
        df_in = _get_real_numbers_df(size=attr[2], positive=positive, zero=zero)
        df_in.loc[df_in[ATTR_ID] == 10, attr[0]] = single  # To test a single null value
        _transform_log_df(df_in, transformation_type, attr[0], attr[1])
