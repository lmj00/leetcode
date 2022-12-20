class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        ls = []
        
        for i in words:
            for j in range(len(words)):
                if i in words[j] and i != words[j] and i not in ls:
                    ls.append(i)
        
        return ls