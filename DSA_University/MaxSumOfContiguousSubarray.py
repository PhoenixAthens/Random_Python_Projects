import math

seq=[-2,-3,-1]

# Brute Force Algorithm O(n^3)
# This solution also exceeds Time limit 186/227
def maxSubArray(nums:list[int])->int:
    if len(nums) == 1:
        return nums[0]
    n = len(nums)
    maxSum = 0
    for i in range(0,n):
        for j in range(i,n):
            subSeqSum = 0
            for k in range(i,j+1):
                subSeqSum+=nums[k]
                maxSum=max(maxSum,subSeqSum)
    return maxSum

print(maxSubArray(seq))

# Dynamic Programming O(n^2) algorithm
# this solution works but exceeds the time limit! 221/227
def maxSubArray( nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    n = len(nums)
    maxSum = nums[0]
    for i in range(0, n):
        subSeq = nums[i]
        maxSum = max(maxSum, subSeq)
        for j in range(i + 1, n):
            subSeq += nums[j]
            maxSum = max(maxSum, subSeq)

    return maxSum

print(maxSubArray(seq))

# Divide and Conquer O(n)// Runtime: 2634ms
def maxSubArray(nums:list[int],low:int,high:int)->int:
    if low == high:
        return nums[low]
    mid = (low+high)//2
    maxLeftSum=-123456
    SubSum=0
    for i in range(mid,low-1,-1):
        SubSum+=nums[i]
        maxLeftSum=max(maxLeftSum,SubSum)

    maxRightSum=-123456
    SubSum=0
    for i in range(mid+1,high+1):
        SubSum+=nums[i]
        maxRightSum=max(maxRightSum,SubSum)

    left = maxSubArray(nums, low, mid)
    right = maxSubArray(nums,mid+1,high)
    return max(left,maxRightSum+maxLeftSum,right)

print(maxSubArray(seq,0,len(seq)-1))