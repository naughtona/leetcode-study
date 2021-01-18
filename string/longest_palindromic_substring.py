class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = R = 0
        i, n = 0, len(s)
        mid = n // 2
        while i < n:
            if i > mid+1 and 2*(n-i) < R-L:
                break
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if not R or r-l+1 > R-L:
                    L, R = l, r+1
                l -= 1; r += 1
            
            l = i; r = i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if not R or r-l+1 > R-L:
                    L, R = l, r+1
                l -= 1; r += 1
            i += 1        
        return s[L:R]

# >>> from longest_palindromic_substring import Solution
# >>> Solution().longestPalindrome("babad")
# 'bab'
# >>> Solution().longestPalindrome("cbbd")
# 'bb'
# >>> Solution().longestPalindrome("a")
# 'a'
# >>> Solution().longestPalindrome("ac")
# 'a'