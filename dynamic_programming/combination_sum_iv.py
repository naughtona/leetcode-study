class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def rec(left, cache):
            if left < 0: return 0
            elif left == 0: return 1
            
            if left in cache: return cache[left]
            
            count = 0
            for n in nums:
                count += rec(left-n, cache)
            
            cache[left] = count
            return cache[left]
        
        return rec(target, {})
