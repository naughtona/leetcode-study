from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums[:2]
        for i, n in enumerate(nums[2:], start=2):
            if i - 3 >= 0:
                dp.append(max(dp[i-3], dp[i-2]) + n)
            else:
                dp.append(dp[i-2] + n)
        
        return max(dp[-2:])

# Example input
# [2,1,1,2]
# Expected output
# 4
