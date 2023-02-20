import pytest

@pytest.fixture
def yeild_fixture():
    print('start a test')
    yield 5
    print('end a test')

def test_example(yeild_fixture):
    print('run example')
    num = yeild_fixture
    assert num == 5