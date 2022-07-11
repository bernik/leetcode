class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {}
        def f(i):
            if i in mem:
                return mem[i]
            
            n = len(cost) - i - 1
            res = 0
            if n < 0:
                res = 0
            elif n == 0:
                res = cost[i]
            else:
                res = cost[i] + min(f(i+1), f(i+2))
                
            mem[i] = res
            return res
            
        return min(f(0), f(1))
                