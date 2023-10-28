"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


def find_route(stopDict, start, end):
    visited = set()
    stack = []
    path = []

    def dfs(node):
        if node == end:
            path.append(node)
            return True

        visited.add(node)
        for neighbor in stopDict.get(node, set()):
            if neighbor not in visited:
                if dfs(neighbor):
                    path.append(node)
                    return True

        return False

    if dfs(start):
        path.reverse()
        return path
    else:
        return "no route possible"


def main():
    numLines = int(input())
    stopDict = {}
    for _ in range(numLines):
        u, v = input().split()
        if u not in stopDict:
            stopDict[u] = set()
        if v not in stopDict:
            stopDict[v] = set()
        stopDict[u].add(v)
        stopDict[v].add(u)
    start, end = input().split()

    route = find_route(stopDict, start, end)
    if route == "no route possible":
        print(route)
    else:
        print(" ".join(route))


if __name__ == "__main__":
    main()

