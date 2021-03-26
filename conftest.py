import pytest


@pytest.fixture()
def test_list():
    list_1 = ['b', 'a', 'w', 'c']
    yield list_1


@pytest.fixture()
def test_set():
    set_1 = ['b', 'a', 'w', 'c', 'a', 'c']
    yield set(set_1)


@pytest.fixture()
def test_dictionary():
    dic_1 = dict(f_name='ivan', s_name='test', login='abc')
    yield dic_1
