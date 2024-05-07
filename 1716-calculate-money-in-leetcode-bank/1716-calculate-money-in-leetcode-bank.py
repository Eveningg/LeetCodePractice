class Solution:
    def totalMoney(self, n: int) -> int:
        
        ans = 0
        monday = 1
        
        while n > 0:
            for day in range(min(n, 7)):
                ans += monday + day
            
            n -= 7
            monday += 1

        return ans
    
        counter = 0
        week = 0
        
        for i in range(n):
            if i % 7 == 0 and i != 0:
                week += 6
            counter += (i+1) - week
            
        return counter