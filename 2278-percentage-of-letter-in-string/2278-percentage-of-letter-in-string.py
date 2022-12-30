from collections import Counter
import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        v = list(filter(lambda x: x[0] == letter, Counter(s).most_common()))
        
        return 0 if len(v) == 0 else math.trunc(v[0][1] / len(s) * 100)