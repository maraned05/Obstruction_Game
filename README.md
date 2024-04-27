# Obstruction_Game
A simple Python implementation of the Obstruction game. (http://www.papg.com/show?2XMX)

There isn't a GUI implemented yet. The game is played through the terminal.

Firstly, you have to introduce the size of the grid you want to play on. (two integers separated by space, representing the no. of rows, respectively the no. of columns)
Then, you have the option to choose whether you are the one to make the first move, or the computer.
A move is represented by a tuple of integers, similarly to chess. (the number of the row, followed by the number of the column)
The board is displayed after each move.

The game ends when one of the participants (player or computer) has no space left for a move, and a message is displayed accordingly.

The computer player is not implemented with an AI, it makes a move randomly. Still, whenever possible for it to win in a single move, it takes the chance to win.
