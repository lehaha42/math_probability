from formulas import P2


def main():
	for i in range(10000):
		c = P2(i, 10000, .00_005)
		if c != 0:
			print(f'P(x={i}) = {c}, income: {500*10000 - i*50000}')


if __name__ == "__main__":
	main()
