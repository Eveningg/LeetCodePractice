class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
          # This task is awful, not because it's difficult, because the accepted answer doesn't work as set out by the task lol???
            
          # set creates a new list without duplicate values,as a set can't have duplicate values
          s = set(nums)
        
          # removing all elements from nums
          nums.clear()
        
          #iterating through our set s, appending all values to original array nums
          for i in s:
               nums.append(i)
                
          # this sort function is ESSENTIAL to the solution of this program. Removing this breaks the program.
        # HOWEVER, the input is exactly the same before and after the sort??? awful task lol.
          nums.sort()
          return len(nums)