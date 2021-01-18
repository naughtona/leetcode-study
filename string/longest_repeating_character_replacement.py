class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0]*26
        maxLength, maxOccur = 0, 0
        l = 0
        for r,letter in enumerate(s):
            counts[ord(letter) - ord('A')] += 1
            maxOccur = max(maxOccur, counts[ord(letter) - ord('A')])

            if r - l + 1 - maxOccur > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength

# >>> from longest_repeating_character_replacement import Solution
# >>> Solution().characterReplacement("ABAB",2)
# 4
# >>> Solution().characterReplacement("AABABBA",1)
# 4