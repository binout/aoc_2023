from collections import Counter
from enum import Enum
from typing import List, Union

from input_examples import retrieve_intput


class Card(Enum):
    JOKER = 0
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

    @staticmethod
    def parse_with_joker(value: str):
        if value == "J":
            return Card.JOKER
        return Card.parse(value)


class HandType(Enum):
    HIGH_CARD = 1
    PAIR = 2
    DOUBLE_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7



class Hand:

    def __init__(self, cards: List[Card]):
          self.cards = cards

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
            result = HandType.FIVE_OF_A_KIND
        elif highest_kind[1] == 4:
            result = HandType.FOUR_OF_A_KIND
        elif highest_kind[1] == 3:
            if len(kinds) == 2 and kinds[1][1] == 2:
                result = HandType.FULL_HOUSE
            else:
                result = HandType.THREE_OF_A_KIND
        elif highest_kind[1] == 2:
            if len(kinds) == 2 and kinds[1][1] == 2:
                result = HandType.DOUBLE_PAIR
            else:
                result = HandType.PAIR
        else:
            result = HandType.HIGH_CARD
        return result


def _default_comparator(hand1: Hand, hand2: Hand)->bool:
    zipped = zip(hand1.cards, hand2.cards)
    first_diff = next((card for card in zipped if card[0].value != card[1].value), None)
    return first_diff[0].value > first_diff[1].value


def parse_hand(input_text: str) -> "Hand":
    if len(input_text) != 5:
        raise ValueError("Invalid number of cards")
    return Hand([Card.parse(input_card) for input_card in input_text])


class HandWithJoker(Hand):

    @property
    def hand_type(self) -> HandType:
        number_jokers = sum(card == Card.JOKER for card in self.cards)
        counter = Counter(card for card in self.cards if card != Card.JOKER)
        two_most_commons = counter.most_common(2)
        hightest_kind = two_most_commons[0][1] if len(two_most_commons) > 0 else 0
        second_highest_kind = two_most_commons[1][1] if len(two_most_commons) > 1 else 0

        if number_jokers in [4, 5]:
            return HandType.FIVE_OF_A_KIND
        elif number_jokers == 3:
            if len(set(self.cards)) == 2:
                return HandType.FIVE_OF_A_KIND
            else:
                return HandType.FOUR_OF_A_KIND
        elif number_jokers == 2:
            if hightest_kind == 3:
                return HandType.FIVE_OF_A_KIND
            elif hightest_kind == 2:
                return HandType.FOUR_OF_A_KIND
            else:
                return HandType.THREE_OF_A_KIND
        elif number_jokers == 1:
            if hightest_kind == 4:
                return HandType.FIVE_OF_A_KIND
            elif hightest_kind == 3:
                return HandType.FOUR_OF_A_KIND
            elif hightest_kind == 2:
                if second_highest_kind == 2:
                    return HandType.FULL_HOUSE
                return HandType.THREE_OF_A_KIND
            else:
                return HandType.PAIR
        else:
            return Hand(self.cards).hand_type


def parse_hand_with_joker(input_text: str) -> HandWithJoker:
    if len(input_text) != 5:
        raise ValueError("Invalid number of cards")
    return HandWithJoker([Card.parse_with_joker(input_card) for input_card in input_text])


def total_winnings(input_text:str):
    lines = [line for line in input_text.splitlines() if line.strip() != ""]
    hands_with_bet = {parse_hand(line.split()[0]): int(line.split()[1]) for line in lines}
    sorted_hands_with_bet = dict(sorted(hands_with_bet.items()))
    return sum([(index+1) * sorted_hands_with_bet[hand] for index,hand in enumerate(sorted_hands_with_bet)])


def total_winnings_with_joker(input_text:str):
    lines = [line for line in input_text.splitlines() if line.strip() != ""]
    hands_with_bet = {parse_hand_with_joker(line.split()[0]): int(line.split()[1]) for line in lines}
    sorted_hands_with_bet = dict(sorted(hands_with_bet.items()))
    return sum([(index+1) * sorted_hands_with_bet[hand] for index,hand in enumerate(sorted_hands_with_bet)])


if __name__ == "__main__":
    input_text = retrieve_intput(day=7)
    print(f"total_winnings={total_winnings(input_text)}")
    print(f"total_winnings_with_joker={total_winnings_with_joker(input_text)}")

