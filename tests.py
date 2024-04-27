import unittest
from board import *
from computer_player import *

class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()
    
    def test_move(self):
        col = 2; row = 2; symbol = 'X'
        self.board.move(row, col, symbol)
        self.assertEqual(self.board.get_square(2, 2), 'X')
        for i in range (-1, 2):
            for j in range (-1, 2):
                if not (i == 0 and j == 0):
                    if ((0 <= row + i < self.board.height) and (0 <= col + j < self.board.width)):
                        self.assertEqual(self.board.get_square(row + i, col + j), '-')


    def test_remove_squares(self):
        col = 2; row = 2; symbol = 'X'
        self.board.move(row, col, symbol)
        self.assertNotIn((row, col), self.board.available_squares)
        for i in range (-1, 2):
            for j in range (-1, 2):
                if not (i == 0 and j == 0):
                    if ((0 <= row + i < self.board.height) and (0 <= col + j < self.board.width)):
                        self.assertNotIn((row + i, col + j), self.board.available_squares)


class RandomComputerPlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board()
        self.computer = RandomComputerPlayer(self.board)

    def test_valid_computer_move(self):
        self.computer.move()
        coordinates_of_move = (-1, -1)
        for i in range (self.board.height):
            for j in range (self.board.width):
                if self.board.get_square(i, j) == 'O':
                    coordinates_of_move = (i, j)
        self.assertGreaterEqual(coordinates_of_move[0], 0)
        self.assertGreaterEqual(coordinates_of_move[1], 0)
        self.assertLessEqual(coordinates_of_move[0], self.board.height)
        self.assertLessEqual(coordinates_of_move[1], self.board.width)


if __name__ == "__main__":
    unittest.main()