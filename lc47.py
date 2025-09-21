class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res=[]
        seen=set()
        nums.sort()
        used=[False]*len(nums)

        def dfs(perm):
            if len(perm)==len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                perm.append(nums[i])
                used[i]=True
                dfs(perm)
                perm.pop()
                used[i]=False
            
        dfs([])
        return res