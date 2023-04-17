# runtime: 31ms beats 96.42%, Memory: 13.8 MB beats 50.96%
class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        array: [bool] = []
        maxVal: int = 0
        for i in candies:
            maxVal=max(maxVal,i)
        for i in candies:
            if extraCandies+i>=maxVal:
                array.append(True)
            else:
                array.append(False)

        return array

testCase = Solution()
print(testCase.kidsWithCandies([2,3,5,1,3],3))
