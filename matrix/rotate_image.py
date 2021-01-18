from typing import List
# import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                # top row and right col
                matrix[l][l+i], matrix[l+i][r] = matrix[l+i][r], matrix[l][l+i]
                # right col and bottom row
                matrix[l][l+i], matrix[r][r-i] = matrix[r][r-i], matrix[l][l+i]
                # bottom row and left col
                matrix[l][l+i], matrix[r-i][l] = matrix[r-i][l], matrix[l][l+i]

            l+=1; r-=1
        
        # return np.matrix(matrix)
