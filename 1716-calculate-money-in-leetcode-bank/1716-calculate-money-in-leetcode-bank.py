class Solution:
    def totalMoney(self, n: int) -> int:
        
        counter = 0
        week = 0
        
        for i in range(n):
            if i % 7 == 0 and i != 0:
                week += 6
            counter += (i+1) - week
            
        return counter