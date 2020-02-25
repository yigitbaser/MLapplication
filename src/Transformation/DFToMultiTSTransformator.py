"""
Transformer
"""
from pandas import DataFrame

from src.Transformation.BaseTransformator import BaseTransformator


class DFToMultiTSTransformator(BaseTransformator):  # type:ignore
    """
    Transforms Data frame with three attributes (id, timestamp, value)
    to Data frame with two attributes (id - unique/grouped, ts).
    Ts consists of a list of tuples (timestamp, value).
    """

    def __init__(self) -> None:
        d = {
            "input_type": "pd.DataFrame",
            "output_type": "pd.DataFrame"
        }
        BaseTransformator.__init__(self, name="DFToMultiTS", description=d)

    @staticmethod
    def _transform(df: DataFrame, attr_groupby: str, attr_time: str, attr_value: str) \
            -> DataFrame:
        """
        Perform the transformation.
        :param df: DataFrame.
        :param attr_groupby: str. Attribute for grouping values with.
        :param attr_time: str. Attribute for time.
        :param attr_value: str. Attribute for value
        :return: DataFrame. Rows are ids from atr_groupby. Value ids and TS of type (time, value).
        """
        df_res = df.groupby(
            by=attr_groupby,
            as_index=True
        )[[attr_time, attr_value]].apply(lambda r: list(map(tuple, r.values.tolist())))
        df_res = df_res.to_frame()
        df_res.reset_index(inplace=True)
        df_res.columns = [attr_groupby, "TS_" + attr_value]

        return df_res

    # pylint: disable=arguments-differ
    def fit(self, df: DataFrame, attr_groupby: str, attr_time: str, attr_value: str) \
            -> None:
        pass

    def fit_predict(self, df: DataFrame, attr_groupby: str, attr_time: str, attr_value: str) \
            -> DataFrame:
        return self._transform(df, attr_groupby, attr_time, attr_value)

    def predict(self, df: DataFrame, attr_groupby: str, attr_time: str, attr_value: str) \
            -> DataFrame:
        return self._transform(df, attr_groupby, attr_time, attr_value)
    # pylint: enable=arguments-differ
