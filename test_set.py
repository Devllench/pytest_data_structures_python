import pytest


class TestSetClass:

    @pytest.mark.parametrize("data_test", ['s'])
    @pytest.mark.parametrize("valid_assert", [True])
    def test_isdisjoint(self, test_set, data_test, valid_assert):
        assert test_set.isdisjoint(data_test) == valid_assert

    @pytest.mark.parametrize("data_test", [{'b', 'a', 'w', 'c', 'a', 'c'}])
    @pytest.mark.parametrize("valid_assert", [True])
    def test_append(self, test_set, data_test, valid_assert):
        test_set.issubset(data_test)
        assert test_set.issubset(data_test) == valid_assert

    @pytest.mark.parametrize("data_test", [{'s'}])
    @pytest.mark.parametrize("valid_assert", [{'a', 'b', 'c', 's', 'w'}])
    def test_update(self, test_set, data_test, valid_assert):
        test_set.update(data_test)
        assert test_set == valid_assert

    @pytest.mark.parametrize("data_test", ['w'])
    @pytest.mark.parametrize("valid_assert", [{'a', 'b', 'c'}])
    def test_remove(self, test_set, data_test, valid_assert):
        test_set.remove(data_test)
        assert test_set == valid_assert

    @pytest.mark.parametrize("data_test", ['w'])
    @pytest.mark.parametrize("valid_assert", [set()])
    def test_clear(self, test_set, data_test, valid_assert):
        test_set.clear()
        assert test_set == valid_assert
