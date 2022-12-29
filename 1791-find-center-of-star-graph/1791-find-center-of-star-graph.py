import itertools
from collections import Counter

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        ls = list(itertools.chain(*edges))
        
        return Counter(ls).most_common()[0][0]        