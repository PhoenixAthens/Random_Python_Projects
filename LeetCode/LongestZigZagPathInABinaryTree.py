class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    # Runtime: 537ms beats 13.38%, Memory: 61.4MB beats 47.30%
    def longestZigZag(self, root: TreeNode) -> int:
        maximum:[int]=[0]
        self.dfs(root,True,0,maximum)
        self.dfs(root,False,0,maximum)
        return maximum[0]

    def dfs(self, root:TreeNode,goLeft:bool,count:int,maximum:[int]):
        if root is None:
            return
        maximum[0] = max(maximum[0],count)
        if goLeft:
            self.dfs(root.left,False,count+1,maximum)
            self.dfs(root.right,True,1,maximum)
        else:
            self.dfs(root.right,True,count+1,maximum)
            self.dfs(root.left, False,1, maximum)