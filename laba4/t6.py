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
		x = [-4, 0, 4],
		px = [.1, .5, .4],
		y = [2, 4],
		py = [.5, .5],
		f = lambda a, b: (a+b)//2
	)


if __name__ == "__main__":
	main()
