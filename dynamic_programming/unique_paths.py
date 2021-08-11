DIRECTIONS = [(1,0), (0,1)] # down, right

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def valid_pos(r,c):
            return r >= 0 and r < m and c >= 0 and c < n
        
        def rec(row, col, cache):
            if row == m-1 and col == n-1: return 1
            elif not valid_pos(row, col): return 0
            
            if (row,col) in cache: return cache[(row,col)]
            
            count = 0
            for row_add, col_add in DIRECTIONS:
                new_pos = (row+row_add, col+col_add)
                count += rec(*new_pos, cache)
            
            cache[(row,col)] = count
            return cache[(row,col)]
        
        return rec(0,0,{})
