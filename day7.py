from collections import Counter
from enum import Enum

from input_examples import retrieve_intput


class Card(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @staticmethod
    def parse(value: str):
        if value == "T":
            return Card.TEN
        elif value == "J":
            return Card.JACK
        elif value == "Q":
            return Card.QUEEN
        elif value == "K":
            return Card.KING
        elif value == "A":
            return Card.ACE
        else:
            return Card(int(value))

class HandType(Enum):
    HIGH_CARD = 1
    PAIR = 2
    DOUBLE_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:

    def __init__(self, input_text: str):
        if len(input_text) != 5:
            raise ValueError("Invalid number of cards")
        self.cards = [Card.parse(input_card) for input_card in input_text]

    def __repr__(self):
        return f"Hand({self.cards})"

    def __le__(self, other):
        return not self.__gt__(other)

    def __gt__(self, other):
        if self.hand_type == other.hand_type:
            return _default_comparator(self, other)
        else:
            return self.hand_type.value > other.hand_type.value

    @property
    def hand_type(self) -> HandType:
        card_counter = Counter(self.cards)
        kinds = card_counter.most_common(2)
        highest_kind = max(kinds, key=lambda x: x[1])
        if highest_kind[1] == 5:
            return HandType.FIVE_OF_A_KIND
        elif highest_kind[1] == 4:
            return HandType.FOUR_OF_A_KIND
        elif highest_kind[1] == 3:
            if len(kinds) == 2 and kinds[1][1] == 2:
                return HandType.FULL_HOUSE
            else:
                return HandType.THREE_OF_A_KIND
        elif highest_kind[1] == 2:
            if len(kinds) == 2 and kinds[1][1] == 2:
                return HandType.DOUBLE_PAIR
            else:
                return HandType.PAIR
        else:
            return HandType.HIGH_CARD


def _default_comparator(hand1: Hand, hand2: Hand)->bool:
    zipped = zip(hand1.cards, hand2.cards)
    first_diff = next((card for card in zipped if card[0].value != card[1].value), None)
    return first_diff[0].value > first_diff[1].value


def total_winnings(input_text:str):
    lines = [line for line in input_text.splitlines() if line.strip() != ""]
    hands_with_bet = {Hand(line.split()[0]): int(line.split()[1]) for line in lines}
    sorted_hands_with_bet = dict(sorted(hands_with_bet.items()))
    return sum([(index+1) * sorted_hands_with_bet[hand] for index,hand in enumerate(sorted_hands_with_bet)])


if __name__ == "__main__":
    input_text = retrieve_intput(day=7)
    print(f"total_winnings={total_winnings(input_text)}")