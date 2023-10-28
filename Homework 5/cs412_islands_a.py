"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


def find_largest_island_size(n, grid):
    max_island_size = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                island_size = 0
                stack = [(i, j)]

                while stack:
                    x, y = stack.pop()
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 0
                        island_size += 1
                        stack.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

                max_island_size = max(max_island_size, island_size)

    return max_island_size


def main():
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    largest_island_size = find_largest_island_size(n, grid)
    print(largest_island_size)


if __name__ == "__main__":
    main()