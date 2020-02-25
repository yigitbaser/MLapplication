"""
Exception
"""

from src.Exception.CustomException import CustomException


class EstimationCustomException(CustomException): # type:ignore
    """
    Exception for message group.
    """

    def __init__(self) -> None:
        CustomException.__init__(self, "Estimation.")


class NoModelSet(EstimationCustomException):
    """
    Exception for no model for message.
    """

    def __init__(self, description: str = "No model is set.") -> None:
        super(NoModelSet, self).__init__()
        self.code = 201
        self.description = description


class ModelTeachedYet(EstimationCustomException):
    """
    Exception for model being taught already.
    """

    def __init__(self, description: str = "Model was teached yet.") -> None:
        super(ModelTeachedYet, self).__init__()
        self.code = 202
        self.description = description


class OutOfParamLevels(EstimationCustomException):
    """
    Exception for not fitting the param levels.
    """

    def __init__(self, description: str = "The Data size does not fit any param level.") -> None:
        super(OutOfParamLevels, self).__init__()
        self.code = 203
        self.description = description
