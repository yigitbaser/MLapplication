"""
Tester
"""

import src.Data.TimeSeriesGenerator as G


def test_size_day() -> None:
    """
    To test the length of the generated day time series and
    that each element of the list is a tuple.
    """
    tsg = G.TimeSeriesGenerator()
    ts = tsg.generate_day_data()
    assert len(ts) == 30 and len(ts[0]) == 2


def test_size_week() -> None:
    """
    To test the length of the generated week time series and
    that each element of the list is a tuple.
    """
    tsg = G.TimeSeriesGenerator()
    ts = tsg.generate_week_data()
    assert len(ts) == 30 and len(ts[0]) == 2


def test_size_month() -> None:
    """
    To test the length of the generated month time series and
    that each element of the list is a tuple.
    """
    tsg = G.TimeSeriesGenerator()
    ts = tsg.generate_month_data()
    assert len(ts) == 30 and len(ts[0]) == 2


def test_size_year() -> None:
    """
    To test the length of the generated year time series and
    that each element of the list is a tuple.
    """
    tsg = G.TimeSeriesGenerator()
    ts = tsg.generate_year_data()
    assert len(ts) == 30 and len(ts[0]) == 2
