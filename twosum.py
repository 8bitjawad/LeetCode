class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[nums[i]]=i

        for i in range(len(nums)):
            y=target-nums[i]
            if y in h and h[y]!=i:
                return [i,h[y]]

        # two pointers
        # paired=[(num,i) for i,num in enumerate(nums)]
        # paired.sort()
    
        # front, back = 0,len(paired)-1


        # while front < back:
        #     total= paired[front][0] + paired[back][0]

        #     if total == target:
        #         return paired[front][1],paired[back][1]

        #     elif total < target:
        #         front+=1
            
        #     else:
        #         back-=1
        
