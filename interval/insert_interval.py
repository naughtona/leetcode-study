from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # more passes but pythonic
        if not intervals:
            return [newInterval]
        
        s, e = newInterval
        left = [[si,ei] for si,ei in intervals if ei < s] # ends before we start
        right = [[si,ei] for si,ei in intervals if si > e] # starts after we end
        
        # merging intervals?
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[-len(right)-1][1])
        
        return left + [[s,e]] + right
        
#         # one pass but not elegant
#         out = []
#         a0, b0 = newInterval
#         first, second = None, None
#         for interval in intervals:
#             if first is not None and second is not None:
#                 out.append(interval)
#             else:
#                 if first is None:
#                     if a0 < interval[0]:
#                         first = a0
#                     elif interval[0] <= a0 <= interval[1]:
#                         first = interval[0]
#                     else:
#                         out.append(interval)
#                 if first is not None and second is None:
#                     if b0 < interval[0]:
#                         second = b0
#                         out.append([first,second])
#                         out.append(interval)
#                     elif b0 <= interval[1]:
#                         second = interval[1]
#                         out.append([first,second])
        
#         if first is not None and second is None:
#             second = b0
#             out.append([first,second])
#         elif first is None:
#             first, second = a0, b0
#             out.append([first,second])
            
#         return out
