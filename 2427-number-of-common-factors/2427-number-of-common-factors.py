class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        a_factors = []
        b_factors = []
        
        for i in range(1,a+1):
            if a % i == 0:
                a_factors.append(i)
                
        for i in range(1,b+1):
            if b % i == 0:
                b_factors.append(i)
                
        counter = 0
        for i in range(len(b_factors)):
            
            if b_factors[i] in a_factors:
                counter += 1
                
        return counter