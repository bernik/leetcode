from typing import List, Tuple

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width  = len(grid[0]) 
        ones = [(row, col) for row in range(height) 
                           for col in range(width) 
                           if grid[row][col] == 1]


        def neighbours(x: Tuple[int, int]) -> List[Tuple[int, int]]:
            row, col = x
            res = []
            if row + 1 < height:
                res.append((row + 1, col))
            if row - 1 >= 0:
                res.append((row - 1, col))
            if col + 1 < width:
                res.append((row, col + 1))
            if col - 1 >= 0:
                res.append((row, col - 1))

            return res


        visited = set()
        maxArea = 0
        for one in ones:
            if one in visited:
                continue

            area = 0
            xs = [one]
            while xs:
                x, *xs = xs 
                if grid[x[0]][x[1]] == 0:
                    continue

                if x in visited:
                    continue

                visited.add(x)
                area += 1
                xs += neighbours(x)

            maxArea = max(maxArea, area)

        return maxArea


s = Solution()
input = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
assert s.maxAreaOfIsland(input) == 6

input = [[0,1], [1,1]]
assert s.maxAreaOfIsland(input) == 3