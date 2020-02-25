"""
Benchmarker

This module is a benchmark that requires you to import the function to be tested (as its
arguments if it has). It can also be run with make cronus (instead of executing the test in
PyCharm). More information can be found in: https://pypi.org/project/pytest-benchmark/
"""

# TODO - Create backlog of tests

# As an example for a specific function: import src.Data.FloatTripletGenerator as F

from typing import Any

import pytest

VAR_A = 10
VAR_B = 5


def _first_function_to_be_tested(var_a: int, var_b: int) -> int:
    # Above include the arguments required for running the function you want to test.
    # As an example for a specific function: ftg = F.FloatTripletGenerator()
    # As an example for a specific function: ftg.generate_sample_triplet_df(data_type=data_type)
    return var_a + var_b


def _second_function_to_be_tested(var_a: int, var_b: int) -> int:
    return var_a * var_b


# If you want, you can parametrize with a fixture.
# If you want, you can set per-test option. Remember to APPLY it to BOTH TESTS. To do so type
# @pytest.mark.benchmark() (remember to import pytest) and include in the command line as in here:
# https://pytest-benchmark.readthedocs.io/en/stable/usage.html#commandline-options

@pytest.mark.benchmark(  # type:ignore
    min_time=0.000005,
    max_time=1.0,
    min_rounds=10,
    warmup=True,
    warmup_iterations=10000
)
def test_first_timing(benchmark: Any) -> None:
    """
    Test for timing the first function.
    Arguments MUST be passed directly as below (straight into the benchmark function, after the
    function to be tested) and MUST NOT be passed through the arguments of this test function.
    To execute the benchmark you ONLY have to change the arguments in the code line below.
    :param benchmark: Any. Pytest plugin for benchmarking.
    """
    benchmark(_first_function_to_be_tested, VAR_A, VAR_B)


@pytest.mark.benchmark(  # type:ignore
    min_time=0.000005,
    max_time=1.0,
    min_rounds=10,
    warmup=True,
    warmup_iterations=10000
)
def test_second_timing(benchmark: Any) -> None:
    """
    Test for timing the second function.
    Arguments MUST be passed directly as below (straight into the benchmark function, after the
    function to be tested) and MUST NOT be passed through the arguments of this test function.
    To execute the benchmark you ONLY have to change the arguments in the code line below.
    :param benchmark: Any. Pytest plugin for benchmarking.
    """
    benchmark(_second_function_to_be_tested, VAR_A, VAR_B)
