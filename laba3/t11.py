from formulas import P2


def main():
	print(P2(3, 1000, .005))
	print(1-(P2(0, 1000, .005)+P2(1, 1000, .005)+P2(2, 1000, .005)))


if __name__ == "__main__":
	main()
