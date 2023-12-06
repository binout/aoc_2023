from dataclasses import dataclass
from functools import reduce
from typing import List

from input_examples import retrieve_intput


@dataclass
class Race:
    time: int
    distance_record: int


def compute_all_race_options(race: Race) -> List[int]:
    options = []
    for i in range(0, race.time+1):
        speed = i
        remaining_distance = race.time - i
        options.append(speed * remaining_distance)
    return options


def _count_valid_options(race: Race) -> int:
    options = compute_all_race_options(race)
    return len([option for option in options if option > race.distance_record])


def power_number_of_ways_to_beat_record(text) -> int:
    lines = [line for line in text.splitlines() if line.strip() != ""]
    times = [int(time) for time in lines[0].split(":")[1].split()]
    distance = [int(time) for time in lines[1].split(":")[1].split()]
    races = [Race(time, distance) for (time, distance) in zip(times, distance)]
    number_of_ways = [_count_valid_options(race) for race in races]
    return reduce(lambda x, y: x * y, number_of_ways)


def power_number_of_ways_to_beat_record_only_one_race(text) -> int:
    lines = [line for line in text.splitlines() if line.strip() != ""]
    time = int(lines[0].split(":")[1].strip().replace(" ", ""))
    distance = int(lines[1].split(":")[1].strip().replace(" ", ""))
    race = Race(time, distance)
    number_of_ways = _count_valid_options(race)
    return number_of_ways


if __name__ == "__main__":
    input_text = retrieve_intput(day=6)
    print(f"power_number_of_ways_to_beat_record={power_number_of_ways_to_beat_record(input_text)}")
    print(f"power_number_of_ways_to_beat_record_only_one_race={power_number_of_ways_to_beat_record_only_one_race(input_text)}")

