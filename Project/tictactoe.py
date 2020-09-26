#!/usr/bin/env python3
from random import randint
from typing import Callable, Dict, List, Optional, Tuple


class Board(object):
    """
    Tic-Tac-Toe board
    """

    __board: List[str] = ['_' for _ in range(9)]
    wins: Tuple[Tuple[int, int, int], ...] = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def __repr__(self) -> str:
        return '''\t---------
        | {} {} {} |
        | {} {} {} |
        | {} {} {} |
        ---------'''.format(
            *self.__board
        )

    def clear(self) -> None:
        """Resets the board to its initial state."""
        self.__board = ['_' for _ in range(9)]

    def winner(self) -> Optional[str]:
        if self.__len__() == 0:
            return 'Draw'
        for w in self.wins:
            if all(self.__board[x] == 'X' for x in w):
                return 'X wins'
        for w in self.wins:
            if all(self.__board[x] == 'O' for x in w):
                return 'O wins'
        return None

    def __iter__(self):
        for i in self.__board:
            yield i

    def __getitem__(self, i: int) -> str:
        return self.__board[i]

    def __setitem__(self, i: int, item: str) -> None:
        self.__board[i] = item

    def is_free(self, i: int) -> bool:
        return self.__board[i] == '_'

    def __len__(self) -> int:
        """
        Returns the number of empty cells.
        """
        return self.__board.count('_')


class User:
    @staticmethod
    def move() -> int:
        """
        Gets coordinates from user input.
        """
        while True:
            try:
                x, y = [int(n) for n in input('Enter the coordinates: ').split()]
            except (NameError, ValueError):
                print('You should enter numbers!')
                continue
            if x > 3 or y > 3:
                print('Coordinates should be from 1 to 3!')
                continue
            cell: int = ((3 - y) * 3) + (x - 1)
            if not board.is_free(cell):
                print('This cell is occupied! Choose another one!')
                continue
            return cell


class EasyAI:
    @staticmethod
    def rand_nums() -> int:
        while True:
            cell = randint(0, 8)
            if board.is_free(cell):
                return cell

    def move(self) -> int:
        """
        Returns a random integer from 0 to 8.
        """
        print('Making move level "easy"')
        return self.rand_nums()


class MediumAI(EasyAI):
    def move(self) -> int:
        """Returns a random integer the first few rounds, then checks if it can win in one move or stop the enemy from winning."""
        print('Making move level "medium"')
        for lines in board.wins:
            win_lines = [board[i] for i in lines]
            try:
                if win_lines.count('X') == 2:
                    cell = lines[win_lines.index('_')]
                    return cell
                if win_lines.count('O') == 2:
                    cell = lines[win_lines.index('_')]
                    return cell
            except:
                continue
        return self.rand_nums()


class HardAI(MediumAI):
    outcomes: Dict[str, Tuple[int, int]] = {
        'X wins': (-1, 0),
        'O wins': (1, 0),
        'Draw': (0, 0),
    }

    def max(self, alpha, beta) -> Tuple[int, int]:
        # -1 - loss
        # 0 - draw
        # 1 - win

        maxv: int = -2

        cell: int = -1

        result = board.winner()

        if result:
            return self.outcomes[result]

        for i, item in enumerate(board):
            if item == '_':
                board[i] = 'O'
                m, _ = self.min(alpha, beta)
                if m > maxv:
                    maxv = m
                    cell = i
                board[i] = '_'

                if maxv >= beta:
                    return maxv, cell
                if maxv > alpha:
                    alpha = maxv
        return maxv, cell

    def min(self, alpha, beta) -> Tuple[int, int]:
        minv: int = 2

        cell: int = -1

        result = board.winner()

        if result:
            return self.outcomes[result]

        for i, item in enumerate(board):
            if item == '_':
                board[i] = 'X'
                m, _ = self.max(alpha, beta)
                if m < minv:
                    minv = m
                    cell = i
                board[i] = '_'

            if minv <= alpha:
                return minv, cell
            if minv < beta:
                beta = minv
        return minv, cell

    def move(self) -> int:
        print('Making move level "hard"')
        if turn == 'X':
            _, cell = self.min(-2, 2)
        else:
            _, cell = self.max(-2, 2)
        return cell


def game() -> str:
    global switch
    global turn
    while True:
        turn = 'X' if not switch else 'O'
        print(board)
        if len(board) <= 4:  # If the board has <= 4 spots, check if someone won or not.
            winner = board.winner()
            if winner is not None:
                return winner
        if not switch:
            cell = P1.move()
            board[cell] = turn
        else:
            cell = P2.move()
            board[cell] = turn
        switch = not switch


if __name__ == "__main__":
    difficulties: Dict[str, Callable] = {
        'user': User,
        'easy': EasyAI,
        'medium': MediumAI,
        'hard': HardAI,
    }
    turn: str
    while True:
        commands: List[str] = input("Input command: ").lower().split()
        if 'exit' in commands:
            exit('Bye!')
        board = Board()
        try:
            P1 = difficulties[commands[1]]()
            P2 = difficulties[commands[2]]()
        except:
            print("Unknown option")
            continue
        switch = False
        board.clear()
        print(game())