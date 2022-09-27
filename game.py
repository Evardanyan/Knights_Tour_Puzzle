# Write your code here
def knight_move():
    try:
        while True:
            x1, y1 = input("Enter your board dimensions: ").split()
            x1 = int(x1)
            y1 = int(y1)
            if (x1 < 0 or x1 == 0) or (y1 < 0 or y1 == 0):
                print("Invalid dimensions!")
            else:
                break
        while True:
            x, y = input("Enter the knight's starting position: ").split()
            x1 = int(x1)
            y1 = int(y1)
            x = int(x)
            y = int(y)

            if (x > x1 or x <= 0) or (y > y1 or y <= 0):
                print("Invalid position!")
            else:
                show_cheeseboard(x1, y1, x, y)
                break
    except ValueError:
        print("Invalid dimensions")


def show_cheeseboard(x, y, x1, y1):
    if x > 9 or y > 9:
        cheeseboard = [["___" for i in range(x + 2)] for j in range(y)]
        cheeseboard[y - y1][x1] = "  X"
        if y - y1 - 2 < y and x1 + 1 <= x and x1 - 1 <= x:
            cheeseboard[y - y1 - 2][x1 + 1] = " O"
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
            cheeseboard[y - y1 - 2][x1 + 1] = " O"
            cheeseboard[y - y1 - 2][x1 - 1] = " O"
        if y > y - y1 + 2 >= 0 and x1 + 1 <= x and x1 - 1 <= x:
            cheeseboard[y - y1 + 2][x1 + 1] = " O"
            cheeseboard[y - y1 + 2][x1 - 1] = " O"
        if y > y - y1 - 1 >= 0 and x1 + 2 <= x and x1 - 2 <= x:
            cheeseboard[y - y1 - 1][x1 + 2] = " O"
            cheeseboard[y - y1 - 1][x1 - 2] = " O"
        if y > y - y1 + 1 >= 0 and x1 + 2 <= x and x1 - 2 <= x:
            cheeseboard[y - y1 + 1][x1 + 2] = " O"
            cheeseboard[y - y1 + 1][x1 - 2] = " O"
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




# show_cheeseboard(4, 4, 2, 2)
knight_move()
