"""
Sample code for automated notebook run.
"""
# pylint: disable=too-few-public-methods
# pylint: enable=too-few-public-methods
import os
from typing import Dict, Any
import papermill as pm


class NotebookRunner():
    """
    Automatically runs a notebook
    """

    # pylint: disable=too-few-public-methods
    @staticmethod
    def run_parametrized_notebook(parameters: Dict[str, Any], path_to_notebook: str,
                                  path_to_output: str, convert_to_html: bool = True) -> None:
        """
        Automated run of a notebook. The generated html file will have the same name as specified
        output file.
        :param parameters: Dict. Dictionary of parameters to read the
        :param path_to_notebook: Str. Full path to notebook template.
        :param path_to_output: Str. Full path to save the output.
        :param convert_to_html: Bool. Flag to turn the conversion to html of off.
        :return:
        """
        pm.execute_notebook(path_to_notebook, path_to_output, parameters=parameters)
        if convert_to_html:
            os.system("jupyter nbconvert --to html " + path_to_output)
