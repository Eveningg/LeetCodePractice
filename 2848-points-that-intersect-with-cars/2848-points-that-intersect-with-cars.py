class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        s = set()
        for start, end in nums:
            s|= set(range(start, end+1))

        return len(s)