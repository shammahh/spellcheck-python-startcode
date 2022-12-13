def contains(str, item):
    for element in str:
        if element == item:
            return True
    
    return False

def binery(arr, item):
    low = 0
    hi = len(arr) - 1
    while low <= hi:
        miInd = (low + hi) // 2
        if arr[miInd] == item:
            return miInd
        elif item > arr[miInd]:
            low = miInd + 1
        else:
            hi = miInd - 1
            
    return -1

def linear(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        
    return -1

# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re
import time  # Needed for splitting text with a regular expression
def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()
dictionary = loadWordsFromFile("data-files/dictionary.txt")
aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
# end main()



## chage to while loop
loop = True
while loop:
    # Call main() to begin program
    main()
    
    print("1: Spell Check a Word (Linear Search)")
    print("2: Spell Check a Word (Binary Search)")
    print("3: Spell Check Alice In Wonderland (Linear Search)")
    print("4: Spell Check Alice In Wonderland (Binary Search)")
    print("5: Exit")

    runfun = int(input("what would you like to do"))

    if runfun == 1:
        #print("1")
        #Ask user for a word
        ques = str(input("Which word would you like to find: "))

        # Perform the Search (time it)
        startTime = time.time()
        index = linear(dictionary, ques)
        endTime = time.time()

        # Output the results
        if index == -1:
            print(ques + " was not found")
        else:
            print(ques, index)
        print(f"search time: {endTime - startTime} seconds")
    if runfun == 2:
        #print("2")
        ques = str(input("Which word would you like to find: "))
        startTime = time.time()
        index = binery(dictionary, ques)
        endTime = time.time()

        if index == -1:
            print(ques + " was not found")
        else:
            print(ques, index)
        print(f"search time: {endTime - startTime} seconds")
    if runfun == 3:
        #print("3")
        notfoundcount = 0
        startTime = time.time()
     ## COUNT THE NUMBER OF WODS NOT IN DICTIONARY AND OUTPUT
        for i in range(len(aliceWords)):
            search = linear(dictionary, aliceWords[i].lower())
            if search == -1:
                notfoundcount += 1
        endTime = time.time()
        print(notfoundcount)
        print(f"search time: {endTime - startTime} seconds")
    if runfun == 4:
        ###print("4")
        notfoundcount = 0
        startTime = time.time()
     ### COUNT THE NUMBER OF WODS NOT IN DICTIONARY AND OUTPUT
        for i in range(len(aliceWords)):
            search = binery(dictionary, aliceWords[i].lower())
            if search == -1:
                notfoundcount += 1
        endTime = time.time()
        print(notfoundcount)
        print(f"search time: {endTime - startTime} seconds")
    if runfun == 5:
        print("5")
        
