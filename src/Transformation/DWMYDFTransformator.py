"""
Transformator
"""
from pandas import DataFrame

from src.Transformation.BaseTransformator import BaseTransformator
from src.Transformation.DWMYTransformator import DWMYTransformator


class DWMYDFTransformator(BaseTransformator):  # type:ignore
    """
    Transforms selected attributes of Data frame time format.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "",
            "output_type": ""
        }
        self.t = DWMYTransformator()
        BaseTransformator.__init__(self, "DWMYDF", d)

    def _transform(self, df: DataFrame, time_type: str, attr_name: str) -> DataFrame:
        """
        Transforms selected attributes of Data frame time format.
        :param df: DataFrame. Original Data frame.
        :param time_type: str. "d", "w", "m", "y"
        :param attr_name: str. name of attribute.
        :return: DataFrame
        """
        df[attr_name + "_" + time_type] = self.t.fit_predict(df[attr_name].array, time_type)
        df = df.drop([attr_name], axis=1)
        df = df.reset_index(drop=True)

        return df

    # pylint: disable=arguments-differ
    def fit(self, df: DataFrame, time_type: str, attr_name: str) -> None:
        pass

    def fit_predict(self, df: DataFrame, time_type: str, attr_name: str) -> DataFrame:
        return self._transform(df, time_type, attr_name)

    def predict(self, df: DataFrame, time_type: str, attr_name: str) -> DataFrame:
        return self._transform(df, time_type, attr_name)
    # pylint: enable=arguments-differ
