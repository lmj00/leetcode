class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        ss = ''
        
        for i in s:
            ss += str(ord(i) - 96)      
            
        
        for i in range(k):
            result = 0

            for j in ss:
                result += int(j)

            ss = str(result)
        
        return int(ss)