from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        res = 0
        while truckSize > 0 and boxTypes: 
            [n, x], *boxTypes = boxTypes

            tmp = min(n, truckSize)
            res += tmp * x
            truckSize -= tmp

        return res




s = Solution()
assert s.maximumUnits([[1,3],[2,2],[3,1]], 4) == 8
assert s.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10) == 91