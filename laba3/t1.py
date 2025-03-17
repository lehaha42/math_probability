from formulas import P


def main():
	c = .2
	b = 9
	print(f"1) {P(4, b, c)}")
	print(f"2) а) {P(0, b, c) + P(1, b, c)}")
	print(f"   б) {P(0, b, c) + P(1, b, c) + P(2, b, c)}")
	print(f"   в) {1 - (P(0, b, c) + P(1, b, c))}")
	a = []
	for i in range(100):
		if b*c-(1-c) <= i and i <= b*c+c:
			a.append(i)
	print(f"   г) {a}")


if __name__ == "__main__":
	main()
