# Link: https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n=len(matrix)
        m=len(matrix[0])

        self.matrix2=[[0]*(m+1) for _ in range(n+1)]

        self.matrix2[0][0]=matrix[0][0]
        for i in range(1,n):
            self.matrix2[i][0]=matrix[i][0]+self.matrix2[i-1][0]  

        for j in range(1,m):
            self.matrix2[0][j]=matrix[0][j]+self.matrix2[0][j-1]
                
        for i in range(1,n):
            for j in range(1,m):
                self.matrix2[i][j]=matrix[i][j]+self.matrix2[i][j-1]+self.matrix2[i-1][j]-self.matrix2[i-1][j-1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if len(self.matrix2)==1 and len(self.matrix2[0])==1:
            return self.matrix2[0][0]

        return self.matrix2[row2][col2]-(self.matrix2[row1-1][col2]+self.matrix2[row2][col1-1])+self.matrix2[row1-1][col1-1]

