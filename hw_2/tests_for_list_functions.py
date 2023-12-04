from list_comp_task import *
import pytest


@pytest.mark.parametrize("test_input, expected_output", [([1, 2, 3], 3), ([], 0)])
def test_total_amount(test_input, expected_output):
    res = total_amount(test_input)
    assert res == expected_output


@pytest.mark.parametrize("test_input, expected_output", [([1, 2, 2, 3], 3), ([], 0)])
def test_unique_amount(test_input, expected_output):
    res = unique_amount(test_input)
    assert res == expected_output


@pytest.mark.parametrize("test_input, expected_output", [([1, 2, 2, 3], 2), ([], 0)])
def test_once_occure_amount(test_input, expected_output):
    res = once_occure_amount(test_input)
    assert res == expected_output


@pytest.mark.parametrize("test_input, expected_output", [([1, 2, 2, 3], [2]),
                                                         ([1, 1, 1, 2, 3, 4, 4, 4, 5], [1, 4]),
                                                         ([], [])]
                         )
def test_max_occurance_elements(test_input, expected_output):
    res = max_occurance_elements(test_input)
    assert res == expected_output


@pytest.mark.parametrize("test_input, expected_output", [([1, 2, 2, 3], [2]),
                                                         ([1, 1, 1, 2, 3, 4, 4, 4, 4, 4, 5], [5])])
def test_max_occurance(test_input, expected_output):
    res = max_occurance(test_input)
    assert res == expected_output


@pytest.mark.parametrize("test_input, expected_output", [([1, 2, 2, 3], [[2], [2]]),
                                                         ([1, 1, 1, 2, 3, 4, 4, 4, 4, 4, 5], [[4], [5]])
                                                         ]
                         )
def test_make_list_4_and_5(test_input, expected_output):
    res = make_list_4_and_5(test_input)
    assert res == expected_output


@pytest.mark.parametrize("test_input, expected_output", [([1, 2, 2, 3], [4, 3, 2, [[2],[2]]]),
                                                         ([1, 1, 1, 2, 3, 4, 4, 4, 4, 4, 5], ([11, 5, 3, [[4], [5]]]))
                                                         ]
                         )
def test_stat(test_input, expected_output):
    res = stat(test_input)
    assert res == expected_output
