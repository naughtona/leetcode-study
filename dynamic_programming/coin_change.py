import sys
def coinChange(self, coins: List[int], amount: int) -> int:
    if not amount:
        return 0
    def rec(remaining, cache):
        if remaining < 0: return -1
        elif remaining == 0: return 0
        
        if cache[remaining-1]: return cache[remaining-1]
        
        min_n_coins = sys.maxsize
        for coin in coins:
            n_coins = 1 + rec(remaining-coin, cache)
            
            if n_coins > 0:
                min_n_coins = min(min_n_coins, n_coins)
        
        cache[remaining-1] = -1 if min_n_coins == sys.maxsize else min_n_coins
        return cache[remaining-1]
    
    return rec(amount, [0] * amount)
