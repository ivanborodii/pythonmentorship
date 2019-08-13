import re
from itertools import chain
from functools import reduce

attempt=0
y='' # global value for saving entered by user word

def Main():
    global y
    s=EnterWord()
    y=s
    ComputerGuessing(len(str(s)))

def EnterWord(): # function where user is entering word
    player_word = input(str('Enter the word: '))
    regexp = re.compile(player_word)
    c=0
    f=open('hangman_list.txt','r')
    for line in f.readlines():
        line = line.rstrip() # delete \n from word for correct comparison with entered by user word
        if regexp.fullmatch(line): # analyze if user entered word which located in txt file
            c+=1
            if c==1:
                print('The word is present in the game list.')
                return player_word
    if c==0:
        print('Unfortunately, the word {} is absent in the game list. Please try again.'.format(player_word))
        ew=EnterWord()
        return ew
    f.close()

def ComputerGuessing(d): # function for execution the first attempt to guess the word by computer (if user doesn't give prompt after the first attempt the function is executing again)
                         # this fuction is getting the length guessed word
    global attempt,y
    print('PROMPT FOR COMPUTER: THE WORD CONTAINS {} LETTERS'.format(d))
    print('COMPUTER IS GUESSING...')
    list1,letters,words=[],[],[] # list1 will contain the list guessing words,
                                 # letters - list of letters which formed from list1,
                                 # words - for counting the letter which occurs the most often
    f = open('hangman_list.txt', 'r')
    for line in f.readlines():
        line = line.rstrip()
        if len(line)==d:
            list1.append(line)
    letters=list(chain(*list1))
    k = [(i, letters.count(i)) for i in set(letters)] # create list of tuples (letter, count)
    k.sort(key=lambda x: -x[1])                       # order by count of letters
    for word in list1:
        words.append((word, word.count(k[0][0]))) # create list of tuples (word, count)
    words.sort(key=lambda x: -x[1])               # ordered by the most repeatable letter
    w = words[0][0] # computer is choosing the word which contain the letter which is the repeatable in list1
    print('GUESSING WORD IS {}'.format(w))
    attempt+=1
    if w==y:
        print('COMPUTER HAS GUESSED THE WORD USING {} ATTEMPT.'.format(attempt))
    else:
        list1.remove(w) # delete guessed by computer word from list1
        print("COMPUTER HASN'T GUESSED THE WORD.")
        LetterPrompt(list1) # give list1 to another fuction

def LetterPrompt(list1): # the function is using prompts from user who is indicating letters in guessing word
    global attempt,y
    letters,words,positions=[],[],[] # letters - list of letters which formed from list1 excluding prompted letters,
                                     # words - for counting the letter which occurs the most often,
                                     # positions - for indicating positions of prompted letters
    t=input(str("DO YOU WANT TO GIVE COMPUTER ONE MORE PROMPT? y/n"))
    if t=='y': # in this case computer is finding guessed word using reduce operator
        ltr = input(str("PLEASE, LET COMPUTER KNOW SOME LETTER IN GUESSED WORD:"))
        if ltr in y:
             for i in range(len(y)):
                 if y[i]==ltr:
                     positions.append(i+1)
             print("THE LETTER '{}' IS LOCATED IN POSITIONS NUMBER {}.".format(ltr, positions)) # user stopped to interact with computer
             ltrInd=re.compile(ltr) # computer starts to find the word
             for item in positions:
                list1=[i for i in list1 if ltrInd.match(i,item-1) and i.count(ltr)==len(positions)]
             ltrs=reduce(lambda a, b: a + b, list1)
             letters=[i for i in ltrs if i!=ltr]
             k = [(i, letters.count(i)) for i in set(letters)]  # create list of tuples (letter, count)
             k.sort(key=lambda x: -x[1])                        # order by count of letters
             for word in list1:
                 words.append((word, word.count(k[0][0])))  # create list of tuples (word, count)
             words.sort(key=lambda x: -x[1])                # ordered by the most repeatable letter
             w = words[0][0] # computer is choosing the word which contain the letter which is the repeatable in list1
             print('GUESSING WORD IS {}'.format(w))
             attempt+=1
             if w == y:
                 print('COMPUTER HAS GUESSED THE WORD USING {} ATTEMPTS.'.format(attempt))
             else:
                 list1.remove(w)
                 print("COMPUTER HASN'T GUESSED THE WORD.")
                 LetterPrompt(list1) # if guessed word is incorrect then execute function again
        else:
            print("YOU ENTERED THE LETTER WHICH NOT EXISTS IN THE WORD. PLEASE TRY AGAIN.")
            LetterPrompt(list1)
    elif t=='n': # for finding the word computer uses the same algorithm as in ComputerGuessing function
        letters = list(chain(*list1))
        k = [(i, letters.count(i)) for i in set(letters)]  # create list of tuples (letter, count)
        k.sort(key=lambda x: -x[1])                        # order by count of letters
        for word in list1:
            words.append((word, word.count(k[0][0])))  # create list of tuples (word, count)
        words.sort(key=lambda x: -x[1])                # ordered by the most repeatable letter
        w = words[0][0]
        print('GUESSING WORD IS {}'.format(w))
        attempt += 1
        if w == y:
            print('COMPUTER HAS GUESSED THE WORD USING {} ATTEMPTS.'.format(attempt))
        else:
            list1.remove(w)
            print("COMPUTER HASN'T GUESSED THE WORD.")
            LetterPrompt(list1) # if guessed word is incorrect then execute function again
    else:
        print('YOU ENTERED INVALID CHARACTER. PLEASE, USE y/n symbols')
        LetterPrompt(list1)

if __name__=='__main__': # determine start point
    Main()

