from day9 import OasisSensor, sum_extrapolated_next_values


def test_oasis_sensor_next_value():
    sensor = OasisSensor([0, 3, 6, 9, 12, 15])
    assert 18 == sensor.compute_next_value()

    sensor = OasisSensor([1, 3, 6, 10, 15, 21])
    assert 28 == sensor.compute_next_value()


def test_oasis_sensor_first_value():
    sensor = OasisSensor([10, 13, 16, 21, 30, 45])
    assert 5 == sensor._compute_first_value()



def test_sum_extrapolated_values():
    assert 114 == sum_extrapolated_next_values("""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""")