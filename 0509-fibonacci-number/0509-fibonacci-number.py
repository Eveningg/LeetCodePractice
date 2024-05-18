class Solution:
    def fib(self, n: int) -> int:
        
        fib = [0,1]
        
        if n <= 1:
            return fib[n]
        
        for i in range(1, n):
            newNumber = fib[i] + fib[i-1]
            fib.append(newNumber)
            
        return newNumber
    