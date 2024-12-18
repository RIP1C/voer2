import unittest
from unittest.mock import patch, MagicMock
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

    @patch('builtins.input', side_effect=['0', '1', '2'])
    @patch.object(Board, 'allows_move', side_effect=lambda x: True)
    @patch.object(Board, 'add_move')
    @patch.object(Board, 'wins_for', side_effect=lambda x: x == 'X')
    @patch.object(Board, 'is_full', return_value=False)
    @patch('builtins.print')
    def test_host_game1(self, mock_print, mock_is_full, mock_wins_for, mock_add_move, mock_allows_move, mock_input):
        b = Board(0, 1)
        winner = b.host_game()
        mock_input.assert_any_call('Keuze van X: ')
        mock_print.assert_any_call("\n" + str(b))
        self.assertEqual(winner, 'X')

    @patch('builtins.input', side_effect=['0', '1', '2'])
    @patch.object(Board, 'allows_move', side_effect=lambda x: True)
    @patch.object(Board, 'add_move')
    @patch.object(Board, 'wins_for', side_effect=lambda x: x == 'X')
    @patch.object(Board, 'is_full', return_value=True)
    @patch('builtins.print')
    def test_host_game2(self, mock_print, mock_is_full, mock_wins_for, mock_add_move, mock_allows_move, mock_input):
        b = Board(0, 1)
        winner = b.host_game()
        mock_input.assert_any_call('Keuze van X: ')
        mock_print.assert_any_call("\n" + str(b))
        self.assertEqual(winner, ' ')

    @patch('builtins.input', side_effect=['0', '1', '2'])
    @patch.object(Board, 'allows_move', side_effect=lambda x: True)
    @patch.object(Board, 'add_move')
    @patch.object(Board, 'wins_for', side_effect=lambda x: x == 'O')
    @patch.object(Board, 'is_full', return_value=False)
    @patch('builtins.print')
    def test_host_game3(self, mock_print, mock_is_full, mock_wins_for, mock_add_move, mock_allows_move, mock_input):
        b = Board(0, 1)
        winner = b.host_game()
        mock_input.assert_any_call('Keuze van O: ')
        mock_print.assert_any_call("\n" + str(b))
        self.assertEqual(winner, 'O')



if __name__ == "__main__":
    unittest.main()