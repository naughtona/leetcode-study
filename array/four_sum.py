from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                l, r = j+1, n-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l]==nums[l+1]:
                            l += 1
                        while l < r and nums[r]==nums[r-1]:
                            r -= 1
                        l += 1; r -= 1
        return res

# >>> from four_sum import Solution
# >>> Solution().fourSum([1,0,-1,0,-2,2],0)
# [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
# >>> Solution().fourSum([],0)
# []