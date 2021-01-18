from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        if len(nums)==1:
            return nums[0]
        if nums[right] > nums[left]:
            return nums[left]
        
        while left <= right:
            mid = left + (right - left)//2
            # check if we are at inflection point
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            # see where to search next
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1

# >>> from find_minimum_in_rotated_sorted_array import Solution
# >>> Solution().findMin([4,5,6,7,0,1,2])
# 0
# >>> Solution().findMin([3,4,5,1,2])
# 1
# >>> Solution().findMin([11,13,15,17])
# 11