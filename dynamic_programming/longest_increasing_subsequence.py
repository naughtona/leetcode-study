class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        h = [1] * n # subproblems dp table
        
        for i in range(1,n):
            for j in range(i):
                # can I latch onto this subsequence?
                # can I improve my current best length?
                if nums[i] > nums[j] and h[j]+1 > h[i]:
                    h[i] = h[j]+1
        return max(h)
