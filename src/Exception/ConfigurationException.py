"""
Exception
"""

from src.Exception.CustomException import CustomException


class ConfigurationCustomException(CustomException): # type:ignore
    """
    Exception for configuration group.
    """

    def __init__(self) -> None:
        CustomException.__init__(self, "Configuration.")


class NoSectionException(ConfigurationCustomException):
    """
    Exception for no section.
    """

    def __init__(self, description: str = "No section of that name found.") -> None:
        super(NoSectionException, self).__init__()
        self.code = 401
        self.description = description


class ValueTypeException(ConfigurationCustomException):
    """
    Exception for not valid Data type.
    """

    def __init__(self, description: str = "Type is not valid.") -> None:
        super(ValueTypeException, self).__init__()
        self.code = 402
        self.description = description
