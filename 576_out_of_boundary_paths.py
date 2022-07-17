class Solution:

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10**9+7
        mem = {}
        def dfs(i: int, j: int, moves: int):
            if moves == 0:
                return 0

            if not (0 <= i < m and 0 <= j <n):
                return 0

            if (i,j,moves) in mem:
                return mem[(i,j,moves)]

            res = 0
            if i == 0:
                res += 1
            if i == m-1:
                res += 1
            if j == 0: 
                res += 1
            if j == n-1:
                res += 1

            res += dfs(i-1, j, moves-1) + dfs(i+1, j, moves-1) + dfs(i, j-1, moves-1) + dfs(i, j+1, moves-1)
            res %= modulo
            mem[(i,j,moves)] = res
            return res 

        return dfs(startRow, startColumn, maxMove)


s = Solution()
assert s.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0) == 6
assert s.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1) == 12
