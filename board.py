from texttable import Texttable

class ObstructionError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class Board:
    def __init__(self, height: int = 6, width: int = 6) -> None:
        self.__height = height
        self.__width = width
        self.__board = [[' ' for i in range (width)] for j in range (height)]
        self.__available_squares = []
        for i in range (0, self.__height):
            for j in range (0, self.__width):
                self.__available_squares.append((i, j))

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value: int):
        self.__width = value

    @height.setter
    def height(self, value: int):
        self.__height = value
    
    @property
    def available_squares(self):
        return self.__available_squares.copy()
    
        
    def get_square(self, row: int, column: int):
        """Function that returns the value of the board at a given set of coordinates

        Args:
            row (int): the row coordinate
            column (int): the column coordinate

        Returns:
            str: the character for the board at (row, column)
        """
        return self.__board[row][column]
    
    
    def move(self, row: int, column: int, symbol: str):
        """Function that executes a move on the board

        Args:
            row (int): the row coordinate of the move
            column (int): the column coordinate of the move
            symbol (str): the symbol to place with the move

        Raises:
            ObstructionError: "Invalid row!" if the row coord. is invalid
            ObstructionError: "Invalid column!" if the column coord. is invalid
            ObstructionError: "The square is blocked!" if the square at the given coord. is already blocked
        """
        if not (0 <= row < self.__height):
            raise ObstructionError("Invalid row!")
        
        if not (0 <= column <= self.__width):
            raise ObstructionError("Invalid column!")
        
        if self.__board[row][column] != ' ':
            raise ObstructionError("The square is blocked!")
        
        self.__board[row][column] = symbol
        self.__available_squares.remove((row, column))
        for i in range (-1, 2):
            for j in range (-1, 2):
                if not (i == 0 and j == 0):
                    if ((0 <= row + i < self.__height) and (0 <= column + j < self.__width)):
                        self.__board[row + i][column + j] = '-'
                        if (row + i, column + j) in self.__available_squares:
                            self.__available_squares.remove((row + i, column + j))


    def __str__(self) -> str:
        """Function that returns the board as a texttable

        Returns:
            str: returns the texttable version of the board
        """
        table = Texttable()
        hrow = ['/']
        for i in range (self.__width):
            hrow.append(i)

        table.header(hrow)
        for i in range (self.__height):
            table.add_row([i] + self.__board[i])

        return table.draw()
    

        

        
