"""
Transformator
"""
from typing import Any, List
from pandas import DataFrame

from src.Transformation.BaseTransformator import BaseTransformator


class DWMYGroupTransformator(BaseTransformator):  # type:ignore
    """
    Transforms Data frame - group values with time and compute a function.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "",
            "output_type": ""
        }
        BaseTransformator.__init__(self, "DWMYDF", d)

    @staticmethod
    def _transform(df: DataFrame, time_type: str, attr_names: List[str], fun: Any) \
            -> DataFrame:
        """
        Transforms Data frame - group values with time and compute a function.
        :param df: DataFrame.
        :param time_type: str. "d", "w", "m", "y"
        :param col_names: List[str, str]. Atribute names - first is time, second value.
        :return:
        """
        atr_time = attr_names[0] + "_" + time_type

        df_res = df.groupby(by=atr_time, as_index=True).apply(fun)
        df_res.drop([atr_time], axis=1, inplace=True)
        df_res.reset_index(level=0, inplace=True)

        return df_res

    # pylint: disable=arguments-differ
    def fit(self, df: DataFrame, time_type: str, attr_names: List[str], fun: Any) -> None:
        pass

    def fit_predict(self, df: DataFrame, time_type: str, attr_names: List[str], fun: Any) \
            -> DataFrame:
        return self._transform(df, time_type, attr_names, fun)

    def predict(self, df: DataFrame, time_type: str, attr_names: List[str], fun: Any) -> DataFrame:
        return self._transform(df, time_type, attr_names, fun)
    # pylint: enable=arguments-differ
