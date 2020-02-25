"""
Tester
"""

from typing import Tuple, Generator, Any
from pandas import DataFrame
import pytest

import src.Data.SaverAndLoader as S
import src.Data.TimeSeriesGenerator as G

WHERE_TO_STORE = "raw"
TRIPLET_NAME = "triplet_test"
TIMESERIES_NAME = "timeseries_test"
FILE_NAMES = [TRIPLET_NAME, TIMESERIES_NAME]


def _get_triplet_and_timeseries(
        triplet_name: str = TRIPLET_NAME, timeseries_name: str = TIMESERIES_NAME) \
        -> Tuple[DataFrame, DataFrame]:
    """
    To generate a triplet and a timeseries sample for testing.
    :param triplet_name: String. Name of the generated triplet dataframe.
    :param timeseries_name: String. Name of the generated timeseries dataframe.
    :return: List of DataFrames. Triplet and Timeseries dataframes.
    """
    tsg = G.TimeSeriesGenerator()
    triplet = tsg.generate_sample_triplet_df()
    timeseries = tsg.generate_sample_ts_df()

    triplet.name = triplet_name
    timeseries.name = timeseries_name

    return triplet, timeseries


@pytest.fixture(autouse=True)  # type:ignore # TODO - Add explanation to LearningMaterial repo
def clean_up_pickles() -> Generator[None, None, Any]:  # DON'T provide args with pytest.fixtures.
    # TODO - Fix Mypy error untyped decorator makes function "clean_up_pickles" untyped
    """
    Function to run code before and after each test (autouse=True).
    """
    # Code before running the tests.
    yield  # This is just to mark that tests should run here.
    # Here (and below) is what is executed after the tests.
    sal = S.SaverAndLoader(None)
    for file in FILE_NAMES:
        sal.delete_pkl(file, WHERE_TO_STORE)


def test_triplet_saved_equal_loaded() -> None:
    """
    Test if the saved and loaded triplets are equal.
    """
    sal = S.SaverAndLoader(None)
    triplet, _ = _get_triplet_and_timeseries()
    triplet_attrs = list(triplet.columns)
    sal.save_triplet(triplet, triplet.name, triplet_attrs, WHERE_TO_STORE)
    loaded_triplet = sal.load_triplet(triplet.name, triplet_attrs, WHERE_TO_STORE)
    assert triplet.equals(loaded_triplet)


def test_timeseries_saved_equal_loaded() -> None:
    """
    Test if the saved and loaded timeseries are equal.
    """
    sal = S.SaverAndLoader(None)
    _, timeseries = _get_triplet_and_timeseries()
    timeseries_attrs = list(timeseries.columns)
    sal.save_timeseries(timeseries, timeseries.name, timeseries_attrs, WHERE_TO_STORE)
    loaded_timeseries = sal.load_timeseries(timeseries.name, timeseries_attrs, WHERE_TO_STORE)
    assert timeseries.equals(loaded_timeseries)
