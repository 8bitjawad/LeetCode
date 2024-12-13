from collections import deque
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score=0
        n=len(nums)
        marked=[False]*n
        sorted_idx = sorted(range(n), key=lambda x: nums[x])
        #function returns sorted indexes such that sorted_idx[i] gives the index at which nums has the smallest element and so on

        for i in sorted_idx:

            if not marked[i]:
                score+=nums[i]
                marked[i]=True

                if i-1>=0:
                    marked[i-1]=True
                if i+1<n:
                    marked[i+1]=True
        
        return score




            






                
           



