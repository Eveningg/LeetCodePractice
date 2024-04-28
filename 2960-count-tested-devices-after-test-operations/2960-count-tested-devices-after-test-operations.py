class Solution:
    def countTestedDevices(self, devices: List[int]) -> int:
        
        counter = 0
        
        for i in range(len(devices)):
            
            if devices[i] > counter:
                counter += 1
                
        return counter