from first_task import to_minutes
import pytest


@pytest.mark.parametrize("test_input, expected_output", [(1, 60), (0, 0), (30, 1800)])
def test_to_minutes(test_input, expected_output):
    res = to_minutes(test_input)
    assert res == expected_output
