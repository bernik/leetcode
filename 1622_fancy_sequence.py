class Fancy:

    MODULO = 1000000007

    def __init__(self):
        self.data = []
        self.ops = []
        self.ops_index = -1


    def append(self, val: int) -> None:
        self.data.append(val)
        self.ops.append({"+": 0, "*": 1})
        self.ops_index += 1


    def addAll(self, inc: int) -> None:
        if self.ops_index == -1:
            return
        self.ops[self.ops_index]["+"] += inc
        self.ops[self.ops_index]["+"] %= self.MODULO


    def multAll(self, m: int) -> None:
        if self.ops_index == -1:
            return
        self.ops[self.ops_index]["+"] *= m
        self.ops[self.ops_index]["+"] %= self.MODULO
        self.ops[self.ops_index]["*"] *= m
        self.ops[self.ops_index]["*"] %= self.MODULO


    def getIndex(self, idx: int) -> int:
        if idx >= len(self.data):
            return -1
        else:
            res = self.data[idx]
            for op in self.ops[idx:]:
                res *= op["*"]
                res += op["+"]
            return res % self.MODULO
