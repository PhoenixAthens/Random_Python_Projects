class Solution:
    #using for-loop
    #Runtime: 31ms beats 72.43%, Memory: 14MB beats 9.46%
    #using while-loop
    # Runtime: 32ms beats 63.90%, Memory: 13.9MB beats 55.13%
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        stringMain = []
        i = 0
        if len1>len2:
           while i  < len2 :
               stringMain.append(word1[i])
               stringMain.append(word2[i])
               i+=1

           while i <len1:
               stringMain.append(word1[i])
               i+=1
        elif len2>len1:
            while i <len1:
                stringMain.append(word1[i])
                stringMain.append(word2[i])
                i+=1

            while i < len2:
                stringMain.append(word2[i])
                i+=1
        else:
            while i < len1:
                stringMain.append(word1[i])
                stringMain.append(word2[i])
                i+=1

        return "".join(stringMain)

