import dataclasses
from dataclasses import dataclass
from typing import List

from input_examples import retrieve_intput

BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


@dataclass
class GameSet:
    red: int
    green: int
    blue: int

    def is_valid(self) -> bool:
        return self.red <= BAG["red"] and self.green <= BAG["green"] and self.blue <= BAG["blue"]

    def power(self) -> int:
        return self.red * self.green * self.blue


@dataclass
class Game:
    id: int
    sets: List[GameSet]

    def is_valid(self) -> bool:
        for gameSet in self.sets:
            if not gameSet.is_valid():
                return False

        red_max = max([gameSet.red for gameSet in self.sets])
        green_max = max([gameSet.green for gameSet in self.sets])
        blue_max = max([gameSet.blue for gameSet in self.sets])
        return red_max <= BAG["red"] and green_max <= BAG["green"] and blue_max <= BAG["blue"]

    def minimal_set(self) -> GameSet:
        red_min = max([gameSet.red for gameSet in self.sets])
        green_min = max([gameSet.green for gameSet in self.sets])
        blue_min = max([gameSet.blue for gameSet in self.sets])
        return GameSet(red=red_min, green=green_min, blue=blue_min)


def _parse_game(text: str) -> Game:
    text_parts = text.split(":")

    prefix = text_parts[0]
    game_id = int(prefix.split(" ")[1])

    content = text_parts[1]
    sets = [_parse_game_set(content_sets) for content_sets in content.split(";")]

    return Game(id=game_id, sets=sets)


def _parse_game_set(text_set:str) -> GameSet:
    content_set = text_set.strip()
    color_parts = content_set.split(",")
    game_set = GameSet(red=0, green=0, blue=0)
    for color_part in color_parts:
        color_part = color_part.strip()
        if color_part == "":
            continue
        color = color_part.split(" ")[1]
        if color not in BAG:
            raise ValueError(f"Invalid color {color_part}")
        color_value = int(color_part.split(" ")[0])
        game_set = dataclasses.replace(game_set, **{color: color_value})
    return game_set


def _parse_input_text(text) -> List[Game]:
    str_games = text.splitlines()
    return [_parse_game(str_game) for str_game in str_games if str_game.strip() != ""]


def sum_of_game_ids(text: str) -> int:
    games = _parse_input_text(text)
    return sum([game.id for game in games if game.is_valid()])


def sum_power_of_minial_sets(text: str) -> int:
    games = _parse_input_text(text)
    return sum([game.minimal_set().power() for game in games])


if __name__ == "__main__":
    input_text = retrieve_intput(day=2)
    print(f"sum_of_game_ids={sum_of_game_ids(input_text)}")
    print(f"sum_power_of_minial_sets={sum_power_of_minial_sets(input_text)}")

