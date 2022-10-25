from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first=second=""
        for i in word1:
            first+=str(i)
        for i in word2:
            second+=str(i)
        return first == second


sol1=Solution()
print(sol1.arrayStringsAreEqual(["ab", "c"],["a", "cb"]))