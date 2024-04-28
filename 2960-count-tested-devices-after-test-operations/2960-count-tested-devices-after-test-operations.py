class Solution:
    def countTestedDevices(self, devices: List[int]) -> int:
        
        num = len(devices)
        counter = 0
        
        for i in range(num):
            
            if devices[i] > counter:
                counter += 1
                
        return counter
    
        #[0,1,2]
        
        # 1 > 0 , counter becomes 1
        # 2 > 1 , counter becomes 2