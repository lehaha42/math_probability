import matplotlib.pyplot as plt


def main():
    plt.plot([-1, *[i / 16 for i in range(16*6+1)], 7],
             [0, *[(i / 16 / 6) ** 2 for i in range(16*6+1)], 1])
    plt.show()
    print('M(x) = 4')
    print('M(x^2) = 18')
    print('D(x) = 2')


if __name__ == "__main__":
    main()
