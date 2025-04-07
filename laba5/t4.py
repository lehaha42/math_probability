

def main():
	x = [-2, -1, 3, 8, 9]
	p = [0, .2, .3, 0, .4]
	p[3] = (1 - sum(p)) / 5
	p[0] = p[3] * 4
	print("\n".join(map(lambda a, b: f"{a}\t{b}", x, p)))
	print()
	print("\n".join(map(lambda n, b, c: f"{str(sum(p[:n]))[:7]}\t\t{b} <= x < {c}", [i for i in range(6)], ["-inf"]+x, x+["+inf"])))


if __name__ == "__main__":
	main()
