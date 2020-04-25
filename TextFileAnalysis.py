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

    #Putting words into the dict
    for w in e:             #goes through each word in the fresh list of alphabetical characters
            if w in words:   #checks to see if the word is already in the dictionary for the file
                words[w] += 1    #if the word is already in the dictionary, it adds one to the frequency
            elif w not in words:    #the elif statement in case the word is not in the dictionary
                words[w] = 1     #if the word is not in the dictionary, it'll add the word to the dictionary for the file

    # Counting Items
    total1 = sum(words.values())    #gets the total number of words
    wordCount = sorted(words.values())      #sorts the list of words by the highest frequency
    pcents = []          #initialization
    for word in wordCount:
        percentage = float(word / total1)      #gets the percentage by taking the individual value over the total values of that type
        percentage = '%.3f' % percentage       #limits the percentage to 3 decimal places
        pcents.append(percentage)        #appends the percentage to the list
    pcents = reversed(pcents)
    wordCount = reversed(wordCount)
    sortedWords = reversed(sorted(words, key = words.get))        #gets the keys in the order of the reverse, sorted by value list
    o = zip(sortedWords, wordCount, pcents)     #creates a single 'object' of the word, word count, and percentage
    out = tuple(list(o))

    #Printing items
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

    #Putting Letters into the dict
    for words in e:             #goes through each word in the fresh list of alphabetical characters
        for letter in words:
            if letter in letters:   #checks to see if the letter is already in the file's dictionary
                letters[letter] += 1    #if the word is already in the dictionary, it adds one to the frequency
            elif letter not in letters:    #if the letter is not in the dictionary
                letters[letter] = 1     #adds the word to the file's dictionary
    
    #Counting Items
    letterCount = sum(letters.values()) #total2
    sortedLetterCount = sorted(letters.values())          #sorts the list of words by the highest frequency
    pcents = []
    for letter in sortedLetterCount:
        percentage = float(letter / letterCount)      #gets the percentage by taking the individual value over the total values of that type
        percentage = '%.3f' % percentage        #limits the percentage to 3 decimal places
        pcents.append(percentage)        #appends the percentage to the list
    pcents = reversed(pcents)
    sortedLetterCount = reversed(sortedLetterCount)
    sortedLetters = reversed(sorted(letters, key = letters.get))        #gets the keys in the order of the reverse, sorted by value list
    o = zip(sortedLetters, sortedLetterCount, pcents)       #creates a single 'object' of the word, word count, and percentage
    out = tuple(list(o))
    
    #Printing Items
    print('Letters (total letters: {0})'.format(letterCount))     #no need to use [0:25] since there are only 26 letters
    print('{0}'.format(out[5:9]))
    print('{0}'.format(out[10:14]))
    print('{0}'.format(out[15:19]))
    print('{0}'.format(out[20:24]))
    print('\n')
    return out


def bigram(e):
    bigrams = dict()
    e = open(e, encoding = 'utf8')             #e is the entire text file, opened, the encoding build-in used to properly open files according to Jennifer Sawyer
    e = e.read()                                #this is a similar variation of the code used from my assignment 5
    e = e.lower()
    e = e.strip().split()

    #Putting bigrams into the dict
    for word in e:             #goes through each word in the fresh list of alphabetical characters
        for letter in range(len(word) - 1):     #need it for the range of one less than the length of the word so the index doesn't go out of the limit
            bigr = word[letter] + word[letter + 1] ##this takes the slice starting at d in the word, then one index away and adds the two strings
            # print(r)
            if bigr in bigrams:   #checks to see if the word is already in the dictionary for the file
                bigrams[bigr] += 1    #if the word is already in the dictionary, it adds one to the frequency
            elif bigr not in bigrams:    #the elif statement in case the word is not in the dictionary
                bigrams[bigr] = 1     #if the word is not in the dictionary, it'll add the word to the dictionary for the file
    
    #Counting Itmes
    bigramCount = sum(bigrams.values())
    sortedBigramCount = sorted(bigrams.values())        #sorts the list of words by the highest frequency
    pcents = [] 
    for bigr in sortedBigramCount: 
        percentage = float(bigr / bigramCount)      #gets the percentage by taking the individual value over the total values of that type
        percentage = '%.3f' % percentage        #limits the percentage to 3 decimal places
        pcents.append(percentage)        #appends the percentage to the list
    pcents = reversed(pcents) 
    sortedBigramCount = reversed(sortedBigramCount)
    sortedBigrams = reversed(sorted(bigrams, key = bigrams.get))        #this gets the keys in the order of the reverse, sorted by value list
    o = zip(sortedBigrams, sortedBigramCount, pcents)       #creates a single 'object' of the word, word count, and percentage
    out = tuple(list(o))
    
    #Printing Items
    print('Bigrams (total bigrams: {0})'.format(bigramCount))       #[0:25] was used so that it would only show the top 25 results
    print('{0}'.format(out[5:9]))
    print('{0}'.format(out[10:14]))
    print('{0}'.format(out[15:19]))
    print('{0}'.format(out[20:24]))
    print('\n')
    return out


def trigram(e):
    trigrams = dict ()
    e = open(e, encoding = 'utf8')             #e is the entire text file, the encoding build-in used to properly open files according to Jennifer Sawyer
    e = e.read()                                #this is a similar variation of the code used from my assignment 5
    e = e.lower()
    e = e.strip().split()

    #Putting trigrams into dict
    for word in e:             #goes through each word in the fresh list of alphabetical characters
        for letter in range(len(word) - 2):     #need it for the range of two less than the length of the word so the index doesn't go out of the limit
            trig = word[letter] + word[letter + 1] + word[letter + 2]  #this takes the slice starting at d in the word, then one index away, and 2 indexes away and adds the strings together
            # print(r)
            if trig in trigrams:   #checks to see if the word is already in the dictionary for the file
                trigrams[trig] += 1    #if the word is already in the dictionary, it adds one to the frequency
            elif trig not in trigrams:    #the elif statement in case the word is not in the dictionary
                trigrams[trig] = 1     #if the word is not in the dictionary, it'll add the word to the dictionary for the file
    
    #Counting Items
    trigramCount = sum(trigrams.values())
    sortedTrigramCount = sorted(trigrams.values())       #sorts the list of words by the highest frequency
    pcents = []
    for trig in sortedTrigramCount:
        percentage = float(trig / trigramCount)      #gets the percentage by taking the individual value over the total values of that type
        percentage = '%.3f' % percentage        #limits the percentage to 3 decimal places
        pcents.append(percentage)             #appends the percentage to the list
    pcents = reversed(pcents)
    sortedTrigramCount = reversed(sortedTrigramCount)
    sortedTrigrams = reversed(sorted(trigrams, key = trigrams.get))      #gets the keys in the order of the reverse, sorted by value list
    o = zip(sortedTrigrams, sortedTrigramCount, pcents)     #creates a single 'object' of the word, word count, and percentage
    out = tuple(list(o))
    
    #Printing Items
    print('Trigrams: {0}'.format(trigramCount))      #[0:25] was used so that it would only show the top 25 results
    print('{0}'.format(out[5:9]))
    print('{0}'.format(out[10:14]))
    print('{0}'.format(out[15:19]))
    print('{0}'.format(out[20:24]))
    return out


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

for file in nfiles:            #iteration so that the program prints results for each file in the input
    print('-----Results for file:', file,'-----\n')         #just for clarity when printing :)
    word(file)             #these will call the correct functions once for each file, printing 4 lists each
    letter(file)
    bigram(file)
    trigram(file)
    print('\n\n')

