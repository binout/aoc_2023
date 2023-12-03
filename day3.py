from dataclasses import dataclass
from typing import List

from input_examples import retrieve_intput


@dataclass
class Index:
    x: int
    y: int

    def around_valid_indexes(self) -> List["Index"]:
        return [
            Index(x=self.x - 1, y=self.y - 1),
            Index(x=self.x - 1, y=self.y),
            Index(x=self.x - 1, y=self.y + 1),
            Index(x=self.x, y=self.y - 1),
            Index(x=self.x, y=self.y + 1),
            Index(x=self.x + 1, y=self.y - 1),
            Index(x=self.x + 1, y=self.y),
            Index(x=self.x + 1, y=self.y + 1),
        ]


@dataclass
class IndexedDigit:
    value: str
    indexes: List[Index]

    def __add__(self, other):
        return IndexedDigit(value=self.value + other.value, indexes=self.indexes + other.indexes)

    def value_as_int(self):
        return int(self.value)


Gear = Index

EMPTY_DIGIT = IndexedDigit(value="", indexes=[])


def sum_of_part_numbers(text: str) -> int:
    lines = text.splitlines()
    valid_indexes = _compute_valid_indexes(lines)
    valid_digits = [digit for digit in _get_all_digits(lines) if any([index in valid_indexes for index in digit.indexes])]
    return sum([digit.value_as_int() for digit in valid_digits])


def sum_of_gear_ratios(text: str) -> int:
    lines = text.splitlines()
    digits = _get_all_digits(lines)
    gears = _get_all_gears(lines)
    gear_ratios = []
    for gear in gears:
        gear_digits = [digit for digit in digits if any([index in gear.around_valid_indexes() for index in digit.indexes])]
        if len(gear_digits) == 2:
            gear_ratios.append(gear_digits[0].value_as_int() * gear_digits[1].value_as_int())
    return sum(gear_ratios)


def _get_all_gears(lines: List[str]) -> List[Gear]:
    gears = []
    for rowIndex, line in enumerate(lines):
        for columnIndex, char in enumerate(line):
            if char == "*":
                gears.append(Gear(x=rowIndex, y=columnIndex))
    return gears


def _get_all_digits(lines: List[str]) -> List[IndexedDigit]:
    digits = []
    for rowIndex, line in enumerate(lines):
        if not any(char for char in line if char.isdigit()):
            continue
        current_digit = EMPTY_DIGIT
        for columnIndex, char in enumerate(line):
            if char.isdigit():
                current_digit += IndexedDigit(value=char, indexes=[Index(x=rowIndex, y=columnIndex)])
                # last digit in line
                if columnIndex == len(line) - 1:
                    digits.append(current_digit)
            else:
                # end of digit
                if current_digit != EMPTY_DIGIT:
                    digits.append(current_digit)
                current_digit = EMPTY_DIGIT
    return digits


def _compute_valid_indexes(lines: List[str]) -> List[Index]:
    valid_indexes = []
    for rowIndex, line in enumerate(lines):
        for columnIndex, char in enumerate(line):
            if char.isdigit() or char == ".":
                continue
            index = Index(x=rowIndex, y=columnIndex)
            valid_indexes.extend(index.around_valid_indexes())
    return valid_indexes


if __name__ == "__main__":
    input_text = retrieve_intput(day=3)
    print(f"sum_of_part_numbers={sum_of_part_numbers(input_text)}")
    print(f"sum_of_gear_ratios={sum_of_gear_ratios(input_text)}")
