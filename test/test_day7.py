from day7 import Card, Hand, total_winnings, HandType, HandWithJoker, parse_hand, parse_hand_with_joker, \
    total_winnings_with_joker


def test_card():
    assert Card.ACE.value > Card.KING.value
    assert Card.parse("T") == Card.TEN


def test_hand():
    hand = parse_hand("32T3K")
    assert [Card.THREE, Card.TWO, Card.TEN, Card.THREE, Card.KING] == hand.cards

def test_hand_type():
    assert parse_hand("32T3K").hand_type == HandType.PAIR
    assert parse_hand("T55J5").hand_type == HandType.THREE_OF_A_KIND
    assert parse_hand("KK677").hand_type == HandType.DOUBLE_PAIR
    assert parse_hand("KTJJT").hand_type == HandType.DOUBLE_PAIR
    assert parse_hand("QQQJQ").hand_type == HandType.FOUR_OF_A_KIND
    assert parse_hand("AAAAA").hand_type == HandType.FIVE_OF_A_KIND

def test_hand_comparator():
    assert parse_hand("QQQJA") > parse_hand("KTJJT")
    assert parse_hand("QQQJA") > parse_hand("KK677")
    assert parse_hand("QQQJA") > parse_hand("T55J5")
    assert parse_hand("QQQJA") > parse_hand("32T3K")

    assert parse_hand("T55J5") > parse_hand("KTJJT")
    assert parse_hand("T55J5") > parse_hand("KK677")
    assert parse_hand("T55J5") > parse_hand("32T3K")

    assert parse_hand("KK677") > parse_hand("32T3K")
    assert parse_hand("KK677") > parse_hand("KTJJT")

    assert parse_hand("KTJJT") > parse_hand("32T3K")

    assert parse_hand("J2T2Q") > parse_hand("42836")
    assert parse_hand("644J6") > parse_hand("54566")

    assert parse_hand("33332") > parse_hand("2AAAA")
    assert parse_hand("77888") > parse_hand("77788")

    assert parse_hand("88773") > parse_hand("88772")
    assert parse_hand("88883") > parse_hand("88882")
    assert parse_hand("38888") > parse_hand("28888")

    assert parse_hand("23457") > parse_hand("23456")
    assert parse_hand("23452") > parse_hand("A3456")



def test_total_winnings():
    assert 6440 == total_winnings("""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""")


def test_hand_type_with_joker():
    assert parse_hand_with_joker("32T3K").hand_type == HandType.PAIR
    assert parse_hand_with_joker("KK677").hand_type == HandType.DOUBLE_PAIR
    assert parse_hand_with_joker("T55J5").hand_type == HandType.FOUR_OF_A_KIND
    assert parse_hand_with_joker("KTJJT").hand_type == HandType.FOUR_OF_A_KIND
    assert parse_hand_with_joker("QQQJA").hand_type == HandType.FOUR_OF_A_KIND
    assert parse_hand_with_joker("JJJJJ").hand_type == HandType.FIVE_OF_A_KIND
    assert parse_hand_with_joker("J5555").hand_type == HandType.FIVE_OF_A_KIND
    assert parse_hand_with_joker("J2345").hand_type == HandType.PAIR
    assert parse_hand_with_joker("J2355").hand_type == HandType.THREE_OF_A_KIND
    assert parse_hand_with_joker("JJ232").hand_type == HandType.FOUR_OF_A_KIND
    assert parse_hand_with_joker("J2233").hand_type == HandType.FULL_HOUSE

def test_hand_comparator_with_joker():
    assert parse_hand_with_joker("QQQJA") < parse_hand_with_joker("KTJJT")
    assert parse_hand_with_joker("QQQJA") > parse_hand_with_joker("KK677")
    assert parse_hand_with_joker("QQQJA") > parse_hand_with_joker("T55J5")
    assert parse_hand_with_joker("QQQJA") > parse_hand_with_joker("32T3K")

    assert parse_hand_with_joker("QQQJA") > parse_hand_with_joker("JQQQA")
    assert parse_hand_with_joker("AJJJ2") > parse_hand_with_joker("JJJA2")




def test_total_winnings_with_joker():
    assert 5905 == total_winnings_with_joker("""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""")