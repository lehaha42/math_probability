

def main(n = 0):
    arr = [16, 7, 16, 10]
    for j in range(len(arr)) if (n > len(arr) or n < 1) else [n-1]:
        for i in range(arr[j]):
            print(f'laba {j+1} task {i+1}:')
            exec(f'import laba{j+1}.t{i+1}\nlaba{j+1}.t{i+1}.main()')
            print()


if __name__ == '__main__':
    main(4)
