class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res=[]
        curr=[]
        total=0

        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i>=len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i,curr,total+candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
        
        dfs(0,curr,total)
        return res