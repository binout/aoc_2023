from dataclasses import dataclass
from itertools import cycle

from input_examples import retrieve_intput


@dataclass(frozen=True)
class Node:
    value: str

    @property
    def is_start(self) -> bool:
        return self.value == "AAA"

    @property
    def is_end(self) -> bool:
        return self.value == "ZZZ"

    def __repr__(self):
        return self.value

@dataclass
class Network:
    node: Node
    left: Node
    right: Node


def _parse_network(input_text:str) -> Network:
    parsed = input_text.split("=")
    node = Node(parsed[0].strip())
    left_and_right = parsed[1].replace("(", "").replace(")", "").split(",")
    left = Node(left_and_right[0].strip())
    right = Node(left_and_right[1].strip())
    return Network(node=node, left=left, right=right)


def steps_to_end(input_text:str) -> int:
    lines = [line for line in  input_text.splitlines() if line.strip() != ""]
    directions = [direction for direction in lines[0].strip()]
    networks = [_parse_network(line) for line in lines[1:] if line.strip() != ""]
    network_by_node = {network.node: network for network in networks}

    nb_steps = 0
    current_network = network_by_node[Node("AAA")]
    for direction in cycle(directions):
        nb_steps += 1
        if direction == "L":
            current_network = network_by_node[current_network.left]
        else:
            current_network = network_by_node[current_network.right]
        if current_network.node.is_end:
            break
    return nb_steps


if __name__ == "__main__":
    input_text = retrieve_intput(day=8)
    print(steps_to_end(input_text))