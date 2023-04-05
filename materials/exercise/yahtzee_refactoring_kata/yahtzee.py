class Yatzy:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        """
        The player scores the sum of all dice, no matter what they read. For example:

        1,1,3,3,6 placed on “chance” scores 14 (1+1+3+3+6)
        4,5,5,6,1 placed on “chance” scores 21 (4+5+5+6+1)
        """
        total = 0
        total += d1
        total += d2
        total += d3
        total += d4
        total += d5
        return total

    @staticmethod
    def yatzy(dice):
        """
        If all dice have the same number, the player scores 50 points. For example:

        1,1,1,1,1 placed on “yatzy” scores 50
        1,1,1,2,1 placed on “yatzy” scores 0
        """
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        sum = 0
        if (d1 == 1):
            sum += 1
        if (d2 == 1):
            sum += 1
        if (d3 == 1):
            sum += 1
        if (d4 == 1):
            sum += 1
        if (d5 == 1):
            sum += 1

        return sum

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        sum = 0
        if (d1 == 2):
            sum += 2
        if (d2 == 2):
            sum += 2
        if (d3 == 2):
            sum += 2
        if (d4 == 2):
            sum += 2
        if (d5 == 2):
            sum += 2
        return sum

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        s = 0
        if (d1 == 3):
            s += 3
        if (d2 == 3):
            s += 3
        if (d3 == 3):
            s += 3
        if (d4 == 3):
            s += 3
        if (d5 == 3):
            s += 3
        return s

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4):
                sum += 4
        return sum

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if (self.dice[i] == 5):
                s = s + 5
        return s

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)):
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum

    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        """
        The player scores the sum of the two highest matching dice. For example, when placed on “pair”:

        1,2,3,4,5 scores 0
        3,3,3,4,4 scores 8 (4+4)
        1,1,6,2,6 scores 12 (6+6)
        3,3,3,4,1 scores 6 (3+3)
        3,3,3,3,1 scores 6 (3+3)
        """
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0

    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        """
        when placed on “two pairs”:

        1,1,2,3,3 scores 8 (1+1+3+3)
        1,1,2,3,4 scores 0
        1,1,2,2,2 scores 6 (1+1+2+2)
        3,3,3,3,1 scores 0
        """
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        """
        If there are four dice with the same number, the player scores the sum of these dice. For example, when placed on “four of a kind”:

        2,2,2,2,5 scores 8 (2+2+2+2)
        2,2,2,5,5 scores 0
        2,2,2,2,2 scores 8 (2+2+2+2)
        """
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        """
        If there are three dice with the same number, the player scores the sum of these dice. For example, when placed on “three of a kind”:

        3,3,3,4,5 scores 9 (3+3+3)
        3,3,4,5,6 scores 0
        3,3,3,3,1 scores 9 (3+3+3)
        """
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        """
        When placed on “small straight”, if the dice read

        1,2,3,4,5,

        the player scores 15 (the sum of all the dice).
        """
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        """
        When placed on “large straight”, if the dice read

        2,3,4,5,6,

        the player scores 20 (the sum of all the dice).
        """
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        """
        If the dice are two of a kind and three of a kind, the player scores the sum of all the dice. For example, when placed on “full house”:

        1,1,2,2,2 scores 8 (1+1+2+2+2)
        2,2,3,3,4 scores 0
        4,4,4,4,4 scores 0
        """
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0