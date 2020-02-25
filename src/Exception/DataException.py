"""
Exception
"""

from src.Exception.CustomException import CustomException


class DataCustomException(CustomException): # type:ignore
    """
    Exception for Data group.
    """

    def __init__(self) -> None:
        CustomException.__init__(self, "Data.")


class NoData(DataCustomException):
    """
    Exception for do Data for selected query.
    """

    def __init__(self, description: str = "No Data in database for selected query.") -> None:
        super(NoData, self).__init__()
        self.code = 101
        self.description = description


class NotEnoughData(DataCustomException):
    """
    Exception for not enought observation.
    """

    def __init__(self, description: str = "Not enough number of observations.") -> None:
        super(NotEnoughData, self).__init__()
        self.code = 102
        self.description = description


class NoResponseVariable(DataCustomException):
    """
    Exception for not response variable.
    """

    def __init__(self, description: str = \
            "No response variable/there are only zeros in response varible.") -> None:
        super(NoResponseVariable, self).__init__()
        self.code = 103
        self.description = description


class NotEnoughResponseVariable(DataCustomException):
    """
    Exception for not enough nonzero values.
    """

    def __init__(self, description: str = "Not enough nonzero values in response variable.") \
            -> None:
        super(NotEnoughResponseVariable, self).__init__()
        self.code = 104
        self.description = description


class NotPositiveNumber(DataCustomException):
    """
    Exception for not positive number.
    """

    def __init__(self, description: str = "Not positive number.") -> None:
        super(NotPositiveNumber, self).__init__()
        self.code = 105
        self.description = description


class NoConfigFile(DataCustomException):
    """
    Exception for not having a config file.
    """

    def __init__(self, description: str = "No config file.") -> None:
        super(NoConfigFile, self).__init__()
        self.code = 106
        self.description = description
