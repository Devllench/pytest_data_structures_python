import pytest


class TestDictionaryClass:

    # list_1 = ['a', 'b', 'c']
    @pytest.fixture()
    def test_dictionary(self):
        dic_1 = dict(f_name='ivan', s_name='test', login='abc')
        yield dic_1

    @pytest.mark.parametrize("data_test", ['login'])
    @pytest.mark.parametrize("valid_assert", ['abc'])
    def test_get(self, test_dictionary, data_test, valid_assert):
        assert test_dictionary.get(data_test) == valid_assert

    @pytest.mark.parametrize("data_test", ['login'])
    @pytest.mark.parametrize("valid_assert", [{'f_name': 'ivan', 's_name': 'test'}])
    def test_keys(self, test_dictionary, data_test, valid_assert):
        test_dictionary.pop(data_test)
        assert test_dictionary == valid_assert

    @pytest.mark.parametrize("data_test", ['login'])
    @pytest.mark.parametrize("valid_assert", [{'f_name': 'ivan', 's_name': 'test'}])
    def test_pop(self, test_dictionary, data_test, valid_assert):
        test_dictionary.pop(data_test)
        assert test_dictionary == valid_assert

    @pytest.mark.parametrize("valid_assert", [{'f_name': 'ivan', 's_name': 'test'}])
    def test_popitem(self, test_dictionary, valid_assert):
        test_dictionary.popitem()
        assert test_dictionary == valid_assert

    @pytest.mark.parametrize("data_test", [{'passwd':'login'}])
    @pytest.mark.parametrize("valid_assert", [{'f_name': 'ivan', 'login': 'abc', 'passwd': 'login', 's_name': 'test'}])
    def test_update(self, test_dictionary, data_test, valid_assert):
        test_dictionary.update(data_test)
        assert test_dictionary == valid_assert



