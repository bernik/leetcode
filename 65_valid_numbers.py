import re 

class Solution:
    def isNumber(self, s: str) -> bool:
        i = r"[+-]?\d+"
        d = r"[+-]?(\d+\.\d*|\d*\.\d+)"
        e = f"[eE]{i}"
        number = f"^({d}|{i})({e})?$"
        return re.match(number, s)
        
