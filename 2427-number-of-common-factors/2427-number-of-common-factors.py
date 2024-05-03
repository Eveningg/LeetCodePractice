class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        count = 0
        minn = min(a,b) # minn = 6
        if max(a,b) % minn == 0: # // 12 % 6 is 0, so count = 1 now
            count +=1
        for i in range(1,(minn//2)+1): # range is 1 to (6//2+1) 
            if a % i == 0 and b % i ==0: # // the condition will be true when i = 1,2,3
                count +=1
        return count # count = 4