from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in sorted(strs):
            key = tuple(sorted(s))
            d[key] += [s]
        return d.values()

# >>> from group_anagrams import Solution
# >>> Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# >>> Solution().groupAnagrams([""])
# [['']]
# >>> Solution().groupAnagrams(["a"])
# [['a']]