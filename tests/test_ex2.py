import pytest

# All fixtures have scope argument with available values:
#    function ->  run once per test
#    class    ->  run once per class of tests
#    module   ->  run once per module
#    session  ->  run once per session

# we want to tell fixture runs over multiple tests
# define fixture as module or session by adding scope
@pytest.fixture(scope='session') # or scope='module'
def fixture_1():
    print('run-fixture-1')
    return 1

def test_example_1(fixture_1):
    print('run-example-1')
    num = fixture_1
    assert num == 1 

# def test_example_2(fixture_1):
#     print('run-example-2')
#     num = fixture_1
#     assert num == 1 