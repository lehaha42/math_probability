

def main(n = -1):
    arr = [16, 7, 16]
    for j in range(len(arr)) if (n >= len(arr) or n < 0) else [n]:
        for i in range(arr[j]):
            print(f'laba {j+1} task {i+1}:')
            exec(f'import laba{j+1}.t{i+1}\nlaba{j+1}.t{i+1}.main()')
            print()


if __name__ == '__main__':
    main()
