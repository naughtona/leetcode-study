from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        need, missing = Counter(t), len(t)
        for c in s:
            if not need[c]:
                return False
            missing -= 1
            need[c] -= 1
            
        return False if missing else True

# >>> from valid_anagram import Solution
# >>> Solution().isAnagram("anagram","nagaram")
# True
# >>> Solution().isAnagram("rat","car")
# False