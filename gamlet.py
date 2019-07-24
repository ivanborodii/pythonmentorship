separators=[' ', ',', '.', ';', ':', '[', ']','{', '}', '(', ')', '!', '?', '-','...','\'','\n','\t']
f = open('Book.txt','r')
text=f.read()
f.close()
text = [i for i in text]                          # splitting txt file into list of characters
word=''                                           # variable for creating word for further appending into list
words = []                                        # list for storing words
for i in text:
    if i not in separators:                       # if character is not a separator
        word=word+i                               # then append character to word variable
    else:
        words.append(word.upper())                # if character is not a separator then append word to list with words
        word=''                                   # make len(word)=0 and start to create a new word again
words = [i for i in words if i!='']               # clean list from empty values
k=[(i,words.count(i)) for i in set(words)]        # create tuples of list with couple (word, count)
k.sort(key=lambda x: -x[1])                       # sort the list in descending order by count
f1 = open('Result.txt','w+')                      # create txt file with result set
for i in range(len(k)):
    f1.write(str(k[i][0]) + ' ' + str(k[i][1]) + ' ' + 'times\n')   # write into txt file sorted list of tuples
f1.close()