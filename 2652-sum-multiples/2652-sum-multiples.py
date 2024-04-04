class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # postieve integer n
        # find sum of all integers in range 1, n
        # that are divisble by 3, 5 or 7
        
        runningSum = 0
        
        for num in range(1,n+1):
            
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                runningSum += num
                
        return runningSum