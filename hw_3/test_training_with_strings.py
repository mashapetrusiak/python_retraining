from training_with_strings import *
import pytest


@pytest.mark.parametrize("test_string, size_n, expected_output", [("", 3, ""),
                                                                  ("123", 4, ""),
                                                                  ("123456", 2, ["12", "34", "56"]),
                                                                  ("12345", 3, ["123", "45"])
                                                                  ]
                         )
def test_splited_string(test_string, size_n, expected_output):
    res = splited_string(test_string, size_n)
    assert res == expected_output


@pytest.mark.parametrize("test_string, size_n, expected_output", [("", 3, ""),
                                                                  ("123", 4, ""),
                                                                  ("123456", 2, ["12", "34", "56"]),
                                                                  ("12345", 3, ["123"])
                                                                  ]
                         )
def test_filtered_result(test_string, size_n, expected_output):
    res = filtered_result(test_string, size_n)
    assert res == expected_output


@pytest.mark.parametrize("test_input, expected_output", [("234", False), ("", True), ("246", True)])
def test_check_sum_of_cube(test_input, expected_output):
    res = check_sum_of_cube(test_input)
    assert res == expected_output


@pytest.mark.parametrize("test_string, n, expected_output", [("1234", 1, "2341")])
def test_rotate(test_string, n, expected_output):
    res = rotate(test_string, n)
    assert res == expected_output


@pytest.mark.parametrize("test_string, size_n, expected_output", [("123456987654", 6, "234561876549"),
                                                                  ("123456987653", 6, "234561356789"),
                                                                  ("66443875", 4, "44668753"),
                                                                  ("66443875", 8, "64438756"),
                                                                  ("66443876 9", 8, "67834466"),
                                                                  ("123456779", 8, "23456771"),
                                                                  ("", 8, ""),
                                                                  ("123456779", 0, ""),
                                                                  ("563000655734469485", 4, "0365065073456944")
                                                                  ]
                         )
def test_converting_of_elements(test_string, size_n, expected_output):
    res = converting_of_elements(test_string, size_n)
    assert res == expected_output
