"""
Tester
"""

from typing import Tuple

import numpy as np

import src.Data.Splitter as S


def _get_X_Y() -> Tuple[np.ndarray, np.ndarray]:
    X = np.ndarray([10, 2])
    X[:, 0] = range(1, 11)
    X[:, 1] = [10 * i for i in range(1, 11)]

    Y = np.ndarray([10, 1])
    Y[:, 0] = [100 * i for i in range(1, 11)]

    return X, Y


def test_split_sizes() -> None:
    """
    Tests if the shape of youtput files corresponds to splitting criteria.
    """
    split = S.Splitter()
    X, Y = _get_X_Y()
    X_train, X_test, Y_train, Y_test = split.cv_split(
        X=X, Y=Y, cv_train_size=0.8, cv_random_state=9876
    )
    assert X_train.shape == (8, 2) and X_test.shape == (2, 2) and \
           Y_train.shape == (8, 1) and Y_test.shape == (2, 1)


def test_identity_of_input_and_output() -> None:
    """
    Tests Data preservation.
    """
    split = S.Splitter()
    X, Y = _get_X_Y()
    X_train, X_test, Y_train, Y_test = split.cv_split(
        X=X, Y=Y, cv_train_size=0.6, cv_random_state=987687
    )

    X_out = np.concatenate((X_train, X_test), axis=0)
    X_out = np.sort(X_out, axis=0)

    Y_out = np.concatenate((Y_test, Y_train), axis=0)
    Y_out = np.sort(Y_out, axis=0)

    assert np.array_equal(X, X_out) and np.array_equal(Y, Y_out)
