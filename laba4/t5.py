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
	print('a)')
	f(
		x = [0, 2, 4],
		px = [.5, .2, .3],
		y = [-2, 0, 2],
		py = [.1, .6, .3],
		f = lambda a, b: a-b
	)
	print('\nb)')
	f(
		x=[0, 2, 4],
		px = [.5, .2, .3],
		y = [-2, 0, 2],
		py = [.1, .6, .3],
		f = lambda a, b: a * b
	)


if __name__ == "__main__":
	main()
