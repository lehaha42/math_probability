from formulas import C


def main():
	p = .4*.9+.6*.8
	for i in range(4):
		print(C(i, 3) * p**i * (1-p)**(3-i))


if __name__ == "__main__":
	main()
