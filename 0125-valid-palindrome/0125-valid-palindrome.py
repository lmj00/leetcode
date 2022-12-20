class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        
        for i in s.lower():
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                ss += i
        
        return ss == ss[::-1]