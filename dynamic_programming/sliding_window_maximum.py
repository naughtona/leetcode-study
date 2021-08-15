from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a doubly linked list
        # add one at a time, keeping largest-smallest and oldest-newest
        n = len(nums)
        L, out = deque(), []
        for i in range(n):
            # keep oldest-newest and relevant range
            while L and L[0][1] < i-k+1:
                L.popleft()
            # keep largest-smallest
            while L and L[-1][0] < nums[i]:
                L.pop()
            # add (val, idx) to L
            L.append((nums[i], i))
            # add largest to out
            if i >= k-1:
                out.append(L[0][0])
        
        return out
