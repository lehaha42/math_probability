

def main():
	x = [-2, -1, 0, 1, 2]
	p = [.2, .1, .2, 0, 0]
	p[4] = .1
	p[3] = sum(p[:3]) - p[4]
	print("\n".join(map(lambda a, b: f"{a}\t{b}", x, p)))
	print(f"D(x) = {sum(map(lambda a, b: a * a * b, x, p)) - .1 ** 2}")


if __name__ == "__main__":
	main()
