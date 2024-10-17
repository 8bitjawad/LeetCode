class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        n=len(nums)
        m=len(s)
        if m!=n:
            return True
        else:
            return False
            