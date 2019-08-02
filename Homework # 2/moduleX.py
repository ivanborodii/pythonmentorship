from itertools import combinations

list_of_tuples = [(0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7), (2, 4, 6), (2, 5, 8), (3, 4, 5),
                  (6, 7, 8)]  # all valid combinations for winning x-o-x

def TurnX(gameboard):
    try:
        a = int(input('Player 1: enter position for "X": '))
        if a in range(1,10): # valid positions: 1,2,3,4,5,6,7,8,9
            if not (gameboard[a - 1] == 'X' or gameboard[a - 1] == 'O'): # check if entered position is not filled by 'X' or 'O'
                gameboard[a - 1] = 'X'
                return gameboard # return modified by function gameboard
            else:
                print('This position has already filled. Please, try again')
                x=TurnX(gameboard) # if 'X' was entered on filled position then try to execute function again
                return x
        else:
            print('Invalid character was entered. Please, try again')
            x = TurnX(gameboard) # if was entered invalid character then try to execute function again
            return x
    except ValueError: # in this case except operator assumes that was entered not int type
        print('Invalid character was entered. Please, try again')
        x = TurnX(gameboard) # if was entered invalid character then try to execute function again
        return x

def IsWinX(gameboard):
    global list_of_tuples
    list_of_indexes = [] # this list is saving indexes of gameboard list where 'X' is determined
    for i in range(0, len(gameboard)):
        if gameboard[i]=='X':
            list_of_indexes.append(i)
    comb = combinations(list_of_indexes, 3) # creating list of tuples from 'X' indexes
    for i in comb:
        if i in list_of_tuples: # if tuple of 'X' indexes belongs to valid combination for winning then the player has won
            print('PLayer 1 has won (X)')
            return 1
    return 0