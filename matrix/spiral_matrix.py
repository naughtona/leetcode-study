from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lc, rc = 0, len(matrix[0]) - 1
        lr, rr = 0, len(matrix) - 1
        
        res = []
        i = 0
        while lc <= rc and lr <= rr:
            res.extend([matrix[lr][x] for x in range(lc,rc+1)])
            lr += 1
            if lr > rr:
                break
            res.extend([matrix[y][rc] for y in range(lr,rr+1)])
            rc -= 1
            if lc > rc:
                break
            res.extend([matrix[rr][x] for x in range(rc,lc-1,-1)])
            rr -= 1
            res.extend([matrix[y][lc] for y in range(rr,lr-1,-1)])
            lc += 1
            i+=1
        
        return res

# >>> from spiral_matrix import Solution
# >>> Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
# >>> Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]