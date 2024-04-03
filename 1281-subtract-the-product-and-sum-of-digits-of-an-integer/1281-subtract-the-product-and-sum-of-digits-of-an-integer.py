class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        prod = 1        # n =234
        sums = 0
        
        while n != 0:   
            
            last = n % 10   #returns 4
            prod *= last    
            sums += last    
            n = n // 10  # // makes it integer, rounds down.  
            
        return prod - sums  
            