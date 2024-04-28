class Solution:
    def countTestedDevices(self, v: List[int]) -> int:
        
        n = len(v)
        c = 0
        for i in range(n):
            if v[i] > c:
                c += 1
        return c