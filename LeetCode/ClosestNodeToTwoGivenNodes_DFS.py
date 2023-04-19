class Solution:
    # Runtime: 1263ms beats 65.86%, Memory: 3.6MB beats 17.24%
    def DFS(self, dist,visit,node,edges):
        if not visit[node]:
            visit[node]=True
            neighbor = edges[node]
            if neighbor!=-1 and not visit[neighbor]:
                dist[neighbor] = 1 + dist[node]
                self.DFS(dist,visit,neighbor,edges)



    def closestMeetingNode(self, edges: [int], node1: int, node2: int) -> int:
        n:int = len(edges)
        visit1 = [False]*n
        visit2 = [False]*n
        dist1 = [-27]*n
        dist2 = [-27]*n
        dist1[node1] = 0
        dist2[node2] = 0
        self.DFS(dist1,visit1,node1,edges)
        self.DFS(dist2,visit2,node2,edges)
        currResult = -1
        maxDistTillNow = 2_000_000_000
        for i in range(0,n):
            if dist1[i]==-27 or dist2[i]==-27:
                continue
            tempMax = max(dist1[i],dist2[i])
            if tempMax<maxDistTillNow:
                maxDistTillNow=tempMax
                currResult=i
        return currResult