class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        r =  numBottles 
        
        while numBottles >= numExchange:
            j = numBottles // numExchange
            k = j // numExchange
            r += j 
            k = (numBottles % numExchange)
            numBottles = j +k 
            
        return r
