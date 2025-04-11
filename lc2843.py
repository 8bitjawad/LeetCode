class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:


        count=0

        for num in range(low,high+1):
            num_str=str(num)
            length=len(num_str)

            if length%2 != 0:
                continue

            mid=length//2
            left=num_str[:mid]
            right=num_str[mid:]

            sum_left= sum(int(d) for d in left)
            sum_right= sum(int(d) for d in right)

            if sum_left == sum_right:
                count+=1

        return count


        