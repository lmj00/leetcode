from collections import deque

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        dq_s = deque(i for i in s)
        cp_s = dq_s.copy()
        
        dq_g = deque(i for i in goal)
        
        for i in dq_s:
            cp_s.rotate(-1)

            if cp_s == dq_g:
                return True
            
        return False