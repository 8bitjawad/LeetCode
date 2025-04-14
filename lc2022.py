class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if(len(original) !=m*n):
            return []

        arr=[[0 for _ in range(n)] for _ in range(m)]

        index=0
        for i in range(m):
            for j in range(n):
                arr[i][j]=original[index]
                index+=1    

        return arr