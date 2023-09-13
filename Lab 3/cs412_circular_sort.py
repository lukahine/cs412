"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def main():
    in_list = list(map(int, input().split()))
    q = int(input())
    print(circle_sort(in_list, 0, len(in_list)-1, q))


def circle_sort(items, re_start, re_end, q):
    if re_start > re_end:
        return -1
    mid = (re_start + re_end) // 2
    # If the key is at the mid index return
    if items[mid] == q:
        return mid
    # If the first half is sorted
    if items[re_start] < items[mid]:
        if q >= items[re_start] and q <= items[mid]:
            return circle_sort(items, re_start, mid-1, q)
        # Otherwise search the other half
        return circle_sort(items, mid + 1, re_end, q)
    # If the key is in the second half
    if q >= items[mid] and q <= items[re_end]:
        return circle_sort(items, mid + 1, re_end, q)
    # Search the first half (likely unsorted)
    return circle_sort(items, re_start, mid-1, q)


if __name__ == "__main__":
    main()