class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # n=len(nums)
        # h={}
        # for i in range(n):
        #     if nums[i] in h:
        #         h[nums[i]]+=1

        #     else:
        #         h[nums[i]]=1

        # majority = max(h,key=h.get)

        # return majority

        #boyer-moore voting algorithm

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
