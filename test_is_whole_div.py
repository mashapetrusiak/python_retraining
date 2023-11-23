from first_task import is_whole_div
import pytest


@pytest.mark.parametrize("test_input_divided, test_input_divisor", [(12, 3), (1, 1), (50, 10)])
def test_is_whole_div_positive(test_input_divided, test_input_divisor):
    res = is_whole_div(test_input_divided, test_input_divisor)
    assert res == True


@pytest.mark.parametrize("test_input_divided, test_input_divisor", [(12, 7), (1, 2), (7, 2)])
def test_is_whole_div_negative(test_input_divided, test_input_divisor):
    res = is_whole_div(test_input_divided, test_input_divisor)
    assert res == False
