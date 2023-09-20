"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


def backtrack(sections, target, current, min, result):
    # Base Case : Reached 0 left, checks if result is better than min
    if target == 0:
        if len(current) < min[0]:
            min[0] = len(current)
            result[0] = current.copy()
        return

    # Moves forward with every possible option considering remaining length
    for section in sections:
        if section <= target:
            current.append(section)
            backtrack(sections, target - section, current, min, result)
            current.pop()


def main():
    sections = list(map(int, input().split()))
    target = int(input())

    # min is infinity so that anything will be better than it
    min = [float('inf')]
    # This made it easier to store the best result
    result = [[]]

    backtrack(sections, target, [], min, result)

    for section_length in sorted(set(sections)):
        count = result[0].count(section_length)
        print(f"{count} of length {section_length}")

    print(f"{min[0]} rocket sections minimum")


if __name__ == "__main__":
    main()