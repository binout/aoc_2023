from dataclasses import dataclass
from typing import Optional

from input_examples import retrieve_intput


@dataclass
class DigitWithIndex:
    index: int
    value: int


def calibration(text: str) -> int:
    lines = text.splitlines()
    return sum(line_calibration(line) for line in lines if line.strip() != "")


DIGITS_IN_STR = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def line_calibration(line: str) -> int:
    first_digit = _compute_digit(line)
    last_digit = _compute_digit(line, desc=True)

    if first_digit is None or last_digit is None:
        raise ValueError("No digits found in line")

    return int(f"{first_digit}{last_digit}")


def _compute_digit(line: str, desc: bool = False) -> Optional[int]:
    digit_num = _compute_digit_with_index_for_num(line, desc)
    digit_strs = [_compute_digit_with_index_for_str(line, num_str, desc) for num_str in DIGITS_IN_STR.keys()]
    all_digits_with_index = [digit for digit in [digit_num] + digit_strs if digit is not None]
    if len(all_digits_with_index) == 0:
        return None
    first_digit = min([x for x in all_digits_with_index], key=lambda x: x.index)
    return first_digit.value


def _compute_digit_with_index_for_str(line: str, num_str: str, desc: bool) -> Optional[DigitWithIndex]:
    index = line.find(num_str) if not desc else line.rfind(num_str)
    if index == -1:
        return None
    if desc:
        index = len(line) - index - len(num_str)
    return DigitWithIndex(index, DIGITS_IN_STR[num_str])


def _compute_digit_with_index_for_num(line: str, desc: bool) -> Optional[DigitWithIndex]:
    chars = list(line if not desc else reversed(line))
    first_digit = next((x for x in chars if x.isdigit()), None)
    if first_digit is None:
        return None
    return DigitWithIndex(chars.index(first_digit), int(first_digit))


if __name__ == "__main__":
    input_text = retrieve_intput(day=1)
    print(f"Calibration: {calibration(input_text)}")
