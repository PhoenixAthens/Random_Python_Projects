class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
        tempo = list(sentence);
        counter = 0
        for i in arr:
            if tempo.__contains__(i):
                counter += 1
        if counter == 26:
            return True
        else:
            return False
