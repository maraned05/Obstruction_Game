from board import *
from computer_player import *

class InputError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class UI:
    def __init__(self) -> None:
        self.__board = None
        self.__computer = None

    def get_input(self):
        """Function that retrieves two integers as input, representing the size of the board grid.
        (no. of rows followed by the no. of columns)

        Raises:
            InputError: if there are introduced more that two integers
            InputError: if the input isn't numerical

        Returns:
            list of str: a list with the two input numbers as strings
        """
        while True:
            sizes = input("Choose the side of the grid: ")
            sizes = sizes.split()
            try:
                if len(sizes) < 2:
                        raise InputError("Invalid input!")
                if not (sizes[0].isdigit() and sizes[1].isdigit()):
                    raise InputError("Invalid input!")
            except InputError as ex:
                print(ex)
                continue
            break

        return sizes
    

    def start(self):
        sizes = self.get_input()
        self.__board = Board(int(sizes[0]), int(sizes[1]))
        self.__computer = RandomComputerPlayer(self.__board)

        choice = input("Do you want to play first? (y/n) : ")
        try:
            if choice == "y":
                while True:
                    try:
                        print(self.__board)
                        if len(self.__board.available_squares) == 0:
                            raise GameOver("Game over: Computer wins!")
                        while True:
                            coordinates = input("Enter a position to move onto: ")
                            coordinates = coordinates.split()
                            try:
                                if len(coordinates) < 2:
                                        raise InputError("Invalid input!")
                                row = coordinates[0]
                                col = coordinates[1]
                                if not (row.isdigit() and col.isdigit()):
                                    raise InputError("Invalid input!")
                            except InputError as ex:
                                print(ex)
                                continue
                            row = int(row)
                            col = int(col)
                            try:
                                self.__board.move(row, col, 'X')
                            except Exception as ex:
                                print(ex)
                                continue
                            break
                        self.__computer.move()
                    except Exception as ex:
                        print("\n\n")
                        print(self.__board)
                        print(ex)
                        break

            elif choice == "n":
                while True:
                    try:
                        self.__computer.move()
                        print(self.__board)
                        if len(self.__board.available_squares) == 0:
                            raise GameOver("Game over: Computer wins!")
                        while True:
                            coordinates = input("Enter a position to move onto: ")
                            coordinates = coordinates.split()
                            try:
                                if len(coordinates) < 2:
                                        raise InputError("Invalid input!")
                                row = coordinates[0]
                                col = coordinates[1]
                                if not (row.isdigit() and col.isdigit()):
                                    raise InputError("Invalid input!")
                            except InputError as ex:
                                print(ex)
                                continue
                            row = int(row)
                            col = int(col)
                            try:
                                self.__board.move(row, col, 'X')
                            except Exception as ex:
                                print(ex)
                                continue
                            break
                    except GameOver as ex:
                        print("\n\n")
                        print(self.__board)
                        print(ex)
                        break

            else:
                raise InputError("Invalid command!")
            
        except Exception as ex:
            print(ex)
