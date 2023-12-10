from dataclasses import dataclass
from itertools import accumulate
from typing import List

from input_examples import retrieve_intput


@dataclass
class OasisSensor:
    values: List[int]

    def compute_next_value(self) -> int:
        previous_values = self.values
        last_values = []
        while set(previous_values) != {0}:
            last_values.append(previous_values[-1])
            previous_values = self._compute_next_history(previous_values)

        return list(accumulate(reversed(last_values)))[-1]

    def compute_first_value(self) -> int:
        previous_values = self.values
        first_values = []
        while set(previous_values) != {0}:
            first_values.append(previous_values[0])
            previous_values = self._compute_previous_history(previous_values)

        return list(accumulate(reversed(first_values), lambda x, y: y - x))[-1]

    @staticmethod
    def _compute_next_history(values: List[int]) -> List[int]:
        return [values[index] - values[index-1] for index, value in enumerate(values) if index > 0]

    @staticmethod
    def _compute_previous_history(values: List[int]) -> List[int]:
        return [values[index] - values[index-1] for index, value in enumerate(values) if index > 0]


def sum_extrapolated_next_values(input_text:str):
    lines = [line for line in input_text.splitlines() if line.strip() != ""]
    return sum([OasisSensor([int(value) for value in line.split()]).compute_next_value() for line in lines])


def sum_extrapolated_first_values(input_text:str):
    lines = [line for line in input_text.splitlines() if line.strip() != ""]
    return sum([OasisSensor([int(value) for value in line.split()]).compute_first_value() for line in lines])


if __name__ == "__main__":
    retrieve_intput(day=9)
    print(f"sum_extrapolated_next_values={sum_extrapolated_next_values(retrieve_intput(day=9))}")
    print(f"sum_extrapolated_first_values={sum_extrapolated_first_values(retrieve_intput(day=9))}")

