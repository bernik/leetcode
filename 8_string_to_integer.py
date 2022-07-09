import re

class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = r" *(?P<sign>[-+])?0*(?P<num>\d+)"
        match = re.match(pattern, s) 
        if not match:
            return 0

        sign = match.group('sign')
        if not sign:
            sign = "+"

        num = int(match.group('num'))

        if sign == "+":
            return min(2**31-1, num)
        else:
            return -1 * min(2**31, num)
