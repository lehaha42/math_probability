from formulas import P2


def main():
	s = 0
	for i in range(652, 761):
		s += P2(i, 1000, .7)
	print(s)


if __name__ == "__main__":
	main()
