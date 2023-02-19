import random

board_squares = [[] for _ in range(9)]
full_rows = []


def generate_sudoku():
    # generating squares
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if any(board_squares):
        for elem in board_squares:
            elem.clear()
    if any(full_rows):
        full_rows.clear()

    for i in range(9):
        alt_nums = nums.copy()
        for j in range(9):
            num = random.choice(alt_nums)
            board_squares[i].append(str(num))
            alt_nums.remove(num)
    # generate board/row
    s = 0
    t = 3
    for n in range(3):
        r = 3
        p = 0
        for m in range(3):
            rows = []
            for i in range(s, t):
                for j in range(p, r):
                    rows.append(board_squares[i][j])
            full_rows.append(rows)
            p += 3
            r += 3
        s += 3
        t += 3


def show_board():
    for index, row in enumerate(full_rows):
        if index in [0, 3, 6]:
            print("-----------------")
        print('|'.join(row))
    print("-----------------")


def check_rows():
    for row in full_rows:
        check_list = []
        for elem in row:
            if elem not in check_list:
                check_list.append(elem)
            else:
                print("Rows aren't following rules of SUDOKU!")
                return False
    print("Rows are following rules of SUDOKU!")


def check_columns():
    for i in range(9):
        check_list = []
        for j in range(9):
            if full_rows[j][i] not in check_list:
                check_list.append(full_rows[j][i])
            else:
                print("Columns aren't following rules of SUDOKU!")
                return False
    print("Columns are following rules of SUDOKU!")


user_options = {
    's': show_board,
    'g': generate_sudoku,
    'r': check_rows,
    'c': check_columns,
}


def menu():
    menu_prompt = """
Pick one of the following_options:
's' to show sudoku board
'g' to generate new sudoku board
'r' to check if rows are following rules
'c' to check if columns are following rules
'q' to quit program
What do you want to do? """
    user_input = input(menu_prompt)
    generate_sudoku()
    while user_input != 'q':
        if user_input in user_options.keys():
            selected_action = user_options[user_input]
            selected_action()
        user_input = input(menu_prompt)


menu()

