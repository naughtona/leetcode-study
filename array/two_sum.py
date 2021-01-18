from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_ = sorted(nums)
        
        l, r = 0, n-1
        while l < r:
            a = nums_[l]
            b = nums_[r]
            s = a + b
            
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                i1 = nums.index(a)
                i2 = 1 + nums.index(nums.pop(i1)) if a==b else nums.index(b)
                return [i1,i2]

# >>> from two_sum import Solution
# >>> Solution().twoSum([3,2,4],6)
# [1, 2]

        ## hash table solution

        # h = {}
        # for i, num in enumerate(nums):
        #     n = target - num
        #     if n not in h:
        #         h[num] = i
        #     else:
        #         return [h[n],i]