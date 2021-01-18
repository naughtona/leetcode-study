from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        target = len(word)

        def search(i,j,curr,seen):
            if curr == target:
                return True
            # top
            if i+1 < m and (i+1,j) not in seen and board[i+1][j] == word[curr]:
                if search(i+1,j,curr+1,seen + [(i+1,j)]):
                    return True
            # bottom
            if i-1 >= 0 and (i-1,j) not in seen and board[i-1][j] == word[curr]:
                if search(i-1,j,curr+1,seen + [(i-1,j)]):
                    return True
            # left
            if j-1 >= 0 and (i,j-1) not in seen and board[i][j-1] == word[curr]:
                if search(i,j-1,curr+1,seen + [(i,j-1)]):
                    return True
            # right
            elif j+1 < n and (i,j+1) not in seen and board[i][j+1] == word[curr]:
                if search(i,j+1,curr+1,seen + [(i,j+1)]):
                    return True
            else:
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i,j,1,[(i,j)]):
                        return True
        return False

# >>> from word_search import Solution
# >>> Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
# True
# >>> Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
# True
# >>> Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
# False
