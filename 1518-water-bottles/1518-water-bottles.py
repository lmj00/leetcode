class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    
        result = numBottles
        
        while True:
            share = numBottles // numExchange
            remainder = numBottles % numExchange
            result += share
            
            numBottles = share + remainder
                
            if numBottles < numExchange:
                return result