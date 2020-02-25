"""
TODO - add reporting layer
"""
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseTransformator(ABC):
    """
    Parent class for all transformers to ensure the same interface.
    """

    def __init__(self, name: str, description: Dict[str, Any]) -> None:
        self.class_type = "Transformator"
        self.name = name
        self.description = description

    def get_class_type(self) -> str:
        """
        Returns class type description.
        :return: str. Class type destription.
        """
        return self.class_type

    @abstractmethod
    def fit(self) -> None:
        """
        Fit transformation based on the Data - analogy to sklearn style.
        """

    @abstractmethod
    def predict(self) -> Any:
        """
        Do a prediction based on the fitted model - analogy to sklearn style.
        """

    @abstractmethod
    def fit_predict(self) -> Any:
        """
        Connection of fit and predict into one - analogy to sklearn style.
        """
