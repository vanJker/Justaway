class Solution:
    '''
    1. Create a string retains only alphanumerics. $O(n)$ and $O(1)$
    2. Two pointers. $O(n)$ and $O(1)$
    '''
    def isPalindrome(self, s: str) -> bool:
        astr = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                astr += c.lower()
        return astr == astr[::-1]
    
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            while left < right and not (s[right].isalpha() or s[right].isdigit()):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True