"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""


from itertools import product


def generate_boolean_assignments():
    boolean_values = [False, True]
    variable_combinations = product(boolean_values, repeat=3)

    for assignment in variable_combinations:
        x1, x2, x3 = assignment
        result = evaluate_3sat_B3(x1, x2, x3)
        if result:
            print(f'Satisfied: True\n')
            print(f'Satisfied Values: x1={x1}, x2={x2}, x3={x3}\n')
            return

    print('No satisfying assignment found.')


def evaluate_3sat_B2(x1, x2, x3):    
    clause1 = x1 or x2 or x3
    clause2 = (not x1) or x2 or x3
    clause3 = x1 or (not x2) or x3
    clause4 = x1 or x2 or (not x3)
    clause5 = (not x1) or (not x2) or x3
    clause6 = (not x1) or x2 or (not x3)
    clause7 = x1 or (not x2) or (not x3)
    clause8 = (not x1) or (not x2) or (not x3)

    return clause1 and clause2 and clause3 and clause4 and clause5 and clause6 and clause7 and clause8


def evaluate_3sat_B3(x1, x2, x3):    
    clause1 = x1 or x2 or x3
    clause2 = (not x1) or x2 or x3
    clause3 = x1 or (not x2) or x3
    clause4 = x1 or x2 or (not x3)
    clause5 = (not x1) or (not x2) or x3
    clause6 = (not x1) or x2 or (not x3)
    clause7 = x1 or (not x2) or (not x3)

    return clause1 and clause2 and clause3 and clause4 and clause5 and clause6 and clause7


if __name__ == "__main__":
    generate_boolean_assignments()
