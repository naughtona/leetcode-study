class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        seen = {}
        maxx = 0
        l = 0
        for r,letter in enumerate(s):
            if letter not in seen or seen[letter] < l:
                seen[letter] = r
                maxx = max(maxx, 1 + r-l)
            else:
                # find index of where we failed and start from next letter
                l = seen[letter] + 1
                seen[letter] = r
        return maxx

# >>> from longest_substring_without_repeating_characters import Solution
# >>> Solution().lengthOfLongestSubstring("abcabcbb")
# 3
# >>> Solution().lengthOfLongestSubstring("bbbbb")
# 1
# >>> Solution().lengthOfLongestSubstring("pwwkew")
# 3
# >>> Solution().lengthOfLongestSubstring("")
# 0