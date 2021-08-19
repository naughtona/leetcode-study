from itertools import product

"""
    Returns an integer that denotes the largest integer k such that there is no
    k x k sub-grid with a total value greater than maxSum. If all square sub-grids
    have value greater than maxSum, the function should return 0.
    
    https://leetcode.com/discuss/interview-question/850974/hackerrank-online-assessment-roblox-new-grad-how-to-solve-this
"""

def largestSubgrid(grid, maxSum):
    n = len(grid)
    
    # create cumulative sum matrix
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i,j in product(range(1, n+1), range(1, n+1)):
        dp[i][j] = grid[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    def maxSumRegion(k):
        total = 0
        for i,j in product(range(n-k+1), range(n-k+1)):
            gross = dp[i+k][j+k] # sumD
            sumB = dp[i][j+k]
            sumC = dp[i+k][j]
            sumA = dp[i][j]
            netSum = gross - sumB - sumC + sumA
            total = max(total, netSum)
        return total
    
    # binary search
    l, r = 0, n
    while l < r:
        mid = l + (r-l)//2
        res = maxSumRegion(mid)
        if res <= maxSum:
            l = mid + 1
        else:
            r = mid - 1

    return r-1 if r > 0 else 0

if __name__ == '__main__':
    n = int(input())
    _ = int(input()) # second dim must be n, since square grid
    grid = [list(map(int, input().split())) for _ in range(n)]
    maxSum = int(input())
    print(largestSubgrid(grid, maxSum))
    

#-----------------SAMPLE INPUT 0------------------#
# 3
# 3
# 1 1 1
# 1 1 1
# 1 1 1
# 4
#-----------------SAMPLE OUTPUT 0-----------------#
# 2
#-----------------SAMPLE INPUT 1------------------#
# 4
# 4
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# 39
#-----------------SAMPLE OUTPUT 1-----------------#
# 3
#-----------------SAMPLE INPUT 2------------------#
# 2
# 2
# 4 5
# 6 7
# 2
#-----------------SAMPLE OUTPUT 1-----------------#
# 0
