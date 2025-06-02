
ACC = 1e-8

def f(y, x):
	return (y(x+ACC/2) - y(x-ACC/2))/ACC


def main():
	y1 = lambda x: .62 + 58.74/x
	y2 = lambda x: 9.3 + 9.83*x
	y3 = lambda x: 11.75 * x**1.6281
	y4 = lambda x: 14.87 * 1.016**x
	M, N, K = 1.2, 6, 2.1
	x = 2.64 + M
	print(f'Э(y1) = {f(y1, x) * x / y1(x)}')
	x = 1.38 + N
	print(f'Э(y2) = {f(y2, x) * x / y2(x)}')
	x = 1.503 + K
	print(f'Э(y3) = {f(y3, x) * x / y3(x)}')
	x = 26.3 + N
	print(f'Э(y4) = {f(y4, x) * x / y4(x)}')


if __name__ == "__main__":
	main()
