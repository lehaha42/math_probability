

def main():
	t = 20
	p = .8
	a = []
	for i in range(100):
		if i * p - (1 - p) <= t and t <= (i + 1) * p:
			a.append(i)
	print(a)


if __name__ == "__main__":
	main()
