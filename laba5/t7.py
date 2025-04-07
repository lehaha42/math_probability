

def main():
	x = [3, 4, 5, 6, 7]
	p = [.1, .2, .4, .1, .2]
	print("a)")
	print("\n".join(map(lambda n, b, c: f"{str(sum(p[:n]))[:4]}\t\t{b} <= x < {c}", [i for i in range(6)], ["-inf"] + x, x + ["+inf"])))
	print("b)")
	print(f"P(A) = {sum(p[4:])}")
	print("c)")
	print(f"M(x) = {sum(map(lambda a, b: a*b, x, p))}")
	print(f"D(x) = {sum(map(lambda a, b: a*a*b, x, p))}")


if __name__ == "__main__":
	main()
