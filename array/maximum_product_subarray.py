from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # the max product so far
        res = nums[0]
        # the min/max product of subarray that ends with
        # the current number n
        imax = res
        imin = res

        for n in nums[1:]:
            # negatives make big number smaller & small number bigger
            if n < 0:
                tmp = imax
                imax = imin
                imin = tmp
            
            imax = max(n, imax * n)
            imin = min(n, imin * n)

            # imax is candidate for global result
            res = max(res, imax)
        
        return res

# >>> from maximum_product_subarray import Solution
# >>> Solution().maxProduct([2,3,-2,4])
# 6
# >>> Solution().maxProduct([-2,0,-1])
# 0
# >>> Solution().maxProduct([-2,3,4,-9,8])
# 1728
# >>> Solution().maxProduct([-3,-1,-1])
# 3
# >>> Solution().maxProduct([-1,-1,-3])
# 3