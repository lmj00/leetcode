class Solution:
    def interpret(self, command: str) -> str:
        
        check = 0
        v = ''
        
        for c in command:
            if c == '(':
                check = 0

            elif c == ')':
                if check == 0:
                    v += 'o'
                
            else:
                v += c
                check += 1
        return v
            
