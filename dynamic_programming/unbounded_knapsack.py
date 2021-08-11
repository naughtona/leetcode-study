import sys
sys.setrecursionlimit(2500)

def unboundedKnapsack(k, arr):
    def rec(left, cache):
        if left < 0: return -1
        elif left == 0: return 0

        if cache[left-1]: return cache[left-1]

        min_left = left
        for n in arr:
            res = rec(left-n, cache)

            if res == 0:
                min_left = res
                break
            elif res > 0:
                min_left = min(min_left, res)

        cache[left-1] = min_left
        return cache[left-1]

    return k - rec(k, [0] * k)
    
#    # naive, slow sol: 
#    def rec(remaining, pos, best):
#        for i, n in enumerate(arr[pos:]):
#            if remaining-n == 0: return k
#            elif remaining-n < 0: continue
#            else:
#                best = max(k-(remaining-n), rec(remaining-n, pos+i, best))
#        return best
#
#    return rec(k,0,0)
