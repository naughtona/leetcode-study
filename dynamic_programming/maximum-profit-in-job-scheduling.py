class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def find(time):
            i = len(dp) - 1
            while i >= 0:
                if dp[i][0] <= time:
                    return dp[i][1]
                i -= 1
        
        dp = [(0,0)]
        schedule = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        for st, en, pr in schedule:
            dp.append((en, max(find(en), find(st) + pr)))
        return dp[-1][1]
