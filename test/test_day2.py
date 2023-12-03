from day2 import sum_of_game_ids, _parse_game, sum_power_of_minial_sets


def test_parse_game():
    game = _parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert 1 == game.id
    assert 3 == game.sets[0].blue
    assert 4 == game.sets[0].red
    assert 1 == game.sets[1].red
    assert 2 == game.sets[1].green
    assert 6 == game.sets[1].blue
    assert 2 == game.sets[2].green


def test_day2_part1():
    assert 8 == sum_of_game_ids("""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""")


def test_day2_part2():
    assert 2286 == sum_power_of_minial_sets("""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""")