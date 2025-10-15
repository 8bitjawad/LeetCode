class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        max_w=0
        num_zero = 0

        for r in range(n):
            if nums[r] == 0:
                num_zero +=1
            
            while num_zero > 1:
                if nums[l] == 0:
                    num_zero -=1
                l+=1

            w = r - l
            max_w = max(max_w,w)

            
        return max_w