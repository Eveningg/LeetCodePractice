class Solution:
    def tribonacci(self, n: int) -> int:
        
        arr = [0,1,1]
        
        if n <= 2:
             return arr[n]
            
        for i in range(3,n+1):
            nextNumber = arr[i-3] + arr[i-2] + arr[i-1]
            arr.append(nextNumber)
            
        return arr[n]
            