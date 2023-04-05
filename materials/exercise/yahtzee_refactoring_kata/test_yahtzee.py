from yahtzee import Yatzy


def test_chance_scores_sum_of_all_dice():
    expected = 15
    actual = Yatzy.chance(2, 3, 4, 5, 1)
    assert expected == actual
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)


def test_yatzy_scores_50():
    expected = 50
    actual = Yatzy.yatzy([4, 4, 4, 4, 4])
    assert expected == actual
    assert 50 == Yatzy.yatzy([6, 6, 6, 6, 6])
    assert 0 == Yatzy.yatzy([6, 6, 6, 6, 3])