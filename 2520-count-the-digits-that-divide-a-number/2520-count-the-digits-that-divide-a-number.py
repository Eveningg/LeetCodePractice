class Solution:
    def countDigits(self, num: int) -> int:
        
        n, res = num, 0
        while n>0:
            if num%(n%10)==0:
                res += 1
            n //= 10
        return res