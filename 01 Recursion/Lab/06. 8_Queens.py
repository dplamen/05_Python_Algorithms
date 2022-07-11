def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def can_place_queen(row, col, rows, cols, left, right):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in left:
        return False
    if (row + col) in right:
        return False
    return True


def set_queen(row, col, board, rows, cols, left, right):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left.add(row - col)
    right.add(row + col)


def remove_queen(row, col, board, rows, cols, left, right):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left.remove(row - col)
    right.remove(row + col)


def put_queens(row, board, rows, cols, left, right):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(row, col, rows, cols, left, right):
            set_queen(row, col, board, rows, cols, left, right)
            put_queens(row + 1, board, rows, cols, left, right)
            remove_queen(row, col, board, rows, cols, left, right)


n = 8
board = []
[board.append(['-'] * 8) for _ in range(8)]

put_queens(0, board, set(), set(), set(), set())
