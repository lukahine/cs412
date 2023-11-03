"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


from queue import PriorityQueue


def dijkstra(graph, source, destination):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0

    pq = PriorityQueue()
    pq.put((0, source))

    while not pq.empty():
        d, u = pq.get()
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pq.put((dist[v], v))

    if dist[destination] == float('inf'):
        return "Impossible"
    return dist[destination]


def main():
    n, m, q = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    for _ in range(q):
        s, t = map(int, input().split())
        result = dijkstra(graph, s, t)
        print(result)


if __name__ == "__main__":
    main()