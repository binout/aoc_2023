from day5 import _build_mapping, lowest_seed_location, lowest_seed_location_with_range


def test_build_mapping():
    mapping = _build_mapping("""
seed-to-soil map:
50 98 2
52 50 48""")

    for i in range(0, 50):
        assert mapping[i] == i
    for i in range(50, 98):
        assert mapping[i] == i + 2
    assert mapping[98] == 50
    assert mapping[99] == 51


def test_lowest_seed_location():
    assert 35 == lowest_seed_location("""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""")

def test_lowest_seed_location_with_range():
    assert 46 == lowest_seed_location_with_range("""
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""")
