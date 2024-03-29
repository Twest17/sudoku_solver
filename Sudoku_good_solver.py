def find_empty(table):
    for row in range(9):
        for column in range(9):
            if table[row][column] == 0:
                return row, column
    return None, None


def valid_guess(table, guess, row, column):
    if guess in table[row]:
        return False

    if guess in [table[i][column] for i in range(9)]:
        return False

    for r in range(3*(row // 3), 3*(row // 3)+3):
        for c in range(3*(column // 3), 3*(column // 3)+3):
            if guess == table[r][c]:
                return False
    return True


def main():
    # Easy
    # table = [[3, 8, 0, 1, 0, 0, 7, 0, 0],
    #          [0, 0, 0, 0, 0, 5, 0, 0, 4],
    #          [0, 6, 4, 0, 0, 0, 1, 0, 2],
    #          [4, 2, 0, 0, 5, 7, 0, 0, 0],
    #          [0, 0, 3, 0, 0, 0, 8, 0, 0],
    #          [0, 0, 0, 4, 3, 0, 0, 0, 7],
    #          [0, 0, 0, 0, 0, 2, 0, 6, 8],
    #          [0, 4, 7, 5, 1, 8, 0, 3, 9],
    #          [8, 9, 2, 6, 4, 0, 0, 7, 1]
    #          ]
    # MaxHard
    table = [[0, 1, 0, 0, 5, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 7, 2, 0, 0],
             [5, 0, 8, 9, 0, 0, 0, 0, 4],
             [0, 0, 0, 0, 9, 0, 0, 5, 0],
             [4, 0, 6, 5, 0, 0, 0, 0, 8],
             [3, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 3, 0, 6, 0, 0, 0, 0, 0],
             [6, 0, 1, 0, 2, 0, 4, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 0, 1]
             ]

    if solve(table):
        print('\nYour solution:')
        for row in table:
            print(row)
    else:
        print('not found solution')
    print('count guesses:', count)


count = 0


def solve(table):
    row, column = find_empty(table)
    if row is None:
        return True  # Solved

    for guess in range(1, 10):
        global count
        count += 1
        if valid_guess(table, guess, row, column):
            table[row][column] = guess
            if solve(table):
                return True
            table[row][column] = 0
    return False


main()
