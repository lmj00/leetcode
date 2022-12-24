class Solution:
    def maxPower(self, s: str) -> int:

        v = s[0]
        count = 1
        max_c = 1
        
        for i in range(1, len(s)):
            if v == s[i]:
                count += 1
            else:
                v = s[i]
                count = 1
            
            if max_c < count:
                max_c = count
    
        return max_c