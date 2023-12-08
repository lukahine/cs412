"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


from collections import deque


def zero_flow(graph):
    flow = [dict() for _ in range(len(graph))]
    for u in range(len(graph)):
        for v in graph[u]:
            flow[u][v] = (0, graph[u][v])
    return flow


def residual(G, f, num_nodes):
    residual = [dict() for _ in range(num_nodes)]
    for u in range(num_nodes):
        for v in G[u]:
            if G[u][v] - f[u][v][0] != 0:
                residual[u][v] = f[u][v][1] - f[u][v][0]
            if f[u][v][0] != 0:
                residual[v][u] = f[u][v][0]
    return residual


def augment(G_f, num_nodes):
    n = num_nodes
    g = G_f

    def bfs(s=0, t=n - 1):
        prev = solve(s)
        return reconPath(prev)

    def reconPath(prev, s=0, t=n-1):
        path = []
        curr = t
        while curr is not None:
            path.append(curr)
            curr = prev[curr]
        path.reverse()
        if path[0] == s:
            return path
        return []

    def solve(s):
        q = deque()
        q.append(s)
        visited = [False for _ in range(num_nodes)]
        visited[s] = True
        prev = [None for _ in range(num_nodes)]
        while q:
            node = q.popleft()
            neighbors = g[node]
            for next_node in neighbors:
                if not visited[next_node]:
                    q.append(next_node)
                    visited[next_node] = True
                    prev[next_node] = node
        return prev

    return bfs()


def update_flow(P, f):
    min_capacity = float('inf')
    for i in range(len(P) - 1):
        u, v = P[i], P[i + 1]
        _, capacity = f[u][v]
        if capacity < min_capacity:
            min_capacity = capacity
    for i in range(len(P) - 1):
        u, v = P[i], P[i + 1]
        f[u][v] = (f[u][v][0] + min_capacity, f[u][v][1])
    return f


def cut_S(G_f):
    q = deque()
    q.append(0)
    visited = []
    while q:
        curr = q.popleft()
        for neighbor in G_f[curr]:
            if neighbor not in visited:
                q.append(neighbor)
        visited.append(curr)
    return visited


def fulk(G, num_nodes):
    f = zero_flow(G)
    G_f = residual(G, f, num_nodes)
    P = augment(G_f, num_nodes)
    while P:
        f = update_flow(P, f)
        G_f = residual(G, f, num_nodes)
        P = augment(G_f, num_nodes)
    S = cut_S(G_f)
    min_cuts = []
    flow = 0
    for u in range(num_nodes):
        for v in f[u]:
            if f[u][v][0] != 0 and u in S and v not in S:
                min_cuts.append((u, v))
                flow += f[u][v][0]
    print(flow)
    min_cuts.sort()
    for cut in min_cuts:
        print(f'{cut[0]} {cut[1]}')


def main():
    num_nodes, num_edges = [int(i) for i in input().split()]

    graph = [dict() for _ in range(num_nodes)]
    for _ in range(num_edges):
        u, v, c = [int(i) for i in input().split()]
        graph[u][v] = c

    fulk(graph, num_nodes)


if __name__ == "__main__":
    main()
