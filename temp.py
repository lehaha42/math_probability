

def main():
    for i in range(13,18):
        open(f'laba1/t{i}.py', 'w').write('\n\ndef main():\n\tprint()\n\n\nif __name__ == "__main__":\n\tmain()\n')


if __name__ == '__main__':
    main()
