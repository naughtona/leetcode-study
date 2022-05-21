class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def go_left(num):
            if num - 1 in numset:
                numset.remove(num-1)
                return 1 + go_left(num-1)
            else:
                return 0
        
        def go_right(num):
            if num + 1 in numset:
                numset.remove(num+1)
                return 1 + go_right(num+1)
            else:
                return 0
            
        numset = set(nums)
        max_consec = 0
        while numset:
            num = numset.pop()
            seqlen = 1 + go_left(num) + go_right(num)
            if seqlen > max_consec:
                max_consec = seqlen
        return max_consec
