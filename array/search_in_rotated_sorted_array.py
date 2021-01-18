from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        if n==1:
            if nums[left]==target:
                return 0
            else:
                return -1
        if nums[right] > nums[left]:
            rotation = 0
        else:
            while left <= right:
                mid = (left+right)//2
                
                if nums[mid] > nums[mid+1]:
                    rotation = mid + 1
                    break
                if nums[mid-1] > nums[mid]:
                    rotation = mid
                    break
                
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        left = 0
        right = n - 1

        while left <= right:
            mid = (left+right)//2
            adj_mid = (mid+rotation)%n
            if nums[adj_mid]==target:
                return adj_mid
            if nums[adj_mid] > target:
                right = mid - 1
            elif nums[adj_mid] < target:
                left = mid + 1

        return -1