from dataclasses import dataclass

from input_examples import retrieve_intput


@dataclass
class MappingRange:
    source: int
    destination: int
    length: int


class Mapping:
    def __init__(self, ):
        self.ranges = []

    def add_range(self, source: int, destination: int, length: int):
        self.ranges.append(MappingRange(source=source, destination=destination, length=length))
        self.ranges = sorted(self.ranges, key=lambda mapping_range: mapping_range.source)

    def __getitem__(self, item):
        for mapping_range in self.ranges:
            if item < mapping_range.source:
                return item
            if item < mapping_range.source + mapping_range.length:
                return mapping_range.destination + item - mapping_range.source
        return item


def _build_mapping(text: str) -> Mapping:
    return _mapping(text.splitlines())


def _mapping(lines: list[str]) -> Mapping:
    mapping = Mapping()
    for line in lines:
        if line.strip() != "" and "map:" not in line.strip():
            parts = line.split()
            destination = int(parts[0])
            source = int(parts[1])
            length = int(parts[2])
            mapping.add_range(source=source, destination=destination, length=length)
    return mapping


def lowest_seed_location(text) -> int:
    lines = [line for line in text.splitlines() if line.strip() != ""]
    seeds = [int(seed) for seed in lines[0].split(":")[1].split()]
    print(f"Found {len(seeds)} seeds")
    return _compute_lowest_seed_location(lines[1:], seeds)


def _compute_lowest_seed_location(lines: list[str], seeds: list[int]) -> int:
    maps = []
    current_map = []
    for line in lines:
        if "map:" in line.strip():
            current_map = []
            maps.append(current_map)
        current_map.append(line)

    mappings = [_mapping(current_map) for current_map in maps]
    return min([_compute_location(seed, mappings) for seed in seeds])


def _compute_location(seed: int, mappings: list[Mapping]) -> int:
    current_position = seed
    for mapping in mappings:
        current_position = mapping[current_position]
    return current_position


def lowest_seed_location_with_range(text) -> int:
    lines = [line for line in text.splitlines() if line.strip() != ""]
    seed_ranges = [int(seed) for seed in lines[0].split(":")[1].split()]
    seeds = []
    for i in range(0, len(seed_ranges), 2):
        for j in range(seed_ranges[i], seed_ranges[i]+seed_ranges[i+1]):
            seeds.append(j)
    print(f"Found {len(seeds)} seeds")
    return _compute_lowest_seed_location(lines[1:], seeds)


if __name__ == "__main__":
    input_text = retrieve_intput(day=5)
    print(f"lowest_seed_location={lowest_seed_location(input_text)}")
    print(f"lowest_seed_location_with_range={lowest_seed_location_with_range(input_text)}")


