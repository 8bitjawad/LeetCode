class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        l={}
        # for number in nums:
        #     l[number]=0
        for number in nums:
            if number in l:
                l[number]+=1
            else:
                l[number]=1
        for number in nums:
            if l[number]==1:
                return number