class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        n = len(timeSeries)
        poisoned_time = 0

        for i in range(n-1):
            # calculate the duration of the poison effect
            duration_of_effect = min(duration, timeSeries[i+1]-timeSeries[i])
            poisoned_time += duration_of_effect

        # add the duration of the last poison effect
        poisoned_time += duration

        return poisoned_time
