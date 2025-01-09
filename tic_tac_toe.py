"""Simple TicTacToe implementation for PvP."""

import enum
import os


class BoardOptions(enum.Enum):
    """Enumerator class for possible board cell options (including players)."""

    X: str = 'X'
    O: str = 'O'
    EMPTY: str = '-'


class TicTacToe:
    """TicTacToe class."""

    DRAW = 'Draw!'
    GRID_DIMENSION = 3
    INITIAL_STATUS = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    def __init__(self) -> None:
        """Initialize TicTacToe class."""

        self.grid = TicTacToe.INITIAL_STATUS
        self.player = BoardOptions.X.value

    def run(self) -> None:
        """Run TicTacToe game."""

        os.system('cls')
        TicTacToe.draw_board(grid=self.grid)

        while True:

            cell = input(f'Choice (player {self.player}): ').split(' ')
            x = int(cell[0])
            y = int(cell[1])

            if len(cell) != 2:
                print('Input should contain two values separated by space!')

            elif x not in [0, 1, 2] or y not in [0, 1, 2]:
                print('Value out of range! Use: 0, 1 or 2!')

            elif self.grid[x][y] != BoardOptions.EMPTY.value:
                print('Cell already occupied!')

            else:
                self.grid[x][y] = self.player

                os.system('cls')
                TicTacToe.draw_board(grid=self.grid)

                is_win, winner = TicTacToe.check_win(grid=self.grid, player=self.player)

                if is_win:
                    print(f'Player {BoardOptions.X.value if winner else BoardOptions.O.value} won!')
                    break

                elif not is_win and (winner == TicTacToe.DRAW):
                    print(TicTacToe.DRAW)
                    break

                self.player = TicTacToe.change_player(player=self.player)

    @staticmethod
    def change_player(player: str) -> str:
        """
        Change current player to opposite player.

        :param str player: current player
        :return: opposite player
        """

        if player == BoardOptions.X.value:
            return BoardOptions.O.value

        if player == BoardOptions.O.value:
            return BoardOptions.X.value

    @staticmethod
    def draw_board(grid: list[list[str]]) -> None:
        """
        Draw board using simple print() method.

        :param list[list[str]] grid: current grid status
        """

        for i, row in enumerate(grid):

            row_to_print = []

            for cell in row:

                if cell == BoardOptions.EMPTY.value:
                    row_to_print.append(' ')

                if cell == BoardOptions.X.value:
                    row_to_print.append(BoardOptions.X.value)

                if cell == BoardOptions.O.value:
                    row_to_print.append(BoardOptions.O.value)

            print(' | '.join(row_to_print))

            if i != len(grid) - 1:
                print(9 * '-')

    @staticmethod
    def check_win(grid: list[list[str]], player: str) -> tuple[bool, str]:
        """
        Check if current player win or check for a draw.

        :param list[list[str]] grid: current grid status
        :param str player: current player
        :return: tuple containing win status (True - win, False - not win yet) and player which win (or a draw)
        """

        result = False, ''

        # Check draw - only if there is no more empty cells
        if sum([1 for row in grid for cell in row if cell == BoardOptions.EMPTY.value]) == 0:
            result = False, TicTacToe.DRAW

        # Check rows
        for row in grid:
            score = [True for cell in row if cell == player]
            if len(score) == TicTacToe.GRID_DIMENSION:
                result = all(score), player

        # Check columns
        for column in range(TicTacToe.GRID_DIMENSION):
            score = [True for cell in [row[column] for row in grid] if cell == player]
            if len(score) == TicTacToe.GRID_DIMENSION:
                result = all(score), player

        # Check left diagonal
        score = [True for i in range(TicTacToe.GRID_DIMENSION) if grid[i][i] == player]
        if len(score) == TicTacToe.GRID_DIMENSION:
            result = all(score), player

        # Check right diagonal
        i, j = TicTacToe.GRID_DIMENSION - 1, 0
        score = []
        for _ in range(TicTacToe.GRID_DIMENSION):
            if grid[i][j] == player:
                score.append(True)
            i -= 1
            j += 1
        if len(score) == TicTacToe.GRID_DIMENSION:
            result = all(score), player

        return result
