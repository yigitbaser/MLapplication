"""
Transformation.
"""
import numpy as np
from pandas import DataFrame

from src.Exception.DataException import NotPositiveNumber
from src.Transformation.BaseTransformator import BaseTransformator


class DFLogTransformator(BaseTransformator):  # type:ignore
    """
    Applies logarithm with the indicated base on a specified attribute of a DataFrame.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "pd.DataFrame",
            "output_type": "pd.DataFrame"
        }
        BaseTransformator.__init__(self, name="DFLog", description=d)

    @staticmethod
    def _transform(df: DataFrame, attr_name: str, base: int) -> DataFrame:
        """
        Performs the logarithmic transformation.
        :param df: DataFrame.
        :param attr_name: str. Name of the attribute to be transformed.
        :param base: int. Base of the logarithm.
        :return: DataFrame. DataFrame.
        """

        if sum(df[attr_name] <= 0) > 0:
            raise NotPositiveNumber

        df[attr_name] = df[attr_name] + 1  # To avoid negative values
        df[attr_name] = df[attr_name].apply(np.log) / np.log(base)
        return df

    # pylint: disable=arguments-differ
    def fit(self, df: DataFrame, attr_name: str, base: int) -> None:
        pass

    def predict(self, df: DataFrame, attr_name: str, base: int) -> DataFrame:
        return self._transform(df, attr_name, base)

    def fit_predict(self, df: DataFrame, attr_name: str, base: int) -> DataFrame:
        return self._transform(df, attr_name, base)
    # pylint: enable=arguments-differ
