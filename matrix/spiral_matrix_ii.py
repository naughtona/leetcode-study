import sys
import numpy as np

def generate_matrix(n):
    M = np.zeros((n,n), dtype=int)
    up, down = 0, M.shape[0]
    left, right = 0, M.shape[1]
    counter = 1
    while up < down and left < right:
        # up
        i = left
        while up < down and i < right:
            M[up,i] = counter
            counter += 1
            i += 1
        up += 1

        # right
        i = up
        while left < right and i < down:
            M[i,right-1] = counter
            counter += 1
            i += 1
        right -= 1

        # down
        i = right-1
        while up < down and i >= left:
            M[down-1,i] = counter
            counter += 1
            i -= 1
        down -= 1

        # left
        i = down-1
        while left < right and i >= up:
            M[i,left] = counter
            counter += 1
            i -= 1
        left += 1

    return M

if __name__ == '__main__':
    if len(sys.argv[1:]):
        print(sys.argv[1])
        n = int(sys.argv[1])
        print(generate_matrix(n))
