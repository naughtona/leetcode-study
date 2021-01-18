class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = list(filter(lambda x: x.isalnum(), s))
        
        l, r = 0, len(filtered_s)-1
        
        while l < r:
            a = filtered_s[l].lower()
            b = filtered_s[r].lower()
            if a != b:
                return False
            l += 1; r -= 1
        return True

# >>> from valid_palindrome import Solution
# >>> Solution().isPalindrome("A man, a plan, a canal: Panama")
# True
# >>> Solution().isPalindrome("race a car")
# False