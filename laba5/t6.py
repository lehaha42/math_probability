

def main():
	x = [2, 4, 6, 8]
	p = [.4, .2, .1, .3]
	y = [0, 1, 2]
	g = [.5, .2, .3]
	z = [2, 3]
	Mx = sum(map(lambda a, b: a*b, x, p))
	My = sum(map(lambda a, b: a*b, y, g))
	Mx2 = sum(map(lambda a, b: a*a*b, x, p))
	My2 = sum(map(lambda a, b: a*a*b, y, g))
	Dx = Mx2 - Mx * Mx
	Dy = My2 - My * My
	print(f"M(z) = {sum(map(lambda a, b: a*b, [Mx, My], z))}")
	print(f"D(z) = {sum(map(lambda a, b: a*b*b, [Dx, Dy], z))}")


if __name__ == "__main__":
	main()
