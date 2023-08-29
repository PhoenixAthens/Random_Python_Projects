# this function takes a string and returns an array
def break_words(sentence:str):
    return sentence.split(" ")

# this also takes a string and returns an array of characters from string in sorted order
def sortWords_characterWise(sentence:str):
    return sorted(sentence) # sorted() can also work with arrays

# this takes an array as input
# or we can take a string as input, turn it into array and then apply pop to it
def print_first_word(sentence:str):
    sentence = break_words(sentence)
    word = sentence.pop(0) # pop is a method that can be applied on arrays and not on strings
    return word

# this also takes an array, i.e,
# we can compensate by taking in a string turning it into an array and then
# applying pop to the array
def print_last_word(sentence:str):
    sentence = break_words(sentence)
    return sentence.pop(-1) # last element in array has index -1

# this takes in a string and returns a sorted array of strings
def sort_sentence_wordWise(sentence:str):
    return sorted(break_words(sentence))

# intakes a string
def print_first_and_last_word(sentence:str):
    brokenUP = break_words(sentence)
    return f"first word: {brokenUP.pop(0)}, last word: {brokenUP.pop(-1)}"

# intakes a string
def print_first_and_last_of_sortedSentence(sentence:str):
    brokenUP = sort_sentence_wordWise(sentence)
    return f"first word: {brokenUP.pop(0)}, last word: {brokenUP.pop(-1)}"

wordy = "All good things come to those who wait."
#print(break_words(wordy))
#print(sortWords_characterWise(wordy))
#print(print_last_word(wordy))
#print(print_first_word(wordy))
#print(sort_sentence_wordWise(wordy))
#print(print_first_and_last_word(wordy))
#print(print_first_and_last_of_sortedSentence(wordy))
"""OUTPUT
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', 'A', 'a', 'c', 'd', 'e', 'e', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'l', 'l', 'm', 
'n', 'o', 'o', 'o', 'o', 'o', 'o', 's', 's', 't', 't', 't', 't', 'w', 'w']
wait.
All
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
first word: All, last word: wait.
first word: All, last word: who
"""