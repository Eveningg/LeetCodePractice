class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        #float celsius - rounded to two decimals
        
        ans = []
        
        kelvin = celsius + 273.15
        fahreheit = celsius * 1.80 + 32.00
        ans.append(kelvin)
        ans.append(fahreheit)
        
        return ans