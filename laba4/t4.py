import matplotlib.pyplot as plt


def f(x, px, y, py, f):
	z = {}
	for i in range(len(x)):
		for j in range(len(y)):
			if f(x[i], y[j]) in z.keys():
				z[f(x[i], y[j])] += px[i] * py[j]
			else:
				z[f(x[i], y[j])] = px[i] * py[j]

	for k in sorted(z.keys()):
		print(k, ':', z[k])
	z = dict(sorted(z.items()))
	plt.plot(z.keys(), z.values())
	plt.show()


def main():
	f(
		x=[2, 4, 6, 8],
		px = [.4, .2, .1, .3],
		y = [0, 1, 2],
		py = [.5, .2, .3],
		f = lambda a, b: 2 * a + 3 * b
	)


if __name__ == "__main__":
	main()
