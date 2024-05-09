class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result=0
        for i in range(len(grid[0])):
            temp=[]
            for j in range(len(grid)):
                ele=max(grid[j])
                temp.append(max(grid[j]))
                grid[j].remove(ele)
            result += max(temp)
        return result