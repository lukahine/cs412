"""
    name:  Your name(s) here

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    in_list = list(map(int,input().split()))
    q = int(input())
    print(recur(in_list,q))

def recur(par_list, q):
    size = len(par_list)
    # If if the middle isnt the query
    if par_list[size / 2] != q:
        # if the first half of the list is sorted
        if par_list[0] <= par_list[(size / 2) - 1]:
            return recur(par_list[0 : (size / 2)]) + size / 2 
        else:
            return recur(par_list[size / 2 : size]) + size / 2
    else:
        return



if __name__ == "__main__":
    main()