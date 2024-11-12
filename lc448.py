class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l={}
        for i in nums:
            l[i]=True
        missing=[]
        for i in range (1,n+1):
            if(i not in l):
                missing.append(i)
        return missing
    
#  class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         dp = [0] * (len(nums)+1)

#         for number in nums:
#             dp[number] += 1

#         result = []
#         for i in range(1,len(dp)):
#             if dp[i] == 0:
#                 result.append(i)

#         return result 