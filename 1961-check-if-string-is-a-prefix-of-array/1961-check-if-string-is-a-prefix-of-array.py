class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        ss = ''
        
        for i in range(len(words)):
            ss += words[i]
            
            if s == ss:
                return True
        
        return False