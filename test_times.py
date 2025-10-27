import pytest
from times import time_range, compute_overlap_time

def test_times():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)

    expected = [
        ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
    ]

    assert result == expected

def test_no_overlap():
    range1 = time_range('2010-01-12 10:00:00', '2010-01-12 13:00:00')
    range2 = time_range('2010-01-12 14:00:00', '2010-01-12 15:00:00')
    result = compute_overlap_time(range1, range2)

    expected = []

    assert result == expected


def test_multiple_intervals_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2)
    range2 = time_range("2010-01-12 10:15:00", "2010-01-12 11:15:00", 2)
    result = compute_overlap_time(range1, range2)
 
    expected = [
        ('2010-01-12 10:15:00', '2010-01-12 10:30:00'),
        ('2010-01-12 10:30:00', '2010-01-12 10:45:00'),
        ('2010-01-12 10:45:00', '2010-01-12 11:00:00')
    ]
    
    assert result == expected

def test_touching_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00")
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 11:15:00")
    result = compute_overlap_time(range1, range2)
 
    expected = []
    
    assert result == expected

def test_time_range_bcksards():
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")

