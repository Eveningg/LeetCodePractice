class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hash = dict(zip(heights,names))
        res = []
        heights.sort(reverse=True)
        for h in heights:
            res.append(hash[h])
        return res