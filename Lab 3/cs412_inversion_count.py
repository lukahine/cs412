"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def mergesort(A):
    if len(A) > 1:
        # Get the mid point
        m = len(A) // 2

        # Get the left and right halves
        left, right = A[:m], A[m:]

        # sort the left and right halves
        mergesort(left)
        mergesort(right)

        # Run the merge operation on A
        merge(A, m)


def merge(A, m):
    i, j = 0, m
    global inversions
    n = len(A)
    B = [0 for _ in range(n)]

    for k in range(n):
        if j >= n:
            B[k] = A[i]
            i += 1
        elif i >= m:
            B[k] = A[j]
            j += 1
        elif A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            inversions += 1
    for k in range(n):
        A[k] = B[k]
        

def main():
    global inversions
    inversions = 0
    in_list = list(map(int, input().split()))
    mergesort(in_list)
    print(inversions)


if __name__ == "__main__":
    main()
