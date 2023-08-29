import ex25_EvenMorePractice as pr
sentence = "All good things come to those who wait."
print(pr.break_words(sentence))
print(pr.print_first_word(sentence))
print(pr.print_last_word(sentence))
print(pr.sortWords_characterWise(sentence))
print(pr.sort_sentence_wordWise(sentence))
print(pr.print_first_and_last_word(sentence))
print(pr.print_first_and_last_of_sortedSentence(sentence))
"""OUTPUT
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
All
wait.
[' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', 'A', 'a', 'c', 'd', 'e', 'e', 'g', 'g', 'h', 'h', 'h', 'i', 'i', 'l', 'l', 'm',
 'n', 'o', 'o', 'o', 'o', 'o', 'o', 's', 's', 't', 't', 't', 't', 'w', 'w']
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
first word: All, last word: wait.
first word: All, last word: who
"""