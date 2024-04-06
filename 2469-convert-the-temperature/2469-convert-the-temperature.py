class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        ans = []
        
        kelvin = celsius + 273.15
        fahreheit = celsius * 1.80 + 32.00
        ans.append(kelvin)
        ans.append(fahreheit)
        
        return ans
    
        # one-liner
        
        return [celsius + 273.15, celsius * 1.80 + 32.00]