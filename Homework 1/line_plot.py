"""
    A sample of using matplotlib
    Kevin Molloy (August 2023)

"""
from matplotlib import pyplot as plt

def main():
    X = [200, 400, 600, 800, 1000]
    Y = [0.468, 0.638, 0.852, 1.075, 1.235]

    plt.plot(X,Y,marker='s',lw=2)
    plt.xlabel("Input Size(in thousands)", fontsize=16)
    plt.ylabel("Runtime(seconds)", fontsize=16)

    # You can interactively show the plot to the terminal using show()
    # or you can save it to a file using savefig. 

    # plt.show()
    plt.savefig(fname='sample_plot.pdf', dpi=300,
                bbox_inches='tight',pad_inches=0.05)
if __name__ == "__main__":
    main()