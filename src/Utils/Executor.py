"""
Executor
"""
from typing import Tuple, Dict, Any, List

from src.Exception.TDDException import NoProperOptionInIf


class Executor():
    """
    Class for executing transformators and other classes.
    """

    def __init__(self) -> None:
        self.class_type = "Executor"
        self.name = "Executor"
        self.report: Dict[str, Any] = {}

    def get_report(self) -> Dict[str, Any]:
        """
        Returns reporter.
        :return: Dict[str, Any]
        """
        return self.report

    @staticmethod
    def execute(data: List[float], queue: List[Tuple[Any, Dict[str, Any]]]) -> List[float]:
        """
        Executes the classes (Transformers, models, ...) with proposed params, starting with Data.
        See doctest for more.
        :param data: List[Any]. List of Data necessary for running. At the first place for
        transformators.
        :param queue: List[Tuple[Any, Dict[str, Any]]. List of tuples.
        instances on the first place, parameters on the other.
        :return: List[Any]. List of return values.
        """
        for worker, params in queue:
            if worker.get_class_type() == "Transformator":
                data[0] = worker.fit_predict(data[0], **params)
            else:
                raise NoProperOptionInIf

        return data
