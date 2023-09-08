"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

"""

def main():
    
    all_noises =  input().split()
    number = int(input())
    animals = {}

    for i in range(0,number):
        temp = input().split()
        animals[temp[2]] = temp[0]

    order = []
    seen = set()
    foxsay = []
    
    
    for noise in all_noises:
        if animals.get(noise, ""):
            if animals[noise] not in seen:
                order.append(animals[noise])
                seen.add(animals[noise])
        else:
            foxsay.append(noise)
    print("what the fox says:", " ".join(foxsay))
    print("also heard:", " ".join(order))

if __name__ == "__main__":
    main()