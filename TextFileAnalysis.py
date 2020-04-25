#!/usr/bin/python3
# Grant Skidmore
# Updated 4/25/20


import os.path


def word(e):
    words = dict()
    e = open(e, encoding = 'utf8')             #e is the whole file with all the text, the encoding build-in used to properly open files according to Jennifer Sawyer
    e = e.read()                                #now we want to read in the file chars, convert them to lowercase, and strip the whitespaces while separating into words
    e = e.lower()
    e = e.strip().split()

    for w in e:             #goes through each word in the fresh list of alphabetical characters
            if w in words:   #checks to see if the word is already in the dictionary for the file
                words[w] += 1    #if the word is already in the dictionary, it adds one to the frequency
            elif w not in words:    #the elif statement in case the word is not in the dictionary
                words[w] = 1     #if the word is not in the dictionary, it'll add the word to the dictionary for the file

    # Counting of items
    total1 = sum(words.values())    #gets the total number of words
    wordCount = sorted(words.values())      #sorts the list of words by the highest frequency
    pcents = []          #initialization
    for word in wordCount:
        percentage = float(word / total1)      #gets the percentage by taking the individual value over the total values of that type
        percentage = '%.3f' % percentage       #limits the percentage to 3 decimal places
        pcents.append(percentage)        #appends the percentage to the list w so it can be paired with the corresponding value and item
    pcents = reversed(pcents)
    wordCount = reversed(wordCount)
    sortedWords = reversed(sorted(words, key = words.get))        #this gets the keys in the order of the reverse, sorted by value list
    o = zip(sortedWords, wordCount, pcents)     #creates a single 'object' of the word, word count, and percentage
    out = tuple(list(o))
    print('Words (total words: {0})'.format(total1))     #[0:25] was used so that it would only show the top 25 results
    print('{0}'.format(out[5:9]))
    print('{0}'.format(out[10:14]))
    print('{0}'.format(out[15:19]))
    print('{0}'.format(out[20:24]))
    print('\n')
    return out


def letter(e):
    letters = dict()
    e = open(e, encoding = 'utf8')             #e is the whole file with all the text, the encoding build-in used to properly open files according to Jennifer Sawyer
    e = e.read()                               #this is a similar variation of the code used from my assignment 5
    e = e.lower()
    e = e.strip().split()
    chars = [] #z
    for words in e:             #goes through each word in the fresh list of alphabetical characters
        for letter in words:
            chars.append(letter)
            if letter in letters:   #checks to see if the letter is already in the file's dictionary
                letters[letter] += 1    #if the word is already in the dictionary, it adds one to the frequency
            elif letter not in letters:    #if the letter is not in the dictionary
                letters[letter] = 1     #adds the word to the file's dictionary
    letterCount = sum(letters.values()) #total2
    sortedLetters = sorted(letters.values())      #x     #sorts the list of words by the highest frequency
    w = []
    for letter in sortedLetters:
        percentage = float(letter / letterCount)      #gets the percentage by taking the individual value over the total values of that type
        percentage = '%.3f' % percentage        #limits the percentage to 3 decimal places
        w.append(percentage)        #appends the percentage to the list w so it can be paired with the corresponding value and item
    w = reversed(w)
    x = reversed(x)
    y = reversed(sorted(letters, key = letters.get))        #this gets the keys in the order of the reverse, sorted by value list
    u = zip(y, x, w)
    q = tuple(list(u))
    print('Letters: {0}'.format(q))     #no need to use [0:25] since there are only 26 letters
    return q


def bigram(e):
    bigrams = dict()
    e = open(e, encoding = 'utf8')             #e is the entire text file, opened, the encoding build-in used to properly open files according to Jennifer Sawyer
    e = e.read()                                #this is a similar variation of the code used from my assignment 5
    e = e.lower()
    e = e.strip().split()
    flist = []                  #flist is a new list of only alphabetical charecters
    z = []
    for a in e:
        if a.isalpha():
            flist.append(a)
    for c in flist:             #goes through each word in the fresh list of alphabetical characters
        for d in range(len(c) - 1):     #need it for the range of one less than the length of the word so the index doesn't go out of the limit
            r = c[d] + c[d + 1] ##this takes the slice starting at d in the word, then one index away and adds the two strings
            # print(r)
            if r in bigrams:   #checks to see if the word is already in the dictionary for the file
                bigrams[r] += 1    #if the word is already in the dictionary, it adds one to the frequency
            elif r not in bigrams:    #the elif statement in case the word is not in the dictionary
                bigrams[r] = 1     #if the word is not in the dictionary, it'll add the word to the dictionary for the file
    total3 = sum(bigrams.values())
    x = sorted(bigrams.values())        #sorts the list of words by the highest frequency
    w = []
    for m in x:
        percentage = float(m / total3)      #gets the percentage by taking the individual value over the total values of that type
        percentage = '%.3f' % percentage        #got the %.3f from stack overflow by searching 'python limit decimal places'
        w.append(percentage)        #appends the percentage to the list w so it can be paired with the corresponding value and item
    w = reversed(w)
    x = reversed(x)
    y = reversed(sorted(bigrams, key = bigrams.get))        #this gets the keys in the order of the reverse, sorted by value list
    u = zip(y, x, w)
    v = tuple(list(u))
    print('Bigrams: {0}'.format(v[0:25]))       #[0:25] was used so that it would only show the top 25 results
    return v


def trigram(e):
    trigrams = dict ()
    e = open(e, encoding = 'utf8')             #e is the entire text file, the encoding build-in used to properly open files according to Jennifer Sawyer
    e = e.read()                                #this is a similar variation of the code used from my assignment 5
    e = e.lower()
    e = e.strip().split()
    flist = []                  #flist is the list of non-numerical charecters or symbols
    z = []
    for a in e:
        if a.isalpha():
            flist.append(a)
    for c in flist:             #goes through each word in the fresh list of alphabetical characters
        for d in range(len(c) - 2):     #need it for the range of two less than the length of the word so the index doesn't go out of the limit
            r = c[d] + c[d + 1] + c[d + 2]  #this takes the slice starting at d in the word, then one index away, and 2 indexes away and adds the strings together
            # print(r)
            if r in trigrams:   #checks to see if the word is already in the dictionary for the file
                trigrams[r] += 1    #if the word is already in the dictionary, it adds one to the frequency
            elif r not in trigrams:    #the elif statement in case the word is not in the dictionary
                trigrams[r] = 1     #if the word is not in the dictionary, it'll add the word to the dictionary for the file
    total4 = sum(trigrams.values())
    x = sorted(trigrams.values())       #sorts the list of words by the highest frequency
    w = []
    for m in x:
        percentage = float(m / total4)      #gets the percentage by taking the individual value over the total values of that type
        percentage = '%.3f' % percentage        #got the %.3f from stack overflow by searching 'python limit decimal places'
        w.append(percentage)            #appends the percentage to the list w so it can be paired with the corresponding value and item
    w = reversed(w)
    x = reversed(x)
    y = reversed(sorted(trigrams, key = trigrams.get))      #this gets the keys in the order of the reverse, sorted by value list
    u = zip(y, x, w)
    w = tuple(list(u))
    print('Trigrams: {0}'.format(w[0:25]))      #[0:25] was used so that it would only show the top 25 results
    return w


nfiles = [ ]    #initialization of the list of files
while True:
    nfile = input('Input a file path for a .txt file you want to analyze: ')
    if len(nfile) > 0:     #need the if statement so that only when the user wants to try to append a file will the program check if the file exists
        if os.path.exists(nfile):
            nfiles.append(nfile)    #appends nfiles with the char contents of nfile
        else:
            print('Invalid File Input') #gives the user an error message if the file does not exists
    else:   #this is to tell the program that the user doesn't want to add more programs to the list
        break

for i in nfiles:            #iteration so that the program prints results for each file in the input
    print('-----Results for file:', i,'-----\n')         #just for clarity when printing :)
    word(i)             #these will call the correct functions once for each file, printing 4 lists each
    letter(i)
    bigram(i)
    trigram(i)

