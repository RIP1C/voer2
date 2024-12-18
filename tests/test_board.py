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

    def test_add_move(self):
        b = Board(1, 1)
        b.add_move(0, 'X')
        self.assertEqual(b.data, [
            ['X'],
        ])

        b = Board(3, 3)
        b.add_move(1, 'O')
        b.add_move(1, 'X')
        b.add_move(1, 'O')
        b.add_move(0, 'X')
        b.add_move(2, 'O')
        b.add_move(2, 'X')
        self.assertEqual(b.data, [
            [' ', 'O', ' '],
            [' ', 'X', 'X'],
            ['X', 'O', 'O'],
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

        b = Board(1, 1)
        b.set_board("0")
        self.assertEqual(b.data, [
            ['X']
        ])

    def test_clear(self):
        b = Board(2, 2)
        b.set_board("0011")
        b.clear()
        self.assertEqual(b.data, [
            [' ', ' '],
            [' ', ' '],
        ])

    def test_is_full(self):
        b = Board(3, 3)
        b.set_board("000111222")
        self.assertEqual(b.is_full(), True)

        b = Board(0, 1)
        self.assertEqual(b.is_full(), False)

        b = Board(1, 1)
        self.assertEqual(b.is_full(), False)

        b = Board(1, 1)
        self.assertEqual(b.is_full(), False)

    def test_del_move(self):
        b = Board(2, 2)
        b.set_board("0011")
        b.del_move(1)
        self.assertEqual(b.data, [
            ['O', ' '],
            ['X', 'X'],
        ])
        b.del_move(1)
        self.assertEqual(b.data, [
            ['O', ' '],
            ['X', ' '],
        ])

        b.del_move(0)
        self.assertEqual(b.data, [
            [' ', ' '],
            ['X', ' '],
        ])

        b.del_move(0)
        self.assertEqual(b.data, [
            [' ', ' '],
            [' ', ' '],
        ])
    
    def test_wins_for(self):
        b = Board(4, 4)
        b.set_board("0101010")
        self.assertEqual(b.wins_for('X'), True)
        self.assertEqual(b.wins_for('O'), False)

        b = Board(1, 1)
        self.assertEqual(b.wins_for('X'), False)


if __name__ == "__main__":
    unittest.main()