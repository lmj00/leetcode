from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        return Counter(s).most_common()[0][1] == Counter(s).most_common()[-1][1]