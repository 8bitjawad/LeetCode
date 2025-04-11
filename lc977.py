class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[0]*len(nums)
        # for i in range(len(nums)):
        #     squares[i]=nums[i]*nums[i]
        
        # squares.sort()
        n=len(nums)
        left,right=0,n-1
        pos=n-1

        while left <= right:
            if (nums[left]*nums[left]) > (nums[right]*nums[right]):
                squares[pos]=nums[left]*nums[left]
                left+=1

            else:
                squares[pos]=nums[right]*nums[right]
                right-=1

            pos-=1

        return squares


        