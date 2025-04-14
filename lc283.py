class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        start,end=0,n


        for i in range(n):
            if nums[i] != 0:
                nums[start]=nums[i]
                start+=1
            
            else:
                continue

        for i in range(start,end):
            nums[i]=0

        return nums
            
            
           