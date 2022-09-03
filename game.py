# Write your code here
def knight_move():
    try:
        x, y = input("Enter the knight's starting position: ").split()
        x = int(x)
        y = int(y)
        if (x > 8 or x < 0) or (y > 8 or y < 0):
            print("Invalid dimensions!")
        else:
            show_cheeseboard(x, y)
    except ValueError:
        print("Invalid dimensions")


def show_cheeseboard(x, y):
    cheese_board = [[" ", "-------------------"],
                    [" 8|", "_", "_", "_", "_", "_", "_", "_", "_", "|"],
                    [" 7|", "_", "_", "_", "_", "_", "_", "_", "_", "|"],
                    [" 6|", "_", "_", "_", "_", "_", "_", "_", "_", "|"],
                    [" 5|", "_", "_", "_", "_", "_", "_", "_", "_", "|"],
                    [" 4|", "_", "_", "_", "_", "_", "_", "_", "_", "|"],
                    [" 3|", "_", "_", "_", "_", "_", "_", "_", "_", "|"],
                    [" 2|", "_", "_", "_", "_", "_", "_", "_", "_", "|"],
                    [" 1|", "_", "_", "_", "_", "_", "_", "_", "_", "|"],
                    [" ", "-------------------"],
                    ["   ", "1", "2", "3", "4", "5", "6", "7", "8", ]]
    cheese_board[9 - y][x] = "x"
    for i in cheese_board:
        clean_comma = ", ".join(i)
        print(clean_comma.replace(", ", " "))


knight_move()
