from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mul = lambda curr_acc, x: curr_acc * x
        left = self.scan(mul, 1, nums, dir='l')
        right = self.scan(mul, 1, nums, dir='r')
        return [l*r for (l,r) in zip(left,right)]
    
    def scan(self,f, start, lst, dir="l"):
        acc = start
        it = [start] + lst[:-1] if dir=="l" else [start] + lst[::-1][:-1]
        res = []
        for e in it:
            acc = f(acc,e)
            res.append(acc)
        return res if dir=="l" else res[::-1]

# >>> from product_of_array_except_self import Solution
# >>> Solution().productExceptSelf([1,2,3,4])
# [24, 12, 8, 6]
