from formulas import P


def main():
	p = .2
	print(f'1) {P(0, 6, p) + P(1, 6, p)}')
	print(f'2) {1 - P(6, 6, p)}')


if __name__ == "__main__":
	main()
