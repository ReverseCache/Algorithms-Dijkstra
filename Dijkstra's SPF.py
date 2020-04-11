def SetLoop(s):
    for i in s:
        break
    return i

graphL = {'A': [['B', 7], ['C', 1]],
          'B': [['A', 7], ['C', 2], ['D', 3]],
          'C': [['A', 1], ['D', 4], ['B', 2]],
          'D': [['C', 4], ['B', 3]]
          }


visited = set()  # Set to keep track of visited nodes.
queue = set()  # Initialize a queue
empty = set()


def dijkstra():
    n = input("Inital node?")
    l = graphL.get(n, "key doesn't exist")
    if l == "key doesn't exist":
        return(l)
    else:
        d = {n: 0}  # the origin is always 0 away  # use dict() or {}
        d.update({x[0]: x[1] if len(x) == 2 else None for x in l})
        visited.add(n)
        queue = set(d.keys()) - visited
        while queue != empty:
            n = SetLoop(queue)
            l = graphL.get(n, "key doesn't exist")
            for x in l:
                if x[0] in d:  # x is [Letter , Number]
                    a = d.get(x[0], "key doesn't exist")
                    b = int(x[1]) + d.get(n, "key doesn't exist")
                    value = b if b < a else a
                    # like z = (i < x) ? i : x  in C/Java
                    key = x[0]
                    d.update({key: value})
                else:
                    # the int is redundant (standardisation)
                    value = int(x[1]) + d.get(n, "key doesn't exist")
                    key = x[0]
                    d.update({key: value})
            visited.add(n)
            queue = set(d.keys()) - visited
    return d


x = dijkstra()  # x becomes dictionary containing distances from inital node
for key in x:
    print("Shortest path from inital node to " + key + " is " + str(x[key]))
