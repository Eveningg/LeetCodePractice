class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        totalTime = arrivalTime + delayedTime
        
        return totalTime if totalTime < 24 else totalTime - 24