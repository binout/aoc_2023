from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple

from input_examples import retrieve_intput


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Tile(Enum):
    VERTICAL_PIPE = "|"
    HORIZONTAL_PIPE = "-"
    L = "L"
    J = "J"
    _7 = "7"
    F = "F"

    @staticmethod
    def parse(value: str):
        if value == "|":
            return Tile.VERTICAL_PIPE
        elif value == "-":
            return Tile.HORIZONTAL_PIPE
        elif value == "L":
            return Tile.L
        elif value == "J":
            return Tile.J
        elif value == "7":
            return Tile._7
        elif value == "F":
            return Tile.F
        raise ValueError(f"Unknown tile {value}")

class Direction(Enum):
    N = "N"
    S = "S"
    E = "E"
    W = "W"

    def inverse(self):
        if self == Direction.N:
            return Direction.S
        elif self == Direction.S:
            return Direction.N
        elif self == Direction.E:
            return Direction.W
        elif self == Direction.W:
            return Direction.E
        raise ValueError(f"Unknown direction {self}")


def _apply_direction(point: Point, direction: Direction) -> Point:
    if direction == Direction.N:
        return point + Point(0, -1)
    elif direction == Direction.S:
        return point + Point(0, 1)
    elif direction == Direction.E:
        return point + Point(1, 0)
    elif direction == Direction.W:
        return point + Point(-1, 0)
    raise ValueError(f"Unknown direction {direction}")



def _compute_connections(tile: Tile) -> Tuple[Direction, Direction]:
    if tile == Tile.VERTICAL_PIPE:
        return Direction.N, Direction.S
    elif tile == Tile.HORIZONTAL_PIPE:
        return Direction.E, Direction.W
    elif tile == Tile.L:
        return Direction.S, Direction.W
    elif tile == Tile.J:
        return Direction.S, Direction.E
    elif tile == Tile._7:
        return Direction.N, Direction.E
    elif tile == Tile.F:
        return Direction.N, Direction.W
    raise ValueError(f"Unknown tile {tile}")


def compute_steps_to_get_out(input_text:str) -> int:
    lines = [line for line in input_text.splitlines() if line.strip() != ""]
    map, start = _read_map(lines)
    current_node = start
    last_direction = None
    nb_steps = 0

    print(f"Starting walk at {current_node}")
    while True:
        for direction in {Direction.N, Direction.S, Direction.E, Direction.W}:
            # Avoid going back
            if direction.inverse() == last_direction:
                continue
            move = _apply_direction(current_node, direction)
            if move == start:
                current_node = move
                last_direction = direction
                nb_steps += 1
                break

            tile = map.get(move, None)
            if tile is not None:
                connections = _compute_connections(tile)
                if direction in connections:
                    current_node = move
                    last_direction = direction
                    nb_steps += 1
                    print(f"Moved to {current_node} with {tile}")
                    break

        # We are back to start
        if current_node == start:
            print(f"Back to start at {current_node}")
            break

    return nb_steps/2


def _read_map(lines: List[str]) -> Tuple[dict, Point]:
    map = {}
    start = None
    for num_line, line in enumerate(lines):
        for index, char in enumerate(line):
            point = Point(index, num_line)
            if char == ".":
                continue
            if char == "S":
                start = point
            else:
                map[point] = Tile.parse(char)
    return map, start


if __name__ == "__main__":
    input_text = retrieve_intput(day=10)
    print(f"steps_to_get_out={compute_steps_to_get_out(input_text)}")

