"""
Transformator
"""
from pandas import DataFrame

from src.Transformation.BaseTransformator import BaseTransformator


class NumberToOneTransformator(BaseTransformator):  # type:ignore
    """
    Transforms values of selected attribute of a Data frame into ones.
    """

    def __init__(self) -> None:
        d = {
            "input_type": "pd.DataFrame",
            "output_type": "pd.DataFrame"
        }
        BaseTransformator.__init__(self, name="NumberToOne", description=d)

    @staticmethod
    def _transform(X: DataFrame, attr_name: str) -> DataFrame:
        """
        Transforms values of selected attribute of a Data frame into ones.
        :param X: DataFrame. Data frame with Data.
        :param attr_name: String. Name of attribute to be transformed.
        :return: DataFrame.
        """
        X[attr_name] = [1] * X.shape[0]

        return X

    # pylint: disable=arguments-differ
    def fit(self, X: DataFrame, attr_name: str) -> None:
        pass

    def fit_predict(self, X: DataFrame, attr_name: str) -> DataFrame:
        return self._transform(X, attr_name)

    def predict(self, X: DataFrame, attr_name: str) -> DataFrame:
        return self._transform(X, attr_name)
    # pylint: enable=arguments-differ
