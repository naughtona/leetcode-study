from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0: 
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # need two new numbers
                    while l < r and nums[l]==nums[l+1]:
                        l += 1
                    while l < r and nums[r]==nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

# >>> from three_sum import Solution
# >>> Solution().threeSum([-1,0,1,2,-1,-4])
# [[-1, -1, 2], [-1, 0, 1]]