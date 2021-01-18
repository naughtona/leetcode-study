from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s = -1 - 10**5
        curr_s = 0

        if len(nums)==1:
            return nums[0]

        for n in nums:
            curr_s = max(curr_s + n, n)
            if curr_s > max_s:
                max_s = curr_s
            elif curr_s < 0:
                curr_s = 0
        return max_s
