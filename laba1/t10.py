from formulas import C


def main():
	n = 0
	for i in range(3):
		n += ((C(3-i, 3)*C(2+i, 4))/C(5, 7))*((6-i)/12)
	print(n)
	for i in range(1, 1000):
		if n*i == int(n*i):
			print(f'{int(n*i)}/{i}')
			break


if __name__ == "__main__":
	main()
