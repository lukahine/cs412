"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


def is_independent_set(graph_size, edges, vertex_set):
    adjacency_matrix = [[0] * graph_size for _ in range(graph_size)]

    for i in range(graph_size):
        for v in edges[i][1:]:
            adjacency_matrix[i][v] = 1
            adjacency_matrix[v][i] = 1

    for i in range(graph_size):
        for j in range(graph_size):
            if i in vertex_set and j in vertex_set and adjacency_matrix[i][j] == 1:
                return False

    return True


if __name__ == "__main__":
    graph_size = int(input())
    
    edges = []
    for _ in range(graph_size):
        edge_list = list(map(int, input().split()))
        edges.append(edge_list)

    independent_set = set(map(int, input().split()))

    result = is_independent_set(graph_size, edges, independent_set)

    print(result)
