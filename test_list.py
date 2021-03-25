import pytest


class TestListClass:

    # list_1 = ['a', 'b', 'c']
    @pytest.fixture()
    def test_list(self):
        list_1 = ['b', 'a', 'w', 'c']
        yield list_1

    @pytest.mark.parametrize("data_test", ['d'])
    @pytest.mark.parametrize("valid_assert", [['b', 'a', 'w', 'c', 'd']])
    def test_append(self, test_list, data_test, valid_assert):
        test_list.append(data_test)
        assert test_list == valid_assert

    @pytest.mark.parametrize("data_test", [[1, 2, 3]])
    @pytest.mark.parametrize("valid_assert", [['b', 'a', 'w', 'c', 1, 2, 3]])
    def test_extend(self, test_list, data_test, valid_assert):
        test_list.extend(data_test)
        assert test_list == valid_assert

    @pytest.mark.parametrize("data_test", ['www'])
    @pytest.mark.parametrize("valid_assert", [['b', 'a', 'w', 'www', 'c']])
    def test_insert(self, test_list, data_test, valid_assert):
        test_list.insert(3, data_test)
        assert test_list == valid_assert

    @pytest.mark.parametrize("valid_assert", [['a', 'b', 'c', 'w']])
    def test_sort(self, test_list, valid_assert):
        test_list.sort()
        assert test_list == valid_assert

    @pytest.mark.parametrize("valid_assert", [['c', 'w', 'a', 'b']])
    def test_reverse(self, test_list, valid_assert):
        test_list.reverse()
        assert test_list == valid_assert
