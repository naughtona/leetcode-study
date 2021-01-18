class Solution:
    def countSubstrings(self, s: str) -> int:
        i, n = 0, len(s)
        count = 0
        while i < n:
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1; l -= 1; r += 1
            
            l = i; r = i+1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1; l -= 1; r += 1
            i += 1        
        return count

# >>> from palindromic_substrings import Solution
# >>> Solution().countSubstrings("abc")
# 3
# >>> Solution().countSubstrings("aaa")
# 6