from moduleX import * # contains TurnX, IsWinX functions
from moduleO import * # contains TurnO, IsWinO functions

winX,winO,draw=0,0,0 # statistic variables for scoreboard

def Main():

    gameboard = []
    global winX,winO,draw
    for i in range(1, 10):
        gameboard.append(i)
    print("-------------")
    for i in range(3):
        print("|", gameboard[0 + i * 3], "|", gameboard[1 + i * 3], "|", gameboard[2 + i * 3], "|") # fill gameboard
    print("-------------")
    cntX,cntO=0,0 # create counters for counting turns

    while True: # this loop is using during the moment when players make turns while the winner has not be determined

        gameboard=TurnX(gameboard) # TurnX function checks logic of turns in the gameboard by Player 1
        cntX+=1
        print("-------------")
        for i in range(3):
            print("|", gameboard[0 + i * 3], "|", gameboard[1 + i * 3], "|", gameboard[2 + i * 3], "|")
        print("-------------")
        if cntX>=3: # if player made equal or more 3 turns then check did the player win
            boolX=IsWinX(gameboard) # IsWinX function checks if Player 1 won the party
            if boolX==1: # if IsWinX returned 1 then Player 1 won the party
                winX+=1
                break
            if cntX==5: # if all turns were made and winner was not determined then draw
                print('Draw')
                draw+=1
                break

        gameboard=TurnO(gameboard)# TurnO function checks logic of turns in the gameboard by Player 2
        cntO+=1
        print("-------------")
        for i in range(3):
            print("|", gameboard[0 + i * 3], "|", gameboard[1 + i * 3], "|", gameboard[2 + i * 3], "|")
        print("-------------")
        if cntO>=3: # if player made equal or more 3 turns then check did the player win
            boolO=IsWinO(gameboard) # IsWinO function checks if Player 2 won the party
            if boolO == 1: # if IsWinO returned 1 then Player 2 won the party
                winO+=1
                break

    Scoreboard(winX, winO, draw)  # transfer statistic variables to Scoreboard function


def Scoreboard(winX, winO, draw): # function for creating scoreboard and make posibility to play the new party or finish the game
    print("-------------")
    print('Scoreboard:')
    print('X-{}, O-{}, Draw-{}'.format(winX, winO, draw))
    print("-------------")
    s = input('Do You want to play one more party? (y/n) ')
    if s == 'y' or s == 'Y':
        Main() # play one more party
    elif s == 'n' or s == 'N':
        pass # quit from the game
    else:
        print('Invalid character was entered. Please, try again')
        x = Scoreboard(winX, winO, draw)
        return x


if __name__=='__main__': # determine start point
    Main()