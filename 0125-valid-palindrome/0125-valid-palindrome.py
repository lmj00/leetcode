class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        
        for i in s.lower():
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                ss += i

        
        i = 0
        for j in range(len(ss) - 1, len(ss) // 2 - 1, -1):
            if ss[i] != ss[j]:
                return False
            i += 1
            
        return True