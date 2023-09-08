"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

"""

def main():
    
    all_noises =  input().split()
    number = int(input())
    animals = [None] * number
    sound = [None] * number

    for i in range(0,number):
        temp = input().split()
        animals[i] = temp[0]
        sound[i] = temp[2]

    order = []
    foxsay = []
    
    for noise in all_noises:
        if noise in sound:
            if animals[sound.index(noise)] not in order:
                order.append(animals[sound.index(noise)])
        else:
            foxsay.append(noise)
    print("what the fox says:", " ".join(foxsay))
    print("also heard:", " ".join(order))
    pass

if __name__ == "__main__":
    main()