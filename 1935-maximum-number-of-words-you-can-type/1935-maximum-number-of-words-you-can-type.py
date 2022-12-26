class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        broken = set(brokenLetters)
        count = 0
        
        for i in text:
            if len(set(i) & broken) == 0:
                print(i)
                count += 1


        return count