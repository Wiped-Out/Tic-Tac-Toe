class TicTacToe:
    def __init__(self):
        board = [list('_' * 9)[i:i + 3] for i in range(0, 9, 3)]
        row1 = [board[2][0], board[1][0], board[0][0]]
        row2 = [board[2][1], board[1][1], board[0][1]]  # I should find a way to make this less ugly...
        row3 = [board[2][2], board[1][2], board[0][2]]
        self.matrix = [row1, row2, row3]

    def __str__(self):
        return f'''\n\t---------
        | {self.matrix[0][2]} {self.matrix[1][2]} {self.matrix[2][2]} |
        | {self.matrix[0][1]} {self.matrix[1][1]} {self.matrix[2][1]} |
        | {self.matrix[0][0]} {self.matrix[1][0]} {self.matrix[2][0]} |
        ---------'''

    def checker(self):
        # Check for X*3 in top, middle and bottom
        if any([self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == 'X' for i in range(3)]):
            print('X wins')
            exit()
        # Check for O*3 in top, middle and bottom
        if any([self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] == 'O' for i in range(3)]):
            print('O wins')
            exit()
        elif any([self.matrix[i] == ['X', 'X', 'X'] for i in range(3)]):  # checks for X down the left, middle
            # and right side
            print('X wins')
            exit()
        elif any([self.matrix[i] == ['O', 'O', 'O'] for i in range(3)]):  # same but for O
            print('O wins')
            exit()
        elif self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != '_':  # checks diagonal
            print(f'{self.matrix[0][2]} wins')
            exit()
        elif self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != '_':  # checks diagonal
            print(f'{self.matrix[0][0]} wins')
            exit()
        elif ((self.matrix[0].count('O') + self.matrix[1].count('O') + self.matrix[2].count('O')) +
              (self.matrix[0].count('X') + self.matrix[1].count('X') + self.matrix[2].count('X'))) == 9:
            print('Draw')
            exit()

    def start(self):
        print(self)
        moves = 1
        while True:
            try:
                x, y = [int(n) - 1 for n in input('Enter the coordinates: ').split()]
            except (NameError, ValueError):
                print('You should enter numbers!')
                continue
            if x >= 3 or y >= 3:  # greater or equal than because list comprehension takes 1 out of n
                print('Coordinates should be from 1 to 3!')
                continue
            if any(xo in self.matrix[x][y] for xo in ('X', 'O')):
                print('This cell is occupied! Choose another one!')
                continue
            else:
                if moves % 2 == 1:
                    self.matrix[x][y] = 'X'
                    print(self)
                    moves += 1
                else:
                    self.matrix[x][y] = 'O'
                    print(self)
                    moves += 1
                if moves >= 5:
                    self.checker()


TicTacToe().start()
