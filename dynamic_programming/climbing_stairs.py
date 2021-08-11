class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            dic = {2:2, 3:3}
            for i in range(4,n+1):
                dic[i] = dic[i-1] + dic[i-2]
        
        return dic[n]

#        # slow sol 1:
#        stack, n_ways = [0], 0
#        while stack:
#            n_steps = stack.pop()
#            if n_steps == n:
#                n_ways += 1
#            elif n_steps < n-1:
#                stack += [n_steps+1] + [n_steps+2]
#            else:
#                stack += [n_steps+1]
#        return n_ways

#        # slow sol 2:
#        if n <= 2:
#            return n
#        else:
#            return climbStairs(n-1) + climbStairs(n-2)

