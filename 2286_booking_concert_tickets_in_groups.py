class BookMyShow:

    def __init__(self, rows: int, seats: int):
        self.seats = seats
        self.rows = rows
        self.nodes = {}
        self.mnodes = {}
        self.build(0, rows-1)
        self.root_node = (0, rows - 1)


    def build(self, l: int, r: int):
        if l == r:
            self.nodes[(l,r)] = self.seats
            self.mnodes[(l,r)] = self.seats
        else:
            m = (l + r)//2
            self.build(l, m)
            self.build(m+1,r)
            self.nodes[(l,r)] = self.nodes[(l,m)] + self.nodes[(m+1, r)]
            self.mnodes[(l,r)] = self.seats


    def gather(self, k: int, maxRow: int) -> List[int]:
        xs = [ self.root_node ]
        p  = { self.root_node: None }

        i = 0
        history = []
        while xs:
            i += 1
            x, *xs = xs 

            a, b = x 
            v = self.nodes[x]

            if v < k:
                continue
            elif self.mnodes[x] < k:
                continue
            elif a == b:
                res = [a, self.seats - v]
                while x is not None:
                    self.nodes[x] -= k
                    a, b = x
                    if a == b:
                        self.mnodes[x] = self.nodes[x]
                    else:
                        m = (a + b)//2
                        l = (a, m)
                        r = (m+1, b)
                        self.mnodes[x] = max(self.mnodes[l], self.mnodes[r])
                    x = p[x]

                return res
            else:
                m = (a + b)//2
                l = (a, m)
                r = (m + 1, b)

                if m < maxRow and self.mnodes[r] >= k:
                    xs = [r] + xs
                    p[r] = x

                if self.mnodes[l] >= k:
                    xs = [l] + xs 
                    p[l] = x

        return []


    def scatter(self, k: int, maxRow: int) -> bool:
        updates = []
        removes = []
        xs = [(self.root_node, k)]
        while xs:
            (x, k), *xs = xs
            a, b = x
            v = self.nodes[x]

            if v == 0 and not xs:
                return False
            elif k == 0:
                continue
            elif v < k:
                return False
            elif a == b:
                updates.append((x, v - k))
            elif v == k and b <= maxRow:
                updates.append((x, 0))
            else:
                m = (a + b)//2
                l = (a, m)
                r = (m+1, b)

                updates.append((x, v - k))
                if maxRow < r[0]:
                    xs = [(l, k)] + xs
                else:
                    lk = min(k, self.nodes[l])
                    xs = [(l, lk), (r, k - lk)] + xs


        for x, v in updates:
            self.nodes[x] = v

        return True 



