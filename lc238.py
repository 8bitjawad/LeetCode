class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(N) space solution
        # n = len(nums)
        # answer=[1]*n
        # prefix=[1]*n
        # suffix=[1]*n

        # for i in range(n):
        #     if i==0:
        #         prefix[i]=1
        #     elif i==1:
        #         prefix[i]=nums[i-1]
        #     else:
        #         prefix[i]=nums[i-1]*prefix[i-1] #prefix=[1,1,2,6]

        # running_product=1

        # for i in range(n-1,-1,-1):
        #     suffix[i]=running_product
        #     running_product*=nums[i]

        # for i in range(n):
        #     answer[i]=prefix[i]*suffix[i]

        # return answer

#O(1) space solution
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        running_suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= running_suffix
            running_suffix *= nums[i]

        return answer
