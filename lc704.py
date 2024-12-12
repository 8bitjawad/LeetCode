class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        L,R=0,n-1

        while L <= R:
            mid=(L+R)//2

            if target==nums[mid]:
                return mid
            
            elif target<nums[mid]:
                R=mid-1

            else:
                L=mid+1
        
        return -1

        