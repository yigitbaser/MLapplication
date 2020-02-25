"""
Testing
"""

from typing import Tuple, Any

import pandas as pd
import pytest
from pandas import DataFrame

import src.Transformation.NumberToOneTransformator as T
from src.GlobalConstants import ATTR_ID, ATTR_VALUE, FP, P

TRANSF_TYPE = (FP, P)


def _generate_data(attr_id: str = ATTR_ID, attr_value: str = ATTR_VALUE) \
        -> Tuple[DataFrame, DataFrame]:
    df_val = pd.DataFrame()
    df_ground_true = pd.DataFrame()

    df_val[attr_id] = [10, 20, 30, 40]
    df_ground_true[attr_id] = df_val[attr_id]

    df_val[attr_value] = [40, 43, 890, 10]
    df_ground_true[attr_value] = [1, 1, 1, 1]

    return df_val, df_ground_true


def _transform_df(df: DataFrame, transformation_type: str, attr_value: str = ATTR_VALUE,
                  transf_type: Tuple[str, str] = TRANSF_TYPE) -> DataFrame:
    t = T.NumberToOneTransformator()

    if transformation_type == transf_type[0]:
        transformed_data = t.fit_predict(df, attr_value)
    elif transformation_type == transf_type[1]:
        transformed_data = t.predict(df, attr_value)

    return transformed_data


@pytest.mark.parametrize("transformation_type", [FP, P])  # type:ignore
def test_transform(transformation_type: str) -> Any:
    """
    Tests transformations.
    :param transformation_type: str. F for "f" (fit), P for "p" (predict)
    and FP for "fp (fit_predict).
    :return: bool. Result of comparison.
    """
    df_val, df_ground_truth = _generate_data()
    df_test = _transform_df(df_val, transformation_type)

    return df_test.equals(df_ground_truth)
