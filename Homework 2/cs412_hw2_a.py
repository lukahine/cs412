"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    n = int(input())
    coord_pair = list(map(int, input().split()))
    i,j = (coord_pair[0], coord_pair[1])
    grid = [["00" for i in range(2**n)] for i in range(2**n)]
    grid[i][j] = "-1"
    if (i < (2**n)/2):
        # Top Left
        if (j < (2**n)/2): 
            pass
        # Top Right
        else:
            pass
    else:
        # Bottom Left
        if (j < (2**n)/2):
            pass
        # Bottom Right
        else:
            pass



    grid_printer(grid, 1)

def recur(grid, counter):
    if len(grid) == 4:
        pass


def grid_printer(grid):
    for arr in grid:
        print(" ".join(arr))

if __name__ == "__main__":
    main()