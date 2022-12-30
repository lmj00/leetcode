from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        v = Counter(s).most_common()
        ss = ''
        
        if v[0][1] == v[-1][1]:
            return sorted(s)
        
        for i in v:
            ss += i[0] * i[1]

        return ss