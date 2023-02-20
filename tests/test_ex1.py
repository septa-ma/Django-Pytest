import pytest

# @pytest.mark.ship # a decorator for skipping a test
# @pytest.mark.slow # a decorator for running a test slow
def test_example1():
    print("test1")
    assert 1 == 1 

# @pytest.mark.xfail # a decorator for checking if a test is fail or not
def test_example2():
    assert 1 == 1