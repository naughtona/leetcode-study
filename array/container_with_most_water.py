from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0

        l, r = 0, len(height)-1

        while l < r:
            lh = height[l]
            rh = height[r]
            area = (r - l) * min(lh, rh)
            maxx = max(maxx,area)

            if lh <= rh:
                l += 1
            elif lh > rh:
                r -= 1
        return maxx

# >>> from container_with_most_water import Solution
# >>> Solution().maxArea([1,8,6,2,5,4,8,3,7])
# 49