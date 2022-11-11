XPosition = [0, 0, 0, 0, 0, 0, 0, 0, 0]
OPosition = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = True

print(f"1 | 2 | 3")
print(f"--|---|--")
print(f"4 | 5 | 6")
print(f"--|---|--")
print(f"7 | 8 | 9")


def printBoard(XPosition, OPosition):
    one = 'X' if XPosition[0] else ('O' if OPosition[0] else 1)
    two = 'X' if XPosition[1] else ('O' if OPosition[1] else 2)
    three = 'X' if XPosition[2] else ('O' if OPosition[2] else 3)
    four = 'X' if XPosition[3] else ('O' if OPosition[3] else 4)
    five = 'X' if XPosition[4] else ('O' if OPosition[4] else 5)
    six = 'X' if XPosition[5] else ('O' if OPosition[5] else 6)
    seven = 'X' if XPosition[6] else ('O' if OPosition[6] else 7)
    eight = 'X' if XPosition[7] else ('O' if OPosition[7] else 8)
    nine = 'X' if XPosition[8] else ('O' if OPosition[8] else 9)
    print(f"{one} | {two} | {three}")
    print(f"--|---|--")
    print(f"{four} | {five} | {six}")
    print(f"--|---|--")
    print(f"{seven} | {eight} | {nine}")


def getInput():
    global XPosition, OPosition, turn
    if turn:
        xChance = True

        def xTurn():
            nonlocal xChance
            print("Turn for X")
            Position = int(
                input("Input the position where you want to place 'X' : "))
            if Position <= 0 or Position > 9:
                print("Invalid Input")
                xTurn()
            elif XPosition[Position - 1] == 0 and OPosition[Position - 1] == 0:
                XPosition[Position - 1] = 1
            else:
                print("Place Already Occupied !")
                xTurn()
                xChance = False
        if xChance:
            xTurn()
        turn = False
    else:
        oChance = True

        def oTurn():
            print("Turn for O")
            Position = int(
                input("Enter the position where you want to place 'O' : "))
            if Position <= 0 or Position > 9:
                print("Invalid Input")
                oTurn()
            elif XPosition[Position - 1] == 0 and OPosition[Position - 1] == 0:
                OPosition[Position - 1] = 1
            else:
                print("Place Already Occupied !")
                oTurn()
        if oChance:
            oTurn()
        turn = True

    printBoard(XPosition, OPosition)
    # print(XPosition,  "\n",  OPosition)


win = False


def sum(a, b, c):
    return a + b + c

# winChck Function will check if someone has won the game or not;


def winCheck(XPosition, OPosition):
    global win
    # creating a array in which all the win possibilities will be mentioned ;
    # The array will contain all the combination of positions where the user will win the match;
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in wins:
        if sum(XPosition[i[0]], XPosition[i[1]], XPosition[i[2]]) == 3:
            win = True
            print("X Won")
        elif sum(OPosition[i[0]], OPosition[i[1]], OPosition[i[2]]) == 3:
            win = True
            print("O Won")


# firing getInput function in loop till anyone wins or the game ends in a draw
# after it fires the function, it will then call winCheck function to check if someone has won or not
chance = 1
while True:
    if chance <= 9:
        getInput()
        winCheck(XPosition, OPosition)
        if win == True:
            break
        chance = chance + 1
    else:
        print("Game Draw")
        break
