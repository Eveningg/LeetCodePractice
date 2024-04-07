class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #array nums 
        #1, 2, 3, 4, 5, 6
        #1, 4, 2, 5, 3, 6
        
        pointer = len(nums) // 2
        emptyArr = []
        
        print(pointer)
        
        for i in nums:
            
            if len(nums) == len(emptyArr):
                break
                
            emptyArr.append(i)
            emptyArr.append(nums[pointer])
            
            pointer += 1
        
        return emptyArr
            