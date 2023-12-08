from day7 import Card, Hand, total_winnings, HandType


def test_card():
    assert Card.ACE.value > Card.KING.value
    assert Card.parse("T") == Card.TEN


def test_hand():
    hand = Hand("32T3K")
    assert [Card.THREE, Card.TWO, Card.TEN, Card.THREE, Card.KING] == hand.cards

def test_hand_type():
    assert Hand("32T3K").hand_type == HandType.PAIR
    assert Hand("T55J5").hand_type == HandType.THREE_OF_A_KIND
    assert Hand("KK677").hand_type == HandType.DOUBLE_PAIR
    assert Hand("KTJJT").hand_type == HandType.DOUBLE_PAIR
    assert Hand("QQQJQ").hand_type == HandType.FOUR_OF_A_KIND
    assert Hand("AAAAA").hand_type == HandType.FIVE_OF_A_KIND

def test_hand_comparator():
    assert Hand("QQQJA") > Hand("KTJJT")
    assert Hand("QQQJA") > Hand("KK677")
    assert Hand("QQQJA") > Hand("T55J5")
    assert Hand("QQQJA") > Hand("32T3K")

    assert Hand("T55J5") > Hand("KTJJT")
    assert Hand("T55J5") > Hand("KK677")
    assert Hand("T55J5") > Hand("32T3K")

    assert Hand("KK677") > Hand("32T3K")
    assert Hand("KK677") > Hand("KTJJT")

    assert Hand("KTJJT") > Hand("32T3K")

    assert Hand("J2T2Q") > Hand("42836")
    assert Hand("644J6") > Hand("54566")

    assert Hand("33332") > Hand("2AAAA")
    assert Hand("77888") > Hand("77788")

    assert Hand("88773") > Hand("88772")
    assert Hand("88883") > Hand("88882")
    assert Hand("38888") > Hand("28888")

    assert Hand("23457") > Hand("23456")
    assert Hand("23452") > Hand("A3456")



def test_total_winnings():
    assert 6440 == total_winnings("""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""")
