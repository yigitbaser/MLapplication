"""
Sample code for automated notebook run.
"""

from src.Utils.NotebookRunner import NotebookRunner

N_S = [10, 20, 30]
A_S = [1, 2, 3]
BASE_PATH_INPUT = "C:/=MyRep=/MLTemplate/notebooks/template/"
INPUT_NOTEBOOK_NAME = "TemplateParameterizedNotebook"
BASE_PATH_OUTPUT = "C:/=MyTemp=/"
OUTPUT_NOTEBOOK_NAME = "Test"

for i, _ in enumerate(N_S):
    NotebookRunner.run_parametrized_notebook(
        {"n": N_S[i], "a": A_S[i], "b": 0},
        BASE_PATH_INPUT + INPUT_NOTEBOOK_NAME + ".ipynb",
        BASE_PATH_OUTPUT + OUTPUT_NOTEBOOK_NAME + str(i) + ".ipynb",
        convert_to_html=True
    )
