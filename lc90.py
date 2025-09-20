class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        subset=[]
        seen=set()
        nums.sort()

        def dfs(i):
            if i>=len(nums):
                t=tuple(subset)
                if t not in seen:
                    res.append(subset.copy())
                    seen.add(t)
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res