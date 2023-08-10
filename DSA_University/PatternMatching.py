# Naïve Algorithm
def match(pattern:str, string:str):
    if not pattern or not string:
        return 0
    lenPattern = len(pattern)
    lenText = len(string)
    found = False
    for i in range(lenText-lenPattern+1):
        tempCounter = 0
        currentlyAt = i
        while tempCounter < lenPattern and currentlyAt<lenText and pattern[tempCounter]==string[currentlyAt]:
            tempCounter+=1
            currentlyAt+=1
        if tempCounter == lenPattern:
            found = True
            print(f"pattern found at {i}")
    if not found:
        print("Pattern not found!!")

match("aba","cbabababaa")
"""
pattern found at 2
pattern found at 4
pattern found at 6
"""
match("abc","cbabababaa")
# Pattern not found!!

# Knuth-Morris-Pratt algorithm
def prefix(pattern): # this is useful when our pattern has a recursive quality, i.e., it repeats itself within itself
    patLength = len(pattern)
    table = [0]*patLength
    j = 0
    for i in range(1,patLength):
        while j>0 and pattern[j]!=pattern[i]:
            j=table[j-1]
        if pattern[i]==pattern[j]:
            j+=1
        table[i]=j
    return table

print(prefix("abcabb")) #[0, 0, 0, 1, 2, 0]
print(prefix("abb")) #[0, 0, 0]
print(prefix("abcabc")) #[0, 0, 0, 1, 2, 3]
print(prefix("abxabc")) #[0, 0, 0, 1, 2, 0]
def patternMatcher(pattern, text):
    textLen = len(text)
    patLen = len(pattern)
    table = prefix(pattern)
    j = 0
    for i in range(textLen):
        while j>0 and pattern[j] != text[i]:
            j = table[j-1]
        if pattern[j]==text[i]:
            j+=1
        if j == patLen:
            print(f"pattern found at {i-patLen+1}")
            return i-patLen+1
    print("Pattern not found!!")
patternMatcher("abcabb","cbabababaa") # Pattern not found!!
patternMatcher("aba","cbabababaa") # pattern found at 2
patternMatcher("abcabb","cbabcabcab") # Pattern not found!!
patternMatcher("abcabb","cbabcabcabb") # pattern found at 5









