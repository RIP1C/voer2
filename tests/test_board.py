import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def test_board(self):
        b = Board(2, 3)
        self.assertEqual(b.width, 2)
        self.assertEqual(b.height, 3)
        self.assertEqual(b.data, [
            [' ', ' '],
            [' ', ' '],
            [' ', ' '],
        ])

    def test_allows_move(self):
        b = Board(2, 2)
        self.assertEqual(b.allows_move(1), True, "Should be True")
        self.assertEqual(b.allows_move(2), False, "Should be False")
        self.assertEqual(b.allows_move(-1), False, "Should be false")
        self.assertEqual(b.allows_move(0), True, "Should be True")

    def test_set_board(self):
        b = Board(7, 6)    
        b.set_board("0000")
        self.assertEqual(b.data, [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['O', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', ' ', ' ', ' ', ' ', ' ', ' '],
            ['O', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', ' ', ' ', ' ', ' ', ' ', ' '],
        ])

        b = Board(2, 2)
        b.set_board("1001")
        self.assertEqual(b.data, [
            ['X', 'O'],
            ['O', 'X'],
        ])

        b = Board(1,1)
        b.set_board("0")
        self.assertEqual(b.data, [
            ['X']
        ])


if __name__ == "__main__":
    unittest.main()