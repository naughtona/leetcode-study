class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if not s or n % 2 != 0:
            return False

        filtered_s = filter(lambda x: x in '({[]})',s)
        d = {'(':')','{':'}', '[':']'}
        stack = []

        for p in filtered_s:
            if p in d:
                stack.append(d[p])
            elif not stack or p != stack.pop():
                return False

        return not stack
        
# >>> from valid_parentheses import Solution
# >>> Solution().isValid("()")
# True
# >>> Solution().isValid("()[]{}")
# True
# >>> Solution().isValid("(]")
# False
# >>> Solution().isValid("([)]")
# False
# >>> Solution().isValid("{[]}")
# True                