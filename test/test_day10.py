from day10 import compute_steps_to_get_out



def test_compute_steps_to_get_out_1():
    assert 4 == compute_steps_to_get_out("""
.....
.S-7.
.|.|.
.L-J.
.....""")


def test_compute_steps_to_get_out_2():
    assert 8 == compute_steps_to_get_out("""
..F7.
.FJ|.
SJ.L7
|F--J
LJ...""")

