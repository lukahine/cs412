"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


import math


# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Implementation of Prim's algorithm to find the minimum spanning tree
def prim(graph):
    n = len(graph)
    in_mst = [False] * n
    in_mst[0] = True
    mst_cost = 0
    edges = []

    while len(edges) < n - 1:
        min_edge = (float('inf'), None, None)
        for u in range(n):
            if in_mst[u]:
                for v, weight in graph[u].items():
                    if not in_mst[v] and weight < min_edge[0]:
                        min_edge = (weight, u, v)
        weight, u, v = min_edge
        in_mst[v] = True
        mst_cost += weight
        edges.append((u, v, weight))

    return mst_cost

# Parse input and build the graph with edge weights
def build_graph(city_coordinates):
    n = len(city_coordinates)
    graph = {i: {} for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            distance = calculate_distance(city_coordinates[i], city_coordinates[j])
            graph[i][j] = distance
            graph[j][i] = distance
    return graph

def main():
    n = int(input())
    city_coordinates = [tuple(map(float, input().split())) for _ in range(n)]
    graph = build_graph(city_coordinates)
    min_cost = prim(graph)
    print(f"${min_cost:.1f}M")

if __name__ == "__main__":
    main()