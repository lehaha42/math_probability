from formulas import P2


def main():
	s, s2, m, n = 0, 0, 0, 0
	for i in range(1001):
		if i in range(480, 521):
			s += P2(i, 1000, .5)
		if i <= 480:
			s2 += P2(i, 1000, .5)
		if P2(i, 1000, .5) > m:
			n = i
			m = P2(i, 1000, .5)
	print(f"a) P(x=480) = {P2(480, 1000, .5)}")
	print(f"b) P(x={n}) = {m}")
	print(f"c) P(x<=480) = {s2}")
	print(f"d) P(480<=x<=520) = {s}")



if __name__ == "__main__":
	main()
