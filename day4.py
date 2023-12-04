from collections import defaultdict
from dataclasses import dataclass
from math import pow

from input_examples import retrieve_intput


@dataclass
class Card:
    id: int
    winning_numbers: set[int]
    numbers: set[int]

    @property
    def score(self) -> int:
        if self.number_of_matchings == 0:
            return 0
        return int(pow(2, self.number_of_matchings - 1))

    @property
    def number_of_matchings(self) -> int:
        return len(self.winning_numbers.intersection(self.numbers))


def _parse_card(line: str) -> Card:
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    prefix = line.split(":")[0]
    card_id = int(prefix.split()[1])
    number_part = line.split(":")[1]
    numbers = number_part.split("|")
    winning_numbers = set(int(number) for number in numbers[0].split())
    numbers = set(int(number) for number in numbers[1].split())
    return Card(id=card_id, winning_numbers=winning_numbers, numbers=numbers)


def scratchcards_point(text:str) -> int:
    lines = text.splitlines()
    cards = [_parse_card(line) for line in lines if line.strip() != ""]
    return sum([card.score for card in cards])


def total_scratchcards_won(text:str) -> int:
    lines = text.splitlines()
    cards = [_parse_card(line) for line in lines if line.strip() != ""]
    current_cards: dict[int, int] = defaultdict(lambda: 0)
    for card in cards:
        current_cards[card.id] += 1
        number_of_matchings = card.number_of_matchings
        for i in range(1, number_of_matchings+1):
            current_cards[i + card.id] += current_cards[card.id]
    return sum(current_cards.values())


if __name__ == "__main__":
    input_text = retrieve_intput(day=4)
    print(f"scratchcards_point={scratchcards_point(input_text)}")
    print(f"total_scratchcards_won={total_scratchcards_won(input_text)}")