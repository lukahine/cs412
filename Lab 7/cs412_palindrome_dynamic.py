"""
    name:  Luke Hine

    Honor Code and Acknowledgments:
        This work complies with the JMU Honor Code.
        The loop on line 22 has a runtime of O(n)
        The loop on line 24 has a runtime of O(n^2)
        Therefore the runtime of the algorithm is O(n^2)
"""


def is_palindrome(s):
    return s == s[::-1]


def count_palindrome_parts(input_string):
    n = len(input_string)
    memo = [0] * (n + 1)

    memo[n] = 1

    for start in range(n - 1, -1, -1):
        count = 0
        for end in range(start + 1, n + 1):
            if is_palindrome(input_string[start:end]):
                count += memo[end]
        memo[start] = count

    return memo[0]


def main():
    n = int(input())
    for _ in range(n):
        letters = input()
        print(count_palindrome_parts(letters))


if __name__ == "__main__":
    main()
