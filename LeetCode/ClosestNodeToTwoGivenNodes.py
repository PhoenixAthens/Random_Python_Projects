# runtime: 1082ms beats 85.27%, Memory: 28.7 beats 89.4%
class Solution:
    def closestMeetingNode(self, edges: [int], node1: int, node2: int) -> int:
        n=len(edges)
        dist1=[-27]*n
        dist2=[-27]*n
        self.bfs(dist1,node1,edges)
        self.bfs(dist2,node2,edges)
        closestNode=-1
        maxDistTillNow=2_000_000_000
        for i in range(0,n):
            if dist1[i] == -27 or dist2[i]==-27:
                continue

            tempMax = max(dist1[i],dist2[i])
            if  tempMax < maxDistTillNow:
                closestNode = i
                maxDistTillNow = tempMax
        return closestNode


    def bfs(self, dist:[int],node1:int,edges:[int]):
        length = len(edges)
        boolList:[bool] = [False]*length
        queue = node1
        dist[node1]=0
        while queue is not None:
            if boolList[queue] is True:
                continue
            boolList[queue]=True
            neighbor = edges[queue]
            if neighbor != -1 and boolList[neighbor] is False:
                dist[neighbor]=dist[queue]+1
                queue=neighbor
            else:
                queue=None

test1 = Solution()
print(test1.closestMeetingNode([2,2,3,-1],0,1))
print(test1.closestMeetingNode([1,2,-1],0,2))
