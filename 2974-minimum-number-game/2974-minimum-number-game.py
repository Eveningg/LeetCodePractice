class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # arr nums - even length
        # empty arr arr
        
        # alice will remove the minimum element from nums
        # bob does the same
        
        # alice will append the removed elemeent in the array arr
        # alice does the same
        
        arr = []
        
        while len(nums) > 0:
            
            removedNum = min(nums)
            nums.remove(min(nums))
            removedNum2 = min(nums)
            nums.remove(min(nums))
                
            arr.append(removedNum2)
            arr.append(removedNum)
                
        return arr
                
            
                
            
        
        