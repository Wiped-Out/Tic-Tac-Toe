class TicTacToe:
    def __init__(self, cells):
        board = [list(cells)[i:i + 3] for i in range(0, 9, 3)]
        row1 = [board[2][0], board[1][0], board[0][0]]
        row2 = [board[2][1], board[1][1], board[0][1]]  # I should find a way to make this less ugly...
        row3 = [board[2][2], board[1][2], board[0][2]]
        self.matrix = [row1, row2, row3]

    def __str__(self):
        return f'''\n---------
        | {self.matrix[0][2]} {self.matrix[1][2]} {self.matrix[2][2]} |
        | {self.matrix[0][1]} {self.matrix[1][1]} {self.matrix[2][1]} |
        | {self.matrix[0][0]} {self.matrix[1][0]} {self.matrix[2][0]} |
        ---------'''

    def start(self):
        print(self)
        while True:
            try:
                x, y = [int(n) - 1 for n in input('Enter the coordinates: ').split()]
            except (NameError, ValueError):
                print('You should enter numbers!')
                continue
            if x >= 3 or y >= 3:  # greater or equal than because list comprehension takes 1 out of n
                print('Coordinates should be from 1 to 3!')
                continue
            if any(l in self.matrix[x][y] for l in ('X', 'O')):
                print('This cell is occupied! Choose another one!')
                continue
            break
        self.matrix[x][y] = 'X'
        print(self)


game = TicTacToe(input('Enter cells: ')).start()
