"""
    name:  Your name(s) here

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           Comments here on your code and submission.
"""

# Function to solve the fractional knapsack problem
def fractional_knapsack(items, capacity):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[2], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        name, value, weight = item
        if weight <= capacity:
            knapsack.append((name, value, weight))
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            knapsack.append((name, value * fraction, capacity))
            total_value += value * fraction
            break

    return knapsack, total_value

if __name__ == "__main__":
    # Read input values
    capacity = int(input())
    n = int(input())
    items = []

    for _ in range(n):
        name, value, weight = input().split()
        items.append((name, float(value), float(weight)))

    # Solve the fractional knapsack problem
    knapsack, total_value = fractional_knapsack(items, capacity)

    # Format and print the output
    knapsack_str = ' '.join([f'{name}({value:.2f}, {weight:.2f})' for name, value, weight in knapsack])
    print(knapsack_str)
    print(f'{total_value:.1f}')
