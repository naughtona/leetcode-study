from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## sorting => O(n log n) time, O(1) space
        nums_ = sorted(nums)
        return any((x==nums_[i] for i,x in enumerate(nums_[1:])))

        # ## hashing => O(n) time, O(n) space
        # h = set()
        # for n in nums:
        #     if n in h: return True
        #     else: h.add(n)
        # return False

# >>> from contains_duplicate import Solution
# >>> Solution().containsDuplicate([1,2,3,4])
# False
# >>> Solution().containsDuplicate([1,2,3,1])
# True
