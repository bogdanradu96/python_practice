import pytest

from utils import membership_check


@pytest.mark.parametrize(
    "creation_date, duration, test_date, expected_message",
    [
        ("2024-01-01", 30, "2024-01-31", "Your membership has expired"),  # Expired case
        ("2024-01-01", 30, "2024-01-15", "Your membership is still available and you have 16 days left."),  # Still valid
        ("2024-01-01", 60, "2024-01-31", "Your membership is still available and you have 30 days left."),  # Still Valid
        ("2024-01-01", 30, "2024-01-30", "Your membership is still available and you have 1 days left."),  # 1 day left
        ("2024-01-01", 0, "2024-01-01", "Your membership has expired"),  # Expired immediately
    ],
)
def test_membership_check(creation_date, duration, test_date, expected_message):
    message = membership_check(creation_date, duration, test_date)
    assert message == expected_message