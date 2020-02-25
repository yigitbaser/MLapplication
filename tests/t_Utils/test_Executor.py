"""
Tester
"""
from typing import Dict, Any, List, Tuple

import pytest

import src.Utils.Executor as E


class BaseMy():
    """
    Base class for testing classes.
    """

    def __init__(self, class_type: str) -> None:
        self.class_type = class_type
        self.report: Dict[str, Any] = {}

    def get_report(self) -> Dict[str, Any]:
        """
        Returns the dict of report.
        :return: Dict[str, Any].
        """
        return self.report

    def get_class_type(self) -> str:
        """
        Returns class type.
        """
        return self.class_type


class MySum(BaseMy):
    """
    Transformator for sum.
    """

    def __init__(self) -> None:
        BaseMy.__init__(self, "Transformator")

    @staticmethod
    def fit_predict(x: float, y: float) -> float:
        """
        Sum of two numbers.
        :param x: float.
        :param y: float.
        :return: float.
        """
        return x + y


class MyNeg(BaseMy):
    """
    Transformator for multiplication by one.
    """

    def __init__(self) -> None:
        BaseMy.__init__(self, "Transformator")

    @staticmethod
    def fit_predict(x: float) -> float:
        """
        Multiply by -1.
        :param x: float
        :return: float
        """
        return -x


class MyMul(BaseMy):
    """
    Transformator for multiplication.
    """

    def __init__(self) -> None:
        BaseMy.__init__(self, "Transformator")

    @staticmethod
    def fit_predict(x: float, y: float, z: float) -> float:
        """
        Multiply two numbers
        :param x: float.
        :param y: float.
        :return: float.
        """
        return x * y * z


NO_PARAM_QUEUE_DATA = [1.0]
NO_PARAM_QUEUE: List[Tuple[Any, Dict[str, Any]]] = [
    (MyNeg(), {})
]
NO_PARAM_QUEUE_OUTPUT = [-1.0]

EMPTY_QUEUE_DATA = [1.0]
EMPTY_QUEUE: List[Tuple[Any, Dict[str, Any]]] = []
# OUTPUT IS THE SAME AS INPUT

MIX_QUEUE_DATA = [0.0]
MIX_QUEUE: List[Tuple[Any, Dict[str, Any]]] = [
    (MySum(), {"y": 10.0}),
    (MyNeg(), {}),
    (MyMul(), {"y": 5.0, "z": 7.0})
]
MIX_QUEUE_OUTPUT = [-350.0]


@pytest.mark.parametrize("data, queue, queue_output",  # type:ignore
                         [
                             (NO_PARAM_QUEUE_DATA, NO_PARAM_QUEUE, NO_PARAM_QUEUE_OUTPUT),
                             (EMPTY_QUEUE_DATA, EMPTY_QUEUE, EMPTY_QUEUE_DATA),
                             (MIX_QUEUE_DATA, MIX_QUEUE, MIX_QUEUE_OUTPUT)
                         ])
def test_execution(data: List[float], queue: List[Tuple[Any, Dict[str, Any]]], \
                   queue_output: float) -> None:
    """
    Test equality of input and output of series of queues within Executor class.
    :param data: List[float]. List of one value.
    :param queue: List[Tuple[Any, Dict[str, Any]]]. List of tuples of class instances and
    parameter disctinory (for more infor see the docstring of Executor.
    :param queue_output: List[float]. List of one value
    :return:
    """
    executor = E.Executor()
    out = executor.execute(data, queue)

    assert queue_output == out
