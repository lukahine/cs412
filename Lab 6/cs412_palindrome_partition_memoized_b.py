"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

        This work complies with the JMU Honor Code.
"""


def is_palindrome(s):
    return s == s[::-1]


def count_palindrome_parts(input_string):
    memo = {}

    def backtrack(start):
        if start == len(input_string):
            return 1

        if start in memo:
            return memo[start]

        count = 0
        for end in range(start + 1, len(input_string) + 1):
            if is_palindrome(input_string[start:end]):
                count += backtrack(end)

        memo[start] = count
        return count

    return backtrack(0)

def main():
    n = int(input())
    for _ in range(n):
        letters = input()
        print(count_palindrome_parts(letters))

if __name__ == "__main__":
    main()
