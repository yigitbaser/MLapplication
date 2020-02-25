"""
Exception
"""


class CustomException(Exception):
    """
    Parent class for all transformers to ensure the same interface.
    """

    def __init__(self, group_name: str) -> None:
        """
        Sets up the parameters.
        :param group_name: str. Name of the group of exceptions.
        """
        Exception.__init__(self)

        self.group_name = group_name
        self.code: int = 0  # Code of the exception.
        self.description: str = ""  # Description of the exception.

    def __str__(self) -> str:
        """
        Overrides the print method.
        :return: str. The descritpion of the exception
        """
        return str(self.code) + " " + self.group_name + " " + self.description
