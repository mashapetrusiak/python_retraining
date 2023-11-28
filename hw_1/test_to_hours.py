from hw_1.first_task import to_hours
import pytest


@pytest.mark.parametrize("test_input, expected_output", [(12, 0.2), (5, 0.0833), (0, 0)])
def test_to_hours(test_input, expected_output):
    res = to_hours(test_input)
    assert res == expected_output
