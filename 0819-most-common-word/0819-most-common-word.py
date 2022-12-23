from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        s = re.split(r"[ !?',;.]", paragraph.lower())
        
        for i in Counter(s).most_common():
            if i[0] != '' and i[0] not in banned:
                return i[0]