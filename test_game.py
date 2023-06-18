import unittest

from hw5 import *


class TestHW5(unittest.TestCase):

    def test_get_move(self):
        for i in range(200):
            move = get_move()
            move_set = set(move)
            finger_vals = [1, 2]
            self.assertTrue(move_set.issubset(finger_vals),
                            msg="Invalid number of fingers in move returned by get_move().")

    def test_outcome_tie1(self):
        p1_move = [1, 1]
        p2_move = [1, 1]
        expected = (0, 2)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_tie2(self):
        p1_move = [2, 2]
        p2_move = [1, 1]
        expected = (0, 3)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_tie3(self):
        p1_move = [2, 2]
        p2_move = [2, 2]
        expected = (0, 4)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_tie4(self):
        p1_move = [1, 2]
        p2_move = [2, 1]
        expected = (0, 3)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_p1wins2(self):
        p1_move = [1, 1]
        p2_move = [1, 2]
        expected = (1, 2)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_p1wins3_1(self):
        p1_move = [2, 1]
        p2_move = [1, 1]
        expected = (1, 3)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_p1wins3_2(self):
        p1_move = [1, 2]
        p2_move = [2, 2]
        expected = (1, 3)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_p1wins4(self):
        p1_move = [2, 2]
        p2_move = [2, 1]
        expected = (1, 4)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_p2wins3(self):
        p1_move = [2, 2]
        p2_move = [1, 2]
        expected = (2, 3)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_outcome_p2wins4(self):
        p1_move = [2, 1]
        p2_move = [2, 2]
        expected = (2, 4)
        actual = get_outcome(p1_move, p2_move)
        self.assertEqual(expected, actual)

    def test_calc_winnings_tie(self):
        player = 1
        winner = 0
        amount = 0
        expected = 0
        actual = calc_winnings(player, winner, amount)
        self.assertEqual(expected, actual)

    def test_calc_winnings_p1wins3(self):
        player = 1
        winner = 1
        amount = 3
        expected = 3
        actual = calc_winnings(player, winner, amount)
        self.assertEqual(expected, actual)

    def test_calc_winnings_p1loses2(self):
        player = 1
        winner = 2
        amount = 2
        expected = -2
        actual = calc_winnings(player, winner, amount)
        self.assertEqual(expected, actual)

    def test_calc_winnings_p2wins3(self):
        player = 2
        winner = 2
        amount = 3
        expected = 3
        actual = calc_winnings(player, winner, amount)
        self.assertEqual(expected, actual)

    def test_calc_winnings_p2loses2(self):
        player = 2
        winner = 1
        amount = 2
        expected = -2
        actual = calc_winnings(player, winner, amount)
        self.assertEqual(expected, actual)

    def test_play_multiple_len(self):
        winnings = play_multiple(14)
        actual = len(winnings)
        expected = 14
        self.assertEqual(expected, actual)

    def test_play_multiple_win_values(self):
        winnings = play_multiple(1000)
        vals_in_winnings = set(winnings)
        possible_winnings = [-4, -3, -2, 0, 2, 3, 4]
        self.assertTrue(vals_in_winnings.issubset(possible_winnings),
                        msg="Invalid value in winnings list returned by play_multiple().")


if __name__ == '__main__':
    unittest.main()
