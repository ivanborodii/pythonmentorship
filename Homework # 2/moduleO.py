from itertools import combinations

list_of_tuples = [(0, 1, 2), (0, 3, 6), (0, 4, 8), (1, 4, 7), (2, 4, 6), (2, 5, 8), (3, 4, 5),
                  (6, 7, 8)]  # all valid combinations for winning x-o-x

def TurnO(gameboard):
    try:
        b = int(input('Player 2: enter position for "O": '))
        if b in range(1,10): # valid positions: 1,2,3,4,5,6,7,8,9
            if not (gameboard[b - 1] == 'X' or gameboard[b - 1] == 'O'): # check if entered position is not filled by 'X' or 'O'
                gameboard[b - 1] = 'O'
                return gameboard # return modified by function gameboard
            else:
                print('This position has already filled. Please, try again')
                o=TurnO(gameboard) # if 'O' was entered on filled position then try to execute function again
                return o
        else:
            print('Invalid character was entered. Please, try again')
            o = TurnO(gameboard) # if was entered invalid character then try to execute function again
            return o
    except ValueError: # in this case except operator assumes that was entered not int type
        print('Invalid character was entered. Please, try again')
        o = TurnO(gameboard) # if was entered invalid character then try to execute function again
        return o

def IsWinO(gameboard):
    global list_of_tuples
    list_of_indexes = [] # this list is saving indexes of gameboard list where 'O' is determined
    for i in range(0, len(gameboard)):
        if gameboard[i]=='O':
            list_of_indexes.append(i)
    comb = combinations(list_of_indexes, 3) # creating list of tuples from 'O' indexes
    for i in comb:
        if i in list_of_tuples:
            print('PLayer 2 has won (O)') # if tuple of 'O' indexes belongs to valid combination for winning then the player has won
            return 1
    return 0