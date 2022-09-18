import itertools
alphabet = "abcdefghijklmnopqrstuvwxyz"

def generateWord(n=2):
    '''
    generates all possible words for a given n, where 2n = number of sides of the polygon being glued
    does not consider whether a given word is equivalent to another through rotation

    Takes:
        n (int): n = number of sides of polygon/2

    Returns:


    '''
    wordLength = 2*n
    nAlphabet = alphabet[0:n] # letters to be used for combinations
    workingAlphabet = nAlphabet*2
    permutations = list(itertools.permutations(workingAlphabet))
    #print(permutations)
    permutations = list(dict.fromkeys(permutations)) # removing duplicates
    #print(permutations)
    allOptions = []
    for p in permutations:
        p = ''.join(p)
        #print(p)
        rotationsP = []
        i = 0
        for edge in p:
            #print("Edge:",edge)
            if i == 0:
                rotationsP.append(edge)
                rotationsP.append(edge.upper())
            else:
                clockwiseRotations = []
                anticlockwiseRotations = []
                for rotation in rotationsP:
                    rotation += edge
                    clockwiseRotations.append(rotation)
                for rotation in rotationsP:
                    rotation += edge.upper()
                    anticlockwiseRotations.append(rotation)
                rotationsP = clockwiseRotations
                rotationsP.extend(anticlockwiseRotations)
            i += 1
            #print(rotationsP)
        
        allOptions.extend(rotationsP)
    #print(len(allOptions))
    return allOptions, len(allOptions)
        




print(generateWord())


# NOT CONVINCED THAT THESE ARE WORKING PROPERLY, IGNORE FOR TIME BEING
def removeRotation(wordsList:list): 
    '''
    removes items that are rotations

    takes:
        wordsList (list): list of words as defined for a given n

    returns:
        reducedWords (list): list of words for a given n with rotations removed
    '''
    wordLength = len(wordsList[0])
    reducingList = wordsList
    for word in wordsList:
        prevRotation = word
        for i in range(len(word)):
            lastChar = prevRotation[-1]
            word_rotation = lastChar+prevRotation[0:wordLength-1]
            if word_rotation == word:
                continue
            if word_rotation in reducingList:
                reducingList.remove(word_rotation)
            prevRotation = word_rotation
    reducedWords = reducingList

    return reducedWords    

def removeReflection(wordsList:list):
    '''
    removes items that are reflections, ie, cases and direction reversed

    takes:
        wordsList (list): list of words as defined for a given n

    returns:
        reducedWords (list): list of words for a given n with rotations removed
    '''
    wordLength = len(wordsList[0])
    reducingList = wordsList
    for word in wordsList:
        reflectedWord = word.swapcase()[::-1]
        if reflectedWord in reducingList:
            reducingList.remove(reflectedWord)
    reducedWords = reducingList
    return reducedWords 



def removeDuplicates(wordsList:list):
    '''
    removes items which are duplicates by:
        - cutting and pasting (TO BE IMPLEMENTED)
        - reflection (CREATED)
        - rotation (CREATED)
    
    takes:
        wordsList (list): list of words as defined for a given n

    returns:
        reducedWords (list): list of words for a given n with duplicates removed
    '''
    rotationRemoved = removeRotation(wordsList)
    print(len(rotationRemoved))
    rotationReflectionRemoved = removeReflection(wordsList)
    print(len(rotationReflectionRemoved))

    reducedWords = rotationReflectionRemoved
    print(len(reducedWords))

    return reducedWords

print(removeDuplicates(generateWord()[0]))


