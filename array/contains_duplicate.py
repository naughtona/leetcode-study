from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_ = sorted(nums)
        return any((True if x==nums_[i] else False for i,x in enumerate(nums_[1:])))

# >>> from contains_duplicate import Solution
# >>> Solution().containsDuplicate([1,2,3,4])
# False
# >>> Solution().containsDuplicate([1,2,3,1])
# True
