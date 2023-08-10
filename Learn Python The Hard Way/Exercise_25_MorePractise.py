def breakWords(stuff): # this takes a string
    words = stuff.split(' ')
    return words

def sortWords(words):
    # sort
    # -> the words in order if array is entered
    # -> the characters if sentence is entered
    return sorted(words)

def printLastWord(words): # this takes an array
    return words.pop(-1)

def printFirstWords(words): # this takes an array
    return words.pop(0)

def sort_Sentence(sentence): #
    wordList = breakWords(sentence)
    return sorted(wordList)

def print_firstLast_word(sentence):
    words = breakWords(sentence)
    printFirstWords(words)
    printLastWord(words)

sent = "Hello Phoenix! Who are you?"
sent_2 = sorted(sent.split(" "))
print(sent_2)