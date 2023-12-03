from day1 import calibration


def test_day1_part1():
    assert 142 == calibration("""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""")


def test_treb7uchet():
    assert 77 == calibration("treb7uchet")


def test_pqr3stu8vwx():
    assert 38 == calibration("pqr3stu8vwx")


def test_eightwothree():
    assert 83 == calibration("eightwothree")


def test_day1_part2():
    assert 281 == calibration("""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""")
