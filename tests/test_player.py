import unittest
from src.player import Player
from src.board import Board

class TestPlayer(unittest.TestCase):
    
    def test_repr_(self):
        p = Player('X', "LEFT", 2)
        self.assertEqual(repr(p), "Player: ox = X, tbt = LEFT, ply = 2")
        p = Player('O', "RANDOM", 0)
        self.assertEqual(repr(p), "Player: ox = O, tbt = RANDOM, ply = 0")
    
    def test_opp_chr(self):
        p = Player('X', "LEFT", 3)
        
        self.assertEqual(p.opp_ch(), 'O')
        self.assertEqual(Player('O', "LEFT", 0))

    def test_score_board(self):
        b = Board(7, 6)
        b.set_board("01020305")

        self.assertEqual(Player('X', "LEFT", 0).score_board(b), 100.0)
        self.assertEqual(Player('O', "LEFT", 0).score_board(b), 0.0)
        self.assertEqual(Player('O', "LEFT", 0).score_board(Board(7, 6)), 50.0)

    def test_tiebreak_move(self):
        scores = [0, 0, 50, 0, 50, 50, 0]
        p = Player('X', "LEFT", 1)
        p2 = Player('X', "RIGHT", 1)

        self.assertEqual(p.tiebreak_move(scores), 2)
        self.assertEqual(p2.tiebreak_move(scores), 5)

    def test_scores_for(self):
        b = Board(7, 6)
        b.set_board("1211244445")

        self.assertEqual(Player('X', "LEFT", 0).scores_for(b), [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0])
        self.assertEqual(Player('O', "LEFT", 1).scores_for(b), [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0])
        self.assertEqual(Player('X', "LEFT", 2).scores_for(b), [0.0, 0.0, 0.0, 50.0, 0.0, 0.0, 0.0])
        self.assertEqual(Player('X', "LEFT", 3).scores_for(b), [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0])
        self.assertEqual(Player('O', "LEFT", 3).scores_for(b), [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0])
        self.assertEqual(Player('O', "LEFT", 3).scores_for(b), [50.0, 50.0, 50.0, 100.0, 50.0, 50.0, 50.0])
        self.assertEqual(Player('O', "LEFT", 4).scores_for(b), [0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0])

    def test_next_move(self):
        b = Board(7, 6)
        b.set_board("1211244445")

        self.assertEqual(Player('X', "LEFT", 1).next_move(b), 0)
        self.assertEqual(Player('X', "RIGHT", 1).next_move(b), 6)
        self.assertEqual(Player('X', "LEFT", 2).next_move(b), 3)
        self.assertEqual(Player('X', "RIGHT", 2).next_move(b), 3)
        self.assertEqual(Player('X', "RANDOM", 2).next_move(b), 3)
