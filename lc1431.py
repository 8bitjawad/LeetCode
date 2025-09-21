class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        result=[False]*len(candies)

        for i in range(len(candies)):
            temp= candies[i] +extraCandies
            if temp>=max(candies):
                result[i]=True

        return result

        