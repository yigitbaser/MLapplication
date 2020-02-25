"""
Tester
"""

import datetime
from typing import Tuple

from pandas import DataFrame

import src.Data.TimeSeriesGenerator as G
import src.Transformation.DFToMultiTSTransformator as T
from src.GlobalConstants import ATTR_ID, ATTR_TIME, ATTR_VALUE, ATTR_TIMESERIES


def _get_df(attr_id: str = ATTR_ID, attr_time: str = ATTR_TIME,
            attr_value: str = ATTR_VALUE) -> Tuple[DataFrame, DataFrame]:
    """
    To get the dataframes before, df_in, and after, df_out,
    the transformation to a time series for testing.
    :return: A tuple of two DataFrames.
    """
    tsg = G.TimeSeriesGenerator()
    t = T.DFToMultiTSTransformator()

    df_in = tsg.generate_sample_triplet_df()

    df_out = t.fit_predict(
        df_in,
        attr_id,
        attr_time,
        attr_value
    )

    return df_out, df_in


def test_df_shape(attr_id: str = ATTR_ID) -> None:
    """
    To test the shape of the output time series.
    """
    df_out, df_in = _get_df()
    assert df_out.shape == (len(df_in[attr_id].unique()), 2)


def test_df_date_type(attr_timeseries: str = ATTR_TIMESERIES) -> None:
    """
    To test the Data type of the output time series.
    """
    df_out, _ = _get_df()
    assert isinstance(
        df_out[attr_timeseries][0][0],
        tuple
    ) and isinstance(
        df_out[attr_timeseries][0][0][0],
        datetime.datetime
    )


def test_df_names(attr_timeseries: str = ATTR_TIMESERIES) -> None:
    """
    To test that the attr names are the columns of the output time series DataFrame.
    """
    df_out, _ = _get_df()
    assert df_out.columns[0] == ATTR_ID and df_out.columns[1] == attr_timeseries


def test_length_ts_values(attr_id: str = ATTR_ID, attr_timeseries: str = ATTR_TIMESERIES) -> None:
    """
    To test that unique values are preserved during the transformation.
    """
    df_out, _ = _get_df()
    assert len(list((df_out.loc[df_out[attr_id] == 10][attr_timeseries]))[0]) == 1


def test_data_conservation_after_transformation(attr_timeseries: str = ATTR_TIMESERIES) -> None:
    """
    To test that Data is conserved along the transformation.
    """
    df_out, df_in = _get_df()
    entries = sum(df_out[attr_timeseries].apply(len))
    assert entries == df_in.shape[0]
