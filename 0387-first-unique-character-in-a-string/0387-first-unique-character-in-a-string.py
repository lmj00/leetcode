class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic = {}
            
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            
        
        for k, v in dic.items():    
            if v == 1:
                return s.index(k)
            
        return -1   