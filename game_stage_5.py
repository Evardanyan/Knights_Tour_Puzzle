# Write your code here
import traceback


def knight_move():
    control_exit_from_loop = True
    try:
        while True:
            x1, y1 = input("Enter your board dimensions: ").split()
            x1 = int(x1)
            y1 = int(y1)
            if (x1 < 0 or x1 == 0) or (y1 < 0 or y1 == 0):
                print("Invalid dimensions!")
            else:
                break
        while control_exit_from_loop:
            x, y = input("Enter the knight's starting position: ").split()
            x1 = int(x1)
            y1 = int(y1)
            x = int(x)
            y = int(y)
            if (x > x1 or x <= 0) or (y > y1 or y <= 0):
                print("Invalid position!")
            else:
                cheese_board(x1, y1, x, y)
                count = 1
                while True:
                    # print()
                    # print("Here are the possible moves:")

                    # show_cheeseboard(x1, y1, x, y)
                    # break
                    x, y = input("Enter your next move: ").split()
                    x = int(x)
                    y = int(y)
                    # if x in moves_x and y in moves_y:
                    #     print("Invalid move!")
                    # else:
                    cheeseboard = cheese_board(x1, y1, x, y)
                    # if check_loose(cheeseboard, x1, y1, x, y):
                    # print(check_loose(cheeseboard, x1, y1))
                    if check_win(cheeseboard, x1, y1):
                        print(check_win(cheeseboard, x1, y1))
                        print("What a great tour! Congratulations!")
                        control_exit_from_loop = False
                        break
                    if check_loose(cheeseboard, x1, y1):
                        print("No more possible moves!")
                        count += 1
                        print(f"Your knight visited {count} squares!")
                        control_exit_from_loop = False
                        break
                    count += 1

    except Exception as e:
        print("Invalid dimensions")
        # print(e.with_traceback())
        # print(traceback.TracebackException)
        knight_move()


def start():
    x1, y1 = input("Enter your board dimensions: ").split()
    x1 = int(x1)
    y1 = int(y1)
    x, y = input("Enter the knight's starting position: ").split()
    x = int(x)
    y = int(y)
    cheese_board(x1, y1, x, y)
    count = 1
    while True:
        x, y = input("Enter your next move: ").split()
        x = int(x)
        y = int(y)
        # if x in moves_x and y in moves_y:
        #     print("Invalid move!")
        # else:
        cheeseboard = cheese_board(x1, y1, x, y)
        if check_loose(cheeseboard, x1, y1, x, y):
            print("No more possible moves!")
            print(f"Your knight visited {count} squares!")
            break
        count += 1
        if count == x1 * y1:
            print("What a great tour! Congratulations!")
            break


def check_combination(x, y, x1, y1, x_x, x_y):
    count = 0
    if y >= y1 - 2 > 0 and x >= x1 + 1 and (x1 + 1 != x_x or y1 - 2 != x_y):
        count += 1
    if y >= y1 - 2 > 0 and x >= x1 - 1 > 0 and (x1 - 1 != x_x or y1 - 2 != x_y):
        count += 1
    if y >= y1 + 2 and x >= x1 + 1 and (x1 + 1 != x_x or y1 + 2 != x_y):
        count += 1
    if y >= y1 + 2 and x >= x1 - 1 > 0 and (x1 - 1 != x_x or y1 + 2 != x_y):
        count += 1
    if y >= y1 - 1 > 0 and x >= x1 + 2 and (x1 + 2 != x_x or y1 - 1 != x_y):
        count += 1
    if y >= y1 - 1 > 0 and x >= x1 - 2 > 0 and (x1 - 2 != x_x or y1 - 1 != x_y):
        count += 1
    if y >= y1 + 1 and x >= x1 + 2 and (x1 + 2 != x_x or y1 + 1 != x_y):
        count += 1
    if y >= y1 + 1 and x >= x1 - 2 > 0 and (x1 - 2 != x_x or y1 + 1 != x_y):
        count += 1
    return count


def show_combination_on_cheeseboard(cheeseboard, x, y, x1, y1):
    x_x = x1
    x_y = y1
    if y > y - y1 - 2 >= 0 and x1 + 1 <= x:
        y2 = y1 + 2
        x2 = x1 + 1
        if cheeseboard[y - y1 - 2][x1 + 1] != " *":
            cheeseboard[y - y1 - 2][x1 + 1] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
    if y > y - y1 - 2 >= 0 and x1 - 1 <= x:
        y2 = y1 + 2
        x3 = x1 - 1
        if cheeseboard[y - y1 - 2][x1 - 1] != " *":
            cheeseboard[y - y1 - 2][x1 - 1] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
    if y > y - y1 + 2 >= 0 and x1 + 1 <= x:
        y2 = y1 - 2
        x2 = x1 + 1
        if cheeseboard[y - y1 + 2][x1 + 1] != " *":
            cheeseboard[y - y1 + 2][x1 + 1] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
    if y > y - y1 + 2 >= 0 and x1 - 1 <= x:
        y2 = y1 - 2
        x3 = x1 - 1
        if cheeseboard[y - y1 + 2][x1 - 1] != " *":
            cheeseboard[y - y1 + 2][x1 - 1] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
    if y > y - y1 - 1 >= 0 and x1 + 2 <= x:
        y2 = y1 + 1
        x2 = x1 + 2
        if cheeseboard[y - y1 - 1][x1 + 2] != " *":
            cheeseboard[y - y1 - 1][x1 + 2] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
    if y > y - y1 - 1 >= 0 and x1 - 2 <= x:
        y2 = y1 + 1
        x3 = x1 - 2
        if cheeseboard[y - y1 - 1][x1 - 2] != " *":
            cheeseboard[y - y1 - 1][x1 - 2] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
    if y > y - y1 + 1 >= 0 and x1 + 2 <= x:
        y2 = y1 - 1
        x2 = x1 + 2
        if cheeseboard[y - y1 + 1][x1 + 2] != " *":
            cheeseboard[y - y1 + 1][x1 + 2] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
    if y > y - y1 + 1 >= 0 and x1 - 2 <= x:
        y2 = y1 - 1
        x3 = x1 - 2
        if cheeseboard[y - y1 + 1][x1 - 2] != " *":
            cheeseboard[y - y1 + 1][x1 - 2] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
    return cheeseboard


def clear_combination_on_cheeseboard(cheeseboard, x, y, x1, y1):
    x_x = x1
    x_y = y1
    if y > y - y1 - 2 >= 0 and x1 + 1 <= x:
        y2 = y1 + 2
        x2 = x1 + 1
        if cheeseboard[y - y1 - 2][x1 + 1] != " *":
            cheeseboard[y - y1 - 2][x1 + 1] = "__"
    if y > y - y1 - 2 >= 0 and x1 - 1 <= x:
        y2 = y1 + 2
        x3 = x1 - 1
        if cheeseboard[y - y1 - 2][x1 - 1] != " *":
            cheeseboard[y - y1 - 2][x1 - 1] = "__"
    if y > y - y1 + 2 >= 0 and x1 + 1 <= x:
        y2 = y1 - 2
        x2 = x1 + 1
        if cheeseboard[y - y1 + 2][x1 + 1] != " *":
            cheeseboard[y - y1 + 2][x1 + 1] = "__"
    if y > y - y1 + 2 >= 0 and x1 - 1 <= x:
        y2 = y1 - 2
        x3 = x1 - 1
        if cheeseboard[y - y1 + 2][x1 - 1] != " *":
            cheeseboard[y - y1 + 2][x1 - 1] = "__"
    if y > y - y1 - 1 >= 0 and x1 + 2 <= x:
        y2 = y1 + 1
        x2 = x1 + 2
        if cheeseboard[y - y1 - 1][x1 + 2] != " *":
            cheeseboard[y - y1 - 1][x1 + 2] = "__"
    if y > y - y1 - 1 >= 0 and x1 - 2 <= x:
        y2 = y1 + 1
        x3 = x1 - 2
        if cheeseboard[y - y1 - 1][x1 - 2] != " *":
            cheeseboard[y - y1 - 1][x1 - 2] = "__"
    if y > y - y1 + 1 >= 0 and x1 + 2 <= x:
        y2 = y1 - 1
        x2 = x1 + 2
        if cheeseboard[y - y1 + 1][x1 + 2] != " *":
            cheeseboard[y - y1 + 1][x1 + 2] = "__"
    if y > y - y1 + 1 >= 0 and x1 - 2 <= x:
        y2 = y1 - 1
        x3 = x1 - 2
        if cheeseboard[y - y1 + 1][x1 - 2] != " *":
            cheeseboard[y - y1 + 1][x1 - 2] = "__"
    return cheeseboard


def check_knight_move(cheeseboard, x, y, x1, y1):
    x_x = x1
    x_y = y1
    if y > y - y1 - 2 >= 0 and x1 + 1 <= x:
        y2 = y1 + 2
        x2 = x1 + 1
        if cheeseboard[y - y1 - 2][x1 + 1] != " *":
            cheeseboard[y - y1 - 2][x1 + 1] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
    if y > y - y1 - 2 >= 0 and x1 - 1 <= x:
        y2 = y1 + 2
        x3 = x1 - 1
        if cheeseboard[y - y1 - 2][x1 - 1] != " *":
            cheeseboard[y - y1 - 2][x1 - 1] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
    if y > y - y1 + 2 >= 0 and x1 + 1 <= x:
        y2 = y1 - 2
        x2 = x1 + 1
        if cheeseboard[y - y1 + 2][x1 + 1] != " *":
            cheeseboard[y - y1 + 2][x1 + 1] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
    if y > y - y1 + 2 >= 0 and x1 - 1 <= x:
        y2 = y1 - 2
        x3 = x1 - 1
        if cheeseboard[y - y1 + 2][x1 - 1] != " *":
            cheeseboard[y - y1 + 2][x1 - 1] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
    if y > y - y1 - 1 >= 0 and x1 + 2 <= x:
        y2 = y1 + 1
        x2 = x1 + 2
        if cheeseboard[y - y1 - 1][x1 + 2] != " *":
            cheeseboard[y - y1 - 1][x1 + 2] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
    if y > y - y1 - 1 >= 0 and x1 - 2 <= x:
        y2 = y1 + 1
        x3 = x1 - 2
        if cheeseboard[y - y1 - 1][x1 - 2] != " *":
            cheeseboard[y - y1 - 1][x1 - 2] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
    if y > y - y1 + 1 >= 0 and x1 + 2 <= x:
        y2 = y1 - 1
        x2 = x1 + 2
        if cheeseboard[y - y1 + 1][x1 + 2] != " *":
            cheeseboard[y - y1 + 1][x1 + 2] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
    if y > y - y1 + 1 >= 0 and x1 - 2 <= x:
        y2 = y1 - 1
        x3 = x1 - 2
        if cheeseboard[y - y1 + 1][x1 - 2] != " *":
            cheeseboard[y - y1 + 1][x1 - 2] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
    return cheeseboard


def show_cheeseboard(x, y, x1, y1):
    x_x = x1
    # x_y = y - y1
    x_y = y1
    if x > 9 and y > 9:
        cheeseboard = [["___" for i in range(x + 2)] for j in range(y)]
        cheeseboard[y - y1][x1] = "  X"
        if y - y1 - 2 < y and x1 + 1 <= x and x1 - 1 <= x:
            y2 = y - y1 - 2
            x2 = x1 + 1
            # check_combination(x, y. x2, y2)
            # cheeseboard[y - y1 - 2][x1 + 1] = " O"
            cheeseboard[y - y1 - 2][x1 + 1] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
            cheeseboard[y - y1 - 2][x1 - 1] = " O"
        if y - y1 + 2 < y and x1 + 1 <= x and x1 - 1 <= x:
            cheeseboard[y - y1 + 2][x1 + 1] = " O"
            cheeseboard[y - y1 + 2][x1 - 1] = " O"
        if y - y1 - 1 < y and x1 + 2 <= x and x1 - 2 <= x:
            cheeseboard[y - y1 - 1][x1 + 2] = " O"
            cheeseboard[y - y1 - 1][x1 - 2] = " O"
        if y - y1 + 1 < y and x1 + 2 <= x and x1 - 2 <= x:
            cheeseboard[y - y1 + 1][x1 + 2] = " O"
            cheeseboard[y - y1 + 1][x1 - 2] = " O"
    else:
        cheeseboard = [["__" for i in range(x + 2)] for j in range(y)]
        cheeseboard[y - y1][x1] = " X"
        if y > y - y1 - 2 >= 0 and x1 + 1 <= x and x1 - 1 <= x:
            y2 = y1 + 2
            x2 = x1 + 1
            x3 = x1 - 1
            cheeseboard[y - y1 - 2][x1 + 1] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
            cheeseboard[y - y1 - 2][x1 - 1] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
            # cheeseboard[y - y1 - 2][x1 + 1] = " O"
            # cheeseboard[y - y1 - 2][x1 - 1] = " O"
        if y > y - y1 + 2 >= 0 and x1 + 1 <= x and x1 - 1 <= x:
            # y2 = y - y1 + 2
            y2 = y1 - 2
            x2 = x1 + 1
            x3 = x1 - 1
            cheeseboard[y - y1 + 2][x1 + 1] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
            cheeseboard[y - y1 + 2][x1 - 1] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
            # cheeseboard[y - y1 + 2][x1 + 1] = " O"
            # cheeseboard[y - y1 + 2][x1 - 1] = " O"
        if y > y - y1 - 1 >= 0 and x1 + 2 <= x and x1 - 2 <= x:
            # y2 = y - y1 - 1
            y2 = y1 + 1
            x2 = x1 + 2
            x3 = x1 - 2
            cheeseboard[y - y1 - 1][x1 + 2] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
            cheeseboard[y - y1 - 1][x1 - 2] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
            # cheeseboard[y - y1 - 1][x1 + 2] = " O"
            # cheeseboard[y - y1 - 1][x1 - 2] = " O"
        if y > y - y1 + 1 >= 0 and x1 + 2 <= x and x1 - 2 <= x:
            # y2 = y - y1 + 1
            y2 = y1 - 1
            x2 = x1 + 2
            x3 = x1 - 2
            cheeseboard[y - y1 + 1][x1 + 2] = f" {check_combination(x, y, x2, y2, x_x, x_y)}"
            cheeseboard[y - y1 + 1][x1 - 2] = f" {check_combination(x, y, x3, y2, x_x, x_y)}"
            # cheeseboard[y - y1 + 1][x1 + 2] = " O"
            # cheeseboard[y - y1 + 1][x1 - 2] = " O"
    new_val = [y - i for i in range(y)]
    for new_val, subList in zip(new_val, cheeseboard):
        subList[0] = f"{new_val}|"
        subList[x + 1] = f"|"
    print("", ((x * 3) + 3) * "-")
    count = y
    for i in cheeseboard:
        clean_comma = ", ".join(i)
        print(clean_comma.replace(", ", " "))
        count -= 1
    print("", ((x * 3) + 3) * "-")
    horizontal_number = "    "
    for i in range(1, x + 1):
        horizontal_number = horizontal_number + str(i) + "  "
    horizontal_number.rstrip()
    print(horizontal_number)


def multiple_move(board_x, board_y, move_x, move_y):
    show_cheeseboard(board_x, board_y, move_x, move_y)
    while True:
        x, y = input("Enter your next move: ").split()
        move_x = int(x)
        move_y = int(y)
        show_cheeseboard(board_x, board_y, move_x, move_y)


moves_x = []
moves_y = []


def cheese_board(board_x, board_y, move_x, move_y):
    moves_x.append(move_x)
    moves_y.append(move_y)
    prev_move_x = []
    prev_move_y = []
    if len(moves_x) > 1:
        for i in moves_x[:-1]:
            prev_move_x.append(i)
        for j in moves_y[:-1]:
            prev_move_y.append(j)

        cheeseboard = [["__" for i in range(board_x + 2)] for j in range(board_y)]

        for i, j in zip(prev_move_x, prev_move_y):
            # cheeseboard = show_combination_on_cheeseboard(cheeseboard, board_x, board_y, i, j)
            cheeseboard[board_y - j][i] = " *"

        for i, j in zip(moves_x, moves_y):
            # if (len(moves_x) == 1 and len(moves_y) == 1) or (i == moves_x[-1] and j == moves_y[-1]):
            # cheeseboard = show_combination_on_cheeseboard(cheeseboard, board_x, board_y, i, j)
            if i == moves_x[-1] and j == moves_y[-1]:
                cheeseboard = show_combination_on_cheeseboard(cheeseboard, board_x, board_y, prev_move_x[-1],
                                                              prev_move_y[-1])
                print(cheeseboard[board_y - j][i])

                # if cheeseboard[board_y - j][i] != "__" or cheeseboard[board_y - j][i] != " *":
                if any(map(str.isdigit, cheeseboard[board_y - j][i])):
                    cheeseboard = clear_combination_on_cheeseboard(cheeseboard, board_x, board_y, prev_move_x[-1],
                                                                   prev_move_y[-1])
                    cheeseboard = show_combination_on_cheeseboard(cheeseboard, board_x, board_y, i, j)
                    cheeseboard[board_y - j][i] = " X"
                else:
                    moves_x.pop()
                    moves_y.pop()
                    print("Invalid move!")
                    break
    # -------------------------------------------------------------------------------------------------------------------
    if len(moves_x) == 1:
        cheeseboard = [["__" for i in range(board_x + 2)] for j in range(board_y)]
        # print(len(cheeseboard[0]))
        # print(len(cheeseboard))
        for i, j in zip(moves_x, moves_y):
            if (len(moves_x) == 1 and len(moves_y) == 1) or (i == moves_x[-1] and j == moves_y[-1]):
                cheeseboard = show_combination_on_cheeseboard(cheeseboard, board_x, board_y, i, j)
                if cheeseboard[board_y - j][i] != "__" or cheeseboard[board_y - j][i] != " *":
                    cheeseboard[board_y - j][i] = " X"
            elif len(moves_x) > 1 and len(moves_y) > 1 and i != moves_x[:-1]:
                cheeseboard[board_y - j][i] = " *"
    new_val = [board_y - i for i in range(board_y)]
    for new_val, subList in zip(new_val, cheeseboard):
        subList[0] = f"{new_val}|"
        subList[board_x + 1] = f"|"
    print("", ((board_x * 3) + 3) * "-")
    count = board_y
    for i in cheeseboard:
        clean_comma = ", ".join(i)
        print(clean_comma.replace(", ", " "))
        count -= 1
    print("", ((board_x * 3) + 3) * "-")
    horizontal_number = "    "
    for i in range(1, board_x + 1):
        horizontal_number = horizontal_number + str(i) + "  "
    horizontal_number.rstrip()
    print(horizontal_number)
    return cheeseboard


def check_win(cheeseboard, x, y):
    count_star = 0
    count_x = 0
    count_move_end = 0
    for j in range(len(cheeseboard[0])):
        for i in range(len(cheeseboard)):

            if cheeseboard[i][j] == " *":
                count_star += 1
            elif cheeseboard[i][j] == " X":
                count_x += 1
    if count_star == x * y - 1 and count_x == 1:
        return True


def check_loose(cheeseboard, x, y):
    count_star = 0
    count_x = 0
    count_move_end = 0
    for j in range(1, len(cheeseboard[0])):
        for i in range(len(cheeseboard)):
            # if cheeseboard[i][j] != " *" and "|" not in cheeseboard[i][j] and cheeseboard[i][j] != "__" \
            #         and cheeseboard[i][j] != " X":
            if any(map(str.isdigit, cheeseboard[i][j])):
                count_move_end += 1
    if count_move_end == 0:
        return True
    else:
        return False


def check_loose_old(cheeseboard, x, y, x1, y1):
    possible_moves = 0
    if y > y - y1 - 2 >= 0 and x1 + 1 <= x:
        if cheeseboard[y - y1 - 2][x1 + 1] != " *" or "|" not in cheeseboard[y - y1 - 2][x1 + 1] or \
                cheeseboard[y - y1 - 2][x1 + 1] != "__":
            # print(cheeseboard[y - y1 - 2][x1 + 1])
            possible_moves += 1
    if y > y - y1 - 2 >= 0 and x1 - 1 <= x:
        if cheeseboard[y - y1 - 2][x1 - 1] != " *" or \
                "|" not in cheeseboard[y - y1 - 2][x1 - 1] or cheeseboard[y - y1 - 2][x1 - 1] != "__":
            # print(cheeseboard[y - y1 - 2][x1 - 1])
            possible_moves += 1
    if y > y - y1 + 2 >= 0 and x1 + 1 <= x:
        if cheeseboard[y - y1 + 2][x1 + 1] != " *" or "|" not in cheeseboard[y - y1 + 2][x1 + 1] or "__" != \
                cheeseboard[y - y1 + 2][x1 + 1]:
            # print(cheeseboard[y - y1 + 2][x1 + 1])
            possible_moves += 1
    if y > y - y1 + 2 >= 0 and x1 - 1 <= x:
        if cheeseboard[y - y1 + 2][x1 - 1] != " *" or "|" not in cheeseboard[y - y1 + 2][x1 - 1] or " __" != \
                cheeseboard[y - y1 + 2][x1 - 1]:
            # print(cheeseboard[y - y1 + 2][x1 - 1])
            possible_moves += 1
    if y > y - y1 - 1 >= 0 and x1 + 2 <= x:
        if cheeseboard[y - y1 - 1][x1 + 2] != " *" or "|" not in cheeseboard[y - y1 - 1][x1 + 2] or "__" != \
                cheeseboard[y - y1 - 1][x1 + 2]:
            # print(cheeseboard[y - y1 - 1][x1 + 2])
            possible_moves += 1
    if y > y - y1 - 1 >= 0 and x1 - 2 <= x:
        if cheeseboard[y - y1 - 1][x1 - 2] != " *" or \
                "|" not in cheeseboard[y - y1 - 1][x1 - 2] or cheeseboard[y - y1 - 1][x1 - 2] != "__":
            # print(cheeseboard[y - y1 - 1][x1 - 2])
            possible_moves += 1
    if y > y - y1 + 1 >= 0 and x1 + 2 <= x:
        if cheeseboard[y - y1 + 1][x1 + 2] != " *" or \
                "|" not in cheeseboard[y - y1 + 1][x1 + 2] or cheeseboard[y - y1 + 1][x1 + 2] != "__":
            # print(cheeseboard[y - y1 + 1][x1 + 2])
            possible_moves += 1
    if y > y - y1 + 1 >= 0 and x1 - 2 <= x:
        if cheeseboard[y - y1 + 1][x1 - 2] != " *" or \
                "|" not in cheeseboard[y - y1 + 1][x1 - 2] or cheeseboard[y - y1 + 1][x1 - 2] != "__":
            # print(cheeseboard[y - y1 + 1][x1 - 2])
            possible_moves += 1
    if possible_moves > 0:
        return False
    return True


# def start():
#     x1, y1 = input("Enter your board dimensions: ").split()
#     x1 = int(x1)
#     y1 = int(y1)
#     x, y = input("Enter the knight's starting position: ").split()
#     x = int(x)
#     y = int(y)
#     cheese_board(x1, y1, x, y)
#     count = 1
#     while True:
#         x, y = input("Enter your next move: ").split()
#         x = int(x)
#         y = int(y)
#         if x in moves_x and y in moves_y:
#             print("Invalid move!")
#         else:
#             cheeseboard = cheese_board(x1, y1, x, y)
#             if check_loose(cheeseboard, x1, y1, x, y):
#                 print("No more possible moves!")
#                 print("Your knight visited 4 squares!")
#                 break
#             count += 1
#             if count == x1 * y1:
#                 print("What a great tour! Congratulations!")
#                 break


# start()
# show_cheeseboard(4, 4, 2, 2)
knight_move()
