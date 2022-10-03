class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        time=0
        for i in range(0,len(colors)-1):
            if colors[i]==colors[i+1]:
                if(neededTime[i]<neededTime[i+1]):
                    time+=neededTime[i]
                elif(neededTime[i+1]<neededTime[i]):
                    time+=neededTime[i+1]
                    temp=neededTime[i]
                    neededTime[i]=neededTime[i+1]
                    neededTime[i+1]=temp
                else:
                    time+=neededTime[i]
        return time
work=Solution()
print(work.minCost("abaac",[1,2,3,4,5]))