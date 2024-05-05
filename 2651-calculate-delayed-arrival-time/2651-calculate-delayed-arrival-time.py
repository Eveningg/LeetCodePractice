class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        totalTime = arrivalTime + delayedTime
        
        if totalTime >= 24:
            return totalTime - 24
        
        return totalTime