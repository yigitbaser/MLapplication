"""
Splitter
"""
from configparser import ConfigParser
from typing import Union, Tuple

import numpy as np
from pandas import Series
from sklearn.model_selection import train_test_split

from src.Utils.ConfigHandler import ConfigHandler


class Splitter(ConfigHandler): # type:ignore
    """
    Splits Data into training and testing set for classic X, Y set and for time series.
    """

    def __init__(self, config: Union[None, ConfigParser] = None) -> None:
        super(Splitter, self).__init__(config)

    def cv_split(self, X: np.ndarray, Y: np.ndarray, cv_train_size: Union[None, float] = None,
                 cv_random_state: Union[None, int] = None) \
            -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Splits X, Y into training and testing sets.
        :param X: np.ndarray. Input variable.
        :param Y: np.ndarray. Output variable - SHOULD BE TWO DIMENSION
        :param cv_train_size: Union[None, float]. Size of the training set - between 0,1
        :param cv_random_state: Union[None, int]. Random number for splitting.
        :return: np.ndarrrays. X_train, X_test, Y_train, Y_test.
        """
        if cv_train_size is None:
            cv_train_size = \
                self.try_get_config_value("df_model_validation", "cv_train_size", float)
        if cv_random_state is None:
            cv_random_state = \
                self.try_get_config_value("df_model_validation", "cv_random_state", int)

        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y,
            train_size=cv_train_size,
            random_state=cv_random_state
        )

        return X_train, X_test, Y_train, Y_test

    def time_series_cv_split(self, ts: Series, cv_train_size: Union[None, float] = None) -> \
            Tuple[Series, Series]:
        """
        Splits time series, actually gets first cv_train_size and the rest, no randomness.
        :param ts: Series. Time series.
        :param cv_train_size: Union[None, float]. Size of the training set - between 0,1.
        :return: Tuple[Series, Series]. ts_train, ts_test.
        """
        if cv_train_size is None:
            cv_train_size = \
                self.try_get_config_value("df_model_validation", "cv_train_size", float)
        ts_train = ts[:int(len(ts) * cv_train_size)]
        ts_test = ts[int(len(ts) * cv_train_size):]
        return ts_train, ts_test
