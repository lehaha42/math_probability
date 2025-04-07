

def main():
	x = [-2, -1, 0, 1, 2]
	p = [.2, .1, .2]
	p5 = .1
	p4 = sum(p) - p5
	print("     ".join(map(str, x)))
	print("   ".join(map(str, [*p, p4, p5])))
	print(f"D(x) = {sum(map(lambda a, b: a * a * b, x, p + [p4, p5])) - .1 ** 2}")


if __name__ == "__main__":
	main()
