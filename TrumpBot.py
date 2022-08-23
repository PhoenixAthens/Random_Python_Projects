import random
part1 = ['Putin', 'Hillary', 'Obama', 'Fake News', 'Mexico', 'Arnold Schwarzenegger', 'The Democrats']
part2 = ['no talent', 'on the way down', 'really poort numbers', 'nasty one', 'looking like a fool', 'bad hombre']
part3 = ['got destroyed by my ratings', 'rigged the election', 'had a much smaller crowd', 'will pay for the wall']
part4 = ['so sad', 'apologize', 'so true', 'Media won\'t report', 'Big trouble', 'fantastic job', 'stay tuned']
part5 = ['and the wall will pay for itself', ',you know what Canada will pay for the wall', ',i am very rich', ',wheel is older than wall']
mixTape = [part1,part2,part3,part4,part5]
sentence = []
for j in mixTape:
    sentence.append(j[random.randint(0, len(j)-1)])
print("Sentence: ", ' '.join(sentence))