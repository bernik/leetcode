import re 
import heapq


class Solution:

    def neighbours(self, password):
        groups = [(x, len(xs)) for xs, x in re.findall(r"((.)\2?\2?)", password)]
        groups_len = len(groups)
        
        result = {groups_len-1: [{ "g": groups_len, "v":"", "l": 0}]} 

        for i, group in enumerate(groups):
            result[i-1] = []
            x, n = group 

            if n <= 2:
                result[i-1].append({ "g": i, "v": x*n, "l": n })
                continue


            next_same_len = 0
            if i+1 < groups_len and groups[i+1][0] == x:
                next_same_len = groups[i+1][1]

            # aaa bbb -> aax  bbb
            # aaa aa  -> aax  aa
            # aaa aaa -> aax  aaa
            result[i-1].append({ "g": i, "v": x+x+"^", "l": 3, "r": 1 })

            # aaa bbb -> aa-  bbb
            if next_same_len == 0:
                result[i-1].append({ "g": i, "v": x+x+"-", "l": 2, "d": 1 })
            # aaa bbb -> a--  bbb
            # aaa a   -> a--  a
            if next_same_len <= 1:
                result[i-1].append({ "g": i, "v": x+"--", "l": 1, "d": 2 })
            # aaa a   -> aaba a
            # aaa b   -> aaba b
            if next_same_len <= 1:
                result[i-1].append({ "g": i, "v": x+x+"+"+x, "l": 4, "i": 1 })

            # aaa bbb -> ---  bbb
            # aaa aaa -> ---  aaa
            # aaa aa  -> ---  aa
            # aaa aa  -> x--  aa
            if next_same_len >= 2:
                result[i-1].append({ "g": i, "v": "---", "d": 3 })

        return result


    def strongPasswordChecker(self, password:str) -> int:
        password_length = len(password)
        inserts = 0
        deletes = 0

        if password_length < 6:
            inserts = 6 - password_length
        elif password_length > 20:
            deletes = password_length - 20

        types = 3
        if re.search(r"[a-z]", password): types -= 1
        if re.search(r"[A-Z]", password): types -= 1
        if re.search(r"[0-9]", password): types -= 1

        neighbours = self.neighbours(password)
        ops = {}
        pq = [(0, "start", {"v": "", "g": -1, "l": 0, "o": 0, "i": inserts, "d": deletes, "w": inserts + deletes})]
        visited = set()

        result = []

        while pq:
            weight, node_id, node = heapq.heappop(pq)
            if node_id in visited: continue

            if node["g"] not in neighbours: continue

            visited.add(node_id)

            for idx, next in enumerate(neighbours[node["g"]]):
                # _node_id = f"{node_id} {next['g']} {idx}"
                id = f"{node_id} {next['g']} {idx}"
                _node_id = f"{next['g']} {idx}"
                if node['g'] == max(neighbours.keys()): 
                    id = "finish"
                    _node_id = "finish"

                _node = {
                    "g": next["g"],
                    "v": node["v"] + next["v"],
                    "l": node.get("l", 0) + next.get("l", 0),
                    "o": node["o"] + next.get("i", 0) + next.get("d", 0) + next.get("r", 0),
                    "i": node["i"] - next.get("i", 0),
                    "d": node["d"] - next.get("d", 0),
                }
                _node["w"] = _node["o"] + _node["i"] + _node["d"]

                # if _node["l"] > 20: continue 
                if _node["i"] < 0: continue
                if _node["d"] < 0: continue

                if _node_id not in ops or ops[_node_id]["w"] >= _node["w"]: 
                    # ops[_node_id] = _node
                    ops[id] = _node
                    heapq.heappush(pq, (_node["w"], id, _node))


        return ops["finish"]["w"] + max(0, types - ops["finish"]["w"] + deletes)

