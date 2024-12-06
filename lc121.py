class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minimum=9999
        # n=len(prices)
        # for i in range(n):
        #     if(prices[i]<minimum):
        #         min_index=i
        #         minimum=prices[i]
        # diff=0
        # for i in range(min_index +1,n-1):
        #     if (prices[i]-minimum) > prices[i+1]-minimum:
        #         diff=prices[i]-minimum
        #     elif (prices[i+1]-minimum) > prices[i]-minimum:
        #         diff=prices[i+1]-minimum
         
        # return diff
        minimum_price = float('inf') 
        max_profit = 0  
        
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            profit = price - minimum_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
