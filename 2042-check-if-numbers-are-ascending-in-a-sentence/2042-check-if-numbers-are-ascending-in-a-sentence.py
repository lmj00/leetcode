import re

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        s = list(map(int, re.findall(r'\d+', s)))
        
        return s == sorted(list(set(s)))   