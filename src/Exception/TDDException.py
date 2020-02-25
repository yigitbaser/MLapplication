"""
Exception
"""

from src.Exception.CustomException import CustomException


class TDDException(CustomException): # type:ignore
    """
    Exception for testing group.
    """

    def __init__(self) -> None:
        CustomException.__init__(self, "TDD.")


class NoProperOptionInIf(TDDException):
    """
    Exception for not proper option in if clause.
    """

    def __init__(self, description: str = "Option is not present in the if statement.") -> None:
        super(NoProperOptionInIf, self).__init__()
        self.code = 301
        self.description = description
