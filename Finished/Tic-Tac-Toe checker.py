def checker(c):
    if (c[0] == c[3] == c[6] and c[1] == c[4] == c[7]) or \
            (c.count('O') - c.count('X') > 1 or c.count('X') - c.count('O') > 1):
        return 'Impossible'
    elif c[0] == c[1] == c[2] != '_':  # checks top
        return f'{c[0]} wins'
    elif c[3] == c[4] == c[5] != '_':  # checks middle
        return f'{c[6]} wins'
    elif c[6] == c[7] == c[8] != '_':  # checks bottom
        return f'{c[7]} wins'
    elif c[0] == c[3] == c[6] != '_':  # checks down the left side
        return f'{c[0]} wins'
    elif c[1] == c[4] == c[7] != '_':  # checks down the middle
        return f'{c[1]} wins'
    elif c[2] == c[5] == c[8] != '_':  # checks down the right side
        return f'{c[2]} wins'
    elif c[6] == c[4] == c[2] != '_':  # checks diagonal
        return f'{c[6]} wins'
    elif c[0] == c[4] == c[8] != '_':  # checks diagonal
        return f'{c[0]} wins'
    else:
        if '_' in c:
            return 'Game not finished'
        else:
            return 'Draw'


board = list(input())

print(f"""---------
| {board[0]} {board[1]} {board[2]} |
| {board[3]} {board[4]} {board[5]} |
| {board[6]} {board[7]} {board[8]} |
---------""")
print(checker(board))


