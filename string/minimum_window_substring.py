from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ''
        
        need = Counter(t)
        filtered_s = [(i,c) for (i,c) in enumerate(s,1) if c in need]
        missing = len(t)
        i = l = L = R = 0

        for j,(r,c) in enumerate(filtered_s,1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and not missing:
                    l, other_c = filtered_s[i]
                    need[other_c] += 1
                    missing += need[other_c] > 0
                    i += 1
                if not R or r-l+1 <= R-L:
                    L, R = l-1, r

        return s[L:R]

# >>> from minimum_window_substring import Solution
# >>> Solution().minWindow("ADOBECODEBANC", "ABC")
# 'BANC'
# >>> Solution().minWindow("a", "a")
# 'a'