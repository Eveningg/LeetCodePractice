class Solution:
    def countTestedDevices(self, devices: List[int]) -> int:
        
        n = len(devices)
        c = 0
        for i in range(n):
            if devices[i] > c:
                c += 1
        return c