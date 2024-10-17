class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum_t=n*(n+1)//2
        sum_a=sum(nums)
        return sum_t-sum_a
