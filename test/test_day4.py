from day4 import scratchcards_point, _parse_card, total_scratchcards_won

def test_parse_cards():
    card = _parse_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert 1 == card.id
    assert {41, 48, 83, 86, 17} == card.winning_numbers
    assert {83, 86, 6, 31, 17, 9, 48, 53} == card.numbers

def test_card_score():
    assert 8 == _parse_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53").score
    assert 2 == _parse_card("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19").score
    assert 2 == _parse_card("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1").score
    assert 1 == _parse_card("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83").score
    assert 0 == _parse_card("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36").score
    assert 0 == _parse_card("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11").score


def test_scratchcards_point():
    assert 13 == scratchcards_point("""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""")


def test_total_scratchcards_won():
    assert 30 == total_scratchcards_won("""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""")
