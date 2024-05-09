class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        hash_set = []
        
        for i in range(len(prices)):
            hash_set.append(prices[i])
            
            for j in range(i+1,len(prices)):

                if prices[i] >= prices[j]:
                    newPrice = prices[i] - prices[j]
                    hash_set[i] = newPrice
                    break
                    
        return hash_set
            