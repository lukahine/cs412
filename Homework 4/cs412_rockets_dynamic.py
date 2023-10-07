"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


def dp_min_sections(sections, target):
    dp = [[float('inf')] * (target + 1) for _ in range(len(sections))]
    dp[0][0] = 0

    for i in range(len(sections)):
        for j in range(target + 1):
            if j == 0:
                dp[i][j] = 0
            else:
                if sections[i] <= j:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - sections[i]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

    return dp


def main():
    sections = list(map(int, input().split()))
    target = int(input())

    dp = dp_min_sections(sections, target)
    min_sections = dp[len(sections) - 1][target]
    
    if min_sections == float('inf'):
        print("No valid solution exists.")
    else:
        print(f"{min_sections} rocket sections minimum")


if __name__ == "__main__":
    main()