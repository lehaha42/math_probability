import matplotlib.pyplot as plt


def main():
    plt.plot([-1, *[i / 16 for i in range(16 * 2 + 1)], 3],
             [0, *[(i / 16 / 2) ** 2 for i in range(16 * 2 + 1)], 1])
    plt.show()
    plt.plot([-1, *[i / 16 for i in range(16 * 2 + 1)], 3],
             [0, *[i / 16 / 2 for i in range(16 * 2 + 1)], 1])
    plt.show()
    print('P(x=1) = 0')
    print('P(x<1) = 1/4')
    print('P(1<x<=2) = 3/4')
    print('M(x) = 4/3')
    print('D(x) = 2/9')


if __name__ == "__main__":
    main()
