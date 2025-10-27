import pytest
from times import time_range, compute_overlap_time

test_cases = [
    (
        # Test Case 1: 'test_times'
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [
            ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
            ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
        ]
    ),
    (
        # Test Case 2: 'test_no_overlap'
        time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
        time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
        []
    ),
    (
        # Test Case 3: 'test_multiple_intervals_overlap'
        time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2),
        time_range("2010-01-12 10:15:00", "2010-01-12 11:15:00", 2),
        [
            ('2010-01-12 10:15:00', '2010-01-12 10:30:00'),
            ('2010-01-12 10:30:00', '2010-01-12 10:45:00'),
            ('2010-01-12 10:45:00', '2010-01-12 11:00:00')
        ]
    ),
    (
        # Test Case 4: 'test_touching_ranges'
        time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
        time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00"),
        []
    )
]

@pytest.mark.parametrize("time_range_1, time_range_2, expected", test_cases)
def test_compute_overlap_time(time_range_1, time_range_2, expected):
    result = compute_overlap_time(time_range_1, time_range_2)
    assert result == expected

def test_time_range_backwards():
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")