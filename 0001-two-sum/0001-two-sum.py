class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Iterating Through Integer List
        for counter, integer in enumerate(nums):
            
            # Iterating Through Integer List Again
            for counter2, integer2 in enumerate(nums):
                
                if integer + integer2 == target and counter != counter2:
                    
                    return(counter,counter2)
            

    