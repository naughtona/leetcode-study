from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = {}
        # for cand in strs:
        #     key = tuple(sorted(cand))
        #     anagrams[key] = anagrams.get(key, []) + [cand]
        # return anagrams.values()
        
        anagrams = {}
        for cand in strs:
            key = self.hash(cand)
            anagrams[key] = anagrams.get(key, []) + [cand]
        return anagrams.values()
    
    def hash(self, word: str) -> tuple:
        out = [0]*26
        for char in word:
            out[ord(char)-ord('a')] += 1
        return tuple(out)

# >>> from group_anagrams import Solution
# >>> Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# >>> Solution().groupAnagrams([""])
# [['']]
# >>> Solution().groupAnagrams(["a"])
# [['a']]
