from board import *
import random

class GameOver(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class Check_Win:
    def __init__(self, board: Board) -> None:
        self.__board = board

    def search_squares(self):
        """Function that places an optimal move for a win, if possible

        Returns:
            tuple: the tuple of coordinates where the move should be placed
        """
        ok = 1
        min_row = 100; min_col = 100
        max_row = -1; max_col = -1
        if len(self.__board.available_squares) <= 9:
            for x in self.__board.available_squares:
                for y in self.__board.available_squares:
                    if (abs(x[0] - y[0]) > 2) or (abs(x[1] - y[1]) > 2):
                        ok = 0

                    if x[0] > max_row:
                        max_row = x[0]
                    if y[0] > max_row:
                        max_row = y[0]
                    if x[0] < min_row:
                        min_row = x[0]
                    if y[0] < min_row:
                        min_row = y[0]
                    if x[1] > max_col:
                        max_col = x[1]
                    if y[1] > max_col:
                        max_col = y[1]
                    if x[1] < min_col:
                        min_col = x[1]
                    if y[1] < min_col:
                        min_col = y[1]
        else:
            ok = 0      
        
        if ok == 0:
            return (-1, -1)
        else:
            return ((max_row + min_row) // 2, (max_col + min_col) // 2)


class ComputerPlayer:
    def __init__(self, game_board: Board) -> None:
        self._symbol = 'O'
        self._board = game_board
        

class RandomComputerPlayer(ComputerPlayer):
    def __init__(self, game_board: Board) -> None:
        super().__init__(game_board)

    def move(self):
        """Function that places a move for the computer player

        Raises:
            GameOver: "Game over: Player wins!" if there are no more available squares on the board
        """
        if len(self._board.available_squares) == 0:
            raise GameOver("Game over: Player wins!")

        Checker = Check_Win(self._board)
        coordinates = Checker.search_squares()
        if coordinates != (-1, -1):
            self._board.move(coordinates[0], coordinates[1], self._symbol)
        else:
            row, col = random.choice(self._board.available_squares)
            self._board.move(row, col, self._symbol)

