from day6 import compute_all_race_options, Race, power_number_of_ways_to_beat_record, \
    power_number_of_ways_to_beat_record_only_one_race


def test_compute_all_race_options():
    options = compute_all_race_options(Race(time=7, distance_record=15))
    assert [0, 6, 10, 12, 12, 10, 6, 0] == options


def test_power_number_of_ways_to_beat_record():
    assert 288 == power_number_of_ways_to_beat_record("""
Time:      7  15   30
Distance:  9  40  200
""")


def test_power_number_of_ways_to_beat_record_only_one_race():
    assert 71503 == power_number_of_ways_to_beat_record_only_one_race("""
Time:      7  15   30
Distance:  9  40  200
""")

