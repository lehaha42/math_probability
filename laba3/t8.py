

def main():
	t = 25
	p = .1
	a = []
	for i in range(100):
		if t * p - (1 - p) <= i and i <= (t + 1) * p:
			a.append(i)
	print(a)


if __name__ == "__main__":
	main()
