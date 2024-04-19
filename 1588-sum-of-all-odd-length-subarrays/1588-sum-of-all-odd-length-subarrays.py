class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        
        counter = 0

        for i in range(len(arr)):
            cur = 0
            for j in range(i, len(arr), 2):
                if j > i:
                    cur += arr[j] + arr[j - 1]
                else:
                    cur += arr[j]
                counter += cur

        return counter
            
            