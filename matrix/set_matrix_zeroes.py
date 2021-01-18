from typing import List
# import numpy as np

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ## time => O(M * N)
        ## space => O(M + N)

        m = len(matrix)
        n = len(matrix[0])
        zrows = set()
        zcols = set()
        for y in range(m):
            for x in range(n):
                if matrix[y][x]==0:
                    zrows.add(y)
                    zcols.add(x)
        for y in zrows:
            matrix[y] = [0]*n
        for y in range(m):
            for x in zcols:
                matrix[y][x] = 0

        # return np.matrix(matrix)

        
        ## time => O(M * N)
        ## space => O(1)

        # m = len(matrix)
        # n = len(matrix[0])
        # fcol = False
        # for y in range(m):
        #     if matrix[y][0]==0:
        #         fcol = True
        #     for x in range(1,n):
        #         if matrix[y][x]==0:
        #             matrix[y][0] = 0
        #             matrix[0][x] = 0

        # for y in range(1,m):
        #     for x in range(1,n):
        #         if matrix[y][0]==0 or matrix[0][x]==0:
        #             matrix[y][x] = 0

        # if matrix[0][0]==0:
        #     for x in range(n):
        #         matrix[0][x] = 0

        # if fcol:
        #     for y in range(m):
        #         matrix[y][0] = 0

        