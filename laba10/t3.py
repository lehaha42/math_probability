
ACC = 1e-9

def f(y, x):
	return (y(x+ACC/2) - y(x-ACC/2))/ACC


def main():
	M, N, K = 1.2, 6, 2.1
	y = [
		lambda x: .62 + 58.74/x,
		lambda x: 9.3 + 9.83*x,
		lambda x: 11.75 * x**1.6281,
		lambda x: 14.87 * 1.016**x
	]
	x = [
		2.64 + M,
		1.38 + N,
		1.503 + K,
		26.3 + N
	]
	a = list(map(lambda y, x: f(y, x) * x / y(x), y, x))
	b = a.copy()
	b.sort()
	for i in range(4):
		for j in range(4):
			if a[i] == b[j]:
				print(f"Э(y{i+1}) = {a[i]}\t\t{['weak', 'mid', 'strong', 'very strong'][j]}")
				break


if __name__ == "__main__":
	main()
